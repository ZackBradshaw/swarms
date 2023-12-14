from swarms.structs import Agent
from swarms.models.gpt4_vision_api import GPT4VisionAPI
from swarms.prompts.multi_modal_autonomous_instruction_prompt import (
    MULTI_MODAL_AUTO_AGENT_SYSTEM_PROMPT_1,
)
from swarms.tools.tools_controller import MTQuestionAnswerer, load_valid_tools

llm = GPT4VisionAPI()

task = (
    "Analyze this image of an assembly line and identify any issues"
    " such as misaligned parts, defects, or deviations from the"
    " standard assembly process. IF there is anything unsafe in the"
    " image, explain why it is unsafe and how it could be improved."
)
img = "assembly_line.jpg"

## Initialize the workflow
agent = Agent(
    llm=llm,
    max_loops=1,
    dashboard=True,
)

## Define the endpoint and parameters for the file operation tool
endpoint = "/write_file"
params = {"file_path": "analysis.txt", "text": "Analysis of the assembly line will be written here."}

## Use the call_api function to call the file operation tool
## But first, check if the agent has the 'call_api' attribute
if hasattr(agent, 'call_api'):
    response = agent.call_api(endpoint, params)
else:
    print("The agent does not have the 'call_api' attribute.")
    response = None

## Check the response
if response and "Error" in response:
    print("An error occurred while writing the file.")
elif response:
    print("The file was written successfully.")
else:
    print("No response was received from the API call.")

## Load the tools
tools_mappings = {
    "klarna": "https://www.klarna.com/",
    "chemical-prop": "http://127.0.0.1:8079/tools/chemical-prop/",
    "wolframalpha": "http://127.0.0.1:8079/tools/wolframalpha/",
    "weather": "http://127.0.0.1:8079/tools/weather/",
}

tools = load_valid_tools(tools_mappings)

## Initialize the MTQuestionAnswerer with the loaded tools
qa = MTQuestionAnswerer(openai_api_key="", all_tools=tools)

## Build the runner
agent_executor = qa.build_runner()

## Run the task
agent_executor(task)
