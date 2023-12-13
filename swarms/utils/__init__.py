from swarms.utils.code_interpreter import SubprocessCodeInterpreter
from swarms.utils.markdown_message import display_markdown_message
from swarms.utils.parse_code import (
    extract_code_in_backticks_in_string,
)
from swarms.utils.tool_logging import get_logger
from swarms.utils.pdf_to_text import pdf_to_text
# swarms/utils/__init__.py

import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
# from swarms.utils.phoenix_handler import phoenix_trace_decorator

__all__ = [
    "display_markdown_message",
    "SubprocessCodeInterpreter",
    "extract_code_in_backticks_in_string",
    "pdf_to_text",
    "get_logger",
    # "phoenix_trace_decorator",
]
