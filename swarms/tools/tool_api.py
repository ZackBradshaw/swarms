from gradio_client import Client
client = Client("http://127.0.0.1:7860/")

# Endpoint 0: VLLM Model URL and Memory Utilization
result = client.predict(
    "Howdy!",  # str in 'VLLM Model URL:' Textbox component
    0,  # int | float (numeric value between 0 and 100) in 'Memory Utilization:' Slider component
    fn_index=0
)
print(result)

# Endpoint 1: Unknown endpoint
result = client.predict(fn_index=1)
print(result)

# Endpoint 2: Model provided, Tokenizer, Accelerators, Huggingface api key
result = client.predict(
    "ChatGPT,ChatGPT",  # str (Option from: [('ChatGPT', 'ChatGPT'), ('GPT-3.5', 'GPT-3.5'), ('decapoda-research/llama-13b-hf', 'decapoda-research/llama-13b-hf')]) in 'Model provided' Dropdown component
    "Howdy!",  # str in 'Tokenizer' Textbox component
    "A100,A100",  # str (Option from: [('A100', 'A100'), ('V100', 'V100'), ('P100', 'P100'), ('K80', 'K80'), ('T4', 'T4'), ('P4', 'P4')]) in 'Accelerators:' Dropdown component
    "Howdy!",  # str in 'Huggingface api key:' Textbox component
    fn_index=2
)
print(result)

# Endpoint 3: Cluster textbox 
result = client.predict(
    "Howdy!",  # str in 'Cluster' Textbox component
    fn_index=3
)
print(result)

# Endpoint 4: Cluster textbox 
result = client.predict(
    "Howdy!",  # str in 'Cluster' Textbox component
    fn_index=4
)
print(result)

# Endpoint 5: Cluster textbox 
result = client.predict(
    "Howdy!",  # str in 'Cluster' Textbox component
    fn_index=5
)
print(result)

# Endpoint 6: Various API keys
result = client.predict(
    "Howdy!",  # str in 'OpenAI API KEY:' Textbox component
    "Howdy!",  # str in 'Wolframalpha app id:' Textbox component
    "Howdy!",  # str in 'Weather api key:' Textbox component
    "Howdy!",  # str in 'Bing subscript key:' Textbox component
    "Howdy!",  # str in 'Stock api key:' Textbox component
    "Howdy!",  # str in 'Bing map key:' Textbox component
    "Howdy!",  # str in 'Baidu translation key:' Textbox component
    "Howdy!",  # str in 'Rapidapi key:' Textbox component
    "Howdy!",  # str in 'Serper key:' Textbox component
    "Howdy!",  # str in 'Google places key:' Textbox component
    "Howdy!",  # str in 'Scenex api key:' Textbox component
    "Howdy!",  # str in 'Steamship api key:' Textbox component
    "Howdy!",  # str in 'Huggingface api key:' Textbox component
    "Howdy!",  # str in 'Amadeus ID:' Textbox component
    "Howdy!",  # str in 'Amadeus key:' Textbox component
    fn_index=6
)
print(result)

result = client.predict(
		"Howdy!",	# str  in 'Tools Search' Textbox component
		fn_index=8
)

result = client.predict(
		fn_index=9
)
print(result)

result = client.predict(
		fn_index=10
)
print(result)

result = client.predict(
		"Howdy!",	# str  in 'parameter_32' Textbox component
		None,	# List[str]  in 'Tools provided' Checkboxgroup component
		"ChatGPT,ChatGPT",	# str (Option from: [('ChatGPT', 'ChatGPT'), ('GPT-3.5', 'GPT-3.5'), ('decapoda-research/llama-13b-hf', 'decapoda-research/llama-13b-hf')]) in 'Model provided' Dropdown component
		fn_index=11
)
print(result)

result = client.predict(
		"Howdy!",	# str  in 'parameter_32' Textbox component
		None,	# List[str]  in 'Tools provided' Checkboxgroup component
		"ChatGPT,ChatGPT",	# str (Option from: [('ChatGPT', 'ChatGPT'), ('GPT-3.5', 'GPT-3.5'), ('decapoda-research/llama-13b-hf', 'decapoda-research/llama-13b-hf')]) in 'Model provided' Dropdown component
		fn_index=12
)
print(result)

result = client.predict(
		fn_index=13
)
print(result)

result = client.predict(
		fn_index=14
)
print(result)

result = client.predict(
		fn_index=15
)
print(result)
