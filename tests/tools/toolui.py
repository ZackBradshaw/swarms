import sys
from unittest import result
import gradio_client
import pytest
import os
from unittest.mock import patch, MagicMock
from app import answer_by_tools
from swarms.app import start_tool_server
from swarms.app import set_environ, load_tools, download_model
import pytest
from gradio_client import *
from swarms.tools.tool_controller import ToolInfo


current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(current_dir, ".."))

HOST = "localhost"
PORT = 8000

# TODO fix this test

def test_set_environ():
    @patch("app.LLM")
    def test_download_model(mock_llm):
        # Arrange
        model_url = "facebook/opt-125m"
        memory_utilization = 8
        mock_model = MagicMock()
        mock_llm.return_value = mock_model

        # Act
        result = download_model(model_url, memory_utilization)

        # Assert
        mock_llm.assert_called_once_with(
            model=model_url,
            trust_remote_code=True,
            gpu_memory_utilization=memory_utilization,
        )
        self.assertEqual(
            result,
            gradio_client.update(choices=[(model_url.split("/")[-1], mock_model)]),
        )

    def test_load_tools(self):
        # Call the function
        result = load_tools()
        
@pytest.mark.unit
def test_start_tool_server():
    # Mock server creation
    with patch("socket.socket") as mock_socket:
        start_tool_server()

        # Assert socket creation and port binding
        mock_socket.assert_called_once()
        mock_socket().bind.assert_called_once_with((HOST, PORT))

@pytest.mark.unit
def test_tools():
    # Define a list of tools to test
    tools_to_test = ["file_operation_tool", "tool2", "tool3"]

    for tool in tools_to_test:
        # Mock tool information access
        with patch("gradio_interface.VALID_TOOLS_INFO", {tool: {"desc": "description"}}):
            tools = load_tools()

            # Assert tool list creation
            assert tools == [ToolInfo(tool, "description")]
        
        @pytest.mark.unit
        def test_answer_by_tools():
            # Mock user input and tool/model availability
            with patch("gradio_interface.get_user_input", return_value="question"):
                with patch("gradio_interface.are_tools_available", return_value=True):
                    answer_by_tools()

                    # Assert tool/model calls
                    assert tool.process.called_once_with("question")
                    assert model1.predict.called_once_with(tool.process.return_value)

        # Check if the function returns the expected result
assert result is not None
assert isinstance(result, list)
