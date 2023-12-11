from pydantic import BaseModel, Field
from fastapi import FastAPI, UploadFile, File
from typing import List, Optional
import logging
import torch
import data

from models import imagebind_model
from swarms.models.imagebind_model import ModalityType, load_module
from models import lora as LoRA

app = FastAPI()

class InputData(BaseModel):
    text: Optional[List[str]] = Field(None)
    autdio: Optional[UploadFile] = Field(None)
    text: Optional[UploadFile] = Field(None)

@app.post("/process")
async def process_data(input_data: InputData, audio: UploadFile = File(...), vision: UploadFile = File(...)):
    # Load your model here (if not loaded)
    logging.basicConfig(level=logging.INFO, force=True)


lora = True
linear_probing = False
device = "cpu"  # "cuda:0" if torch.cuda.is_available() else "cpu"
load_head_post_proc_finetuned = True

assert not (linear_probing and lora), (
    "Linear probing is a subset of LoRA training procedure for ImageBind. "
    "Cannot set both linear_probing=True and lora=True. "
)

if lora and not load_head_post_proc_finetuned:
    # Hack: adjust lora_factor to the `max batch size used during training / temperature` to compensate missing norm
    lora_factor = 12 / 0.07
else:
    # This assumes proper loading of all params but results in shift from original dist in case of LoRA
    lora_factor = 1

text_list = ["bird", "car", "dog3", "dog5", "dog8", "grey_sloth_plushie"]
image_paths = [
    ".assets/bird_image.jpg",
    ".assets/car_image.jpg",
    ".assets/dog3.jpg",
    ".assets/dog5.jpg",
    ".assets/dog8.jpg",
    ".assets/grey_sloth_plushie.jpg",
]
audio_paths = [
    ".assets/bird_audio.wav",
    ".assets/car_audio.wav",
    ".assets/dog_audio.wav",
]

# Instantiate model
model = imagebind_model.imagebind_huge(pretrained=True)
if lora:
    model.modality_trunks.update(
        LoRA.apply_lora_modality_trunks(
            model.modality_trunks,
            rank=4,
            # layer_idxs={ModalityType.TEXT: [0, 1, 2, 3, 4, 5, 6, 7, 8],
            #             ModalityType.VISION: [0, 1, 2, 3, 4, 5, 6, 7, 8]},
            modality_names=[ModalityType.TEXT, ModalityType.VISION],
        )
    )

    # Load LoRA params if found
    LoRA.load_lora_modality_trunks(
        model.modality_trunks,
        checkpoint_dir=".checkpoints/lora/550_epochs_lora",
        postfix="_dreambooth_last",
    )

    if load_head_post_proc_finetuned:
        # Load postprocessors & heads
        load_module(
            model.modality_postprocessors,
            module_name="postprocessors",
            checkpoint_dir=".checkpoints/lora/550_epochs_lora",
            postfix="_dreambooth_last",
        )
        load_module(
            model.modality_heads,
            module_name="heads",
            checkpoint_dir=".checkpoints/lora/550_epochs_lora",
            postfix="_dreambooth_last",
        )
elif linear_probing:
    # Load heads
    load_module(
        model.modality_heads,
        module_name="heads",
        checkpoint_dir="./.checkpoints/lora/500_epochs_lp",
        postfix="_dreambooth_last",
    )

model.eval()
model.to(device)

# Load data
inputs = {
    ModalityType.TEXT: data.load_and_transform_text(text_list, device),
    ModalityType.VISION: data.load_and_transform_vision_data(
        image_paths, device, to_tensor=True
    ),
    ModalityType.AUDIO: data.load_and_transform_audio_data(audio_paths, device),
}

with torch.no_grad():
    embeddings = model(inputs)

print(
    "Vision x Text: ",
    torch.softmax(
        embeddings[ModalityType.VISION]
        @ embeddings[ModalityType.TEXT].T
        * (lora_factor if lora else 1),
        dim=-1,
    ),
)
print(
    "Audio x Text: ",
    torch.softmax(
        embeddings[ModalityType.AUDIO]
        @ embeddings[ModalityType.TEXT].T
        * (lora_factor if lora else 1),
        dim=-1,
    ),
)
print(
    "Vision x Audio: ",
    torch.softmax(
        embeddings[ModalityType.VISION] @ embeddings[ModalityType.AUDIO].T, dim=-1
    ),
)


    # Prepare your data
    # For text
text_data = item.text

# For audio and vision, you need to save the uploaded file temporarily and then load it
audio_filename = f"/tmp/{audio.filename}"
vision_filename = f"/tmp/{vision.filename}"
with open(audio_filename, "wb") as buffer:
    buffer.write(await audio.read())
with open(vision_filename, "wb") as buffer:
    buffer.write(await vision.read())

    # Now you can load and transform your audio and vision data
    audio_data = data.load_and_transform_audio_data([audio_filename], device)
    vision_data = data.load_and_transform_vision_data([vision_filename], device, to_tensor=True)

    # Then, you can process your data using your model and return the result
    inputs = {
        ModalityType.TEXT: data.load_and_transform_text(text_data, device),
        ModalityType.VISION: vision_data,
        ModalityType.AUDIO: audio_data,
    }
    with torch.no_grad():
        embeddings = model(inputs)

    result = {
        "Vision x Text": torch.softmax(
            embeddings[ModalityType.VISION]
            @ embeddings[ModalityType.TEXT].T
            * (lora_factor if lora else 1),
            dim=-1,
        ).tolist(),
        "Audio x Text": torch.softmax(
            embeddings[ModalityType.AUDIO]
            @ embeddings[ModalityType.TEXT].T
            * (lora_factor if lora else 1),
            dim=-1,
        ).tolist(),
        "Vision x Audio": torch.softmax(
            embeddings[ModalityType.VISION] @ embeddings[ModalityType.AUDIO].T, dim=-1
        ).tolist(),
    }

    return result
