from typing import Any, Optional, Dict
from abc import ABC, abstractmethod
from pydantic import BaseModel, PrivateAttr
import math
import requests
import json
import os


class ToolOutput:

    def __init__(self, result: str):
        """
        Wraps the result returned from a tool.
        """
        self.result = result

        from pydantic import BaseModel

        class ToolOutput(BaseModel):
            result: str

    def __repr__(self):
        return f"ToolOutput(result={self.result})"


# Base Tool class
class Tool(ABC, BaseModel):
    name: str
    description: str
    action_type: str
    input_format: str  # <<< NEW FIELD

    @abstractmethod
    def run(self, input_text: Any) -> str:
        pass

    def get_tool_description(self) -> str:
        return (
            f"Tool: {self.name}\n"
            f"Description: {self.description}\n"
            f"Action Type: {self.action_type}\n"
            f"Input Format: {self.input_format}\n"
        )
    

