# from .base_tool import Tool
# from typing import Any, Optional
# import openai
# import json
# import os

# class ImageGenerationTool(Tool):
#     name: str = "AI Image Generator"
#     description: str = "Generates an image from a given text prompt."
#     action_type: str = "image_generate"
#     input_format: str = """
# {
#   "prompt": "string (description of the image)",
#   "size": "string (image resolution, e.g., '480x480')"
# }"""
    
#     def __init__(self):
#         super().__init__()
#         ##self.api_key =  os.getenv("OPENAI_API_KEY")
#        # openai.api_key = self.api_key

#     def run(self, input_text: Any) -> str:
#         """Generate an image using OpenAI's DALL·E model."""
#         try:
#             # Parse input
#             if isinstance(input_text, str):
#                 try:
#                     input_data = json.loads(input_text)
#                 except json.JSONDecodeError:
#                     return "Error: Input must be valid JSON."
#             else:
#                 input_data = input_text
            
#             prompt = input_data.get("prompt", "")
#             size = input_data.get("size", "480x480")
            
#             if not prompt:
#                 return "Error: No prompt provided for image generation."
            
#             response = openai.Image.create(
#                 model="gpt-4o",  # Adjust if needed
#                 prompt=prompt,
#                 n=1,
#                 size=size,
#                 response_format="url"
#             )

#             image_url = response["data"][0]["url"]
#             return f"Generated Image URL: {image_url}"
            
#         except openai.error.OpenAIError as e:
#             return f"API error: {str(e)}"
#         except Exception as e:
#             return f"Unexpected error: {str(e)}"

#-----------2nd code----------------
# image_generation_tool.py
from .base_tool import Tool

from typing import Any
import openai
import json
import os

from .base_tool import ToolOutput  # Ensure ToolOutput is imported from base_tool

class ImageGenerationTool(Tool):
    name: str = "AI Image Generator"
    description: str = "Generates an image from a given text prompt."
    action_type: str = "image_generate"
    input_format: str = """
{
  "prompt": "string (description of the image)",
  "size": "string (image resolution, e.g., '480x480')"
}"""

    def __init__(self):
        super().__init__()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def run(self, input_text: Any) -> "ToolOutput":
        try:
            # Parse input
            if isinstance(input_text, str):
                try:
                    input_data = json.loads(input_text)
                except json.JSONDecodeError:
                    return ToolOutput(result="Error: Input must be valid JSON.", image_url=None)
            else:
                input_data = input_text

            prompt = input_data.get("prompt", "")
            size = input_data.get("size", "480x1480")

            if not prompt:
                return ToolOutput(result="Error: No prompt provided for image generation.", image_url=None)

            response = openai.Image.create(
                model="dall-e-3",
                prompt=prompt,
                n=1,
                size=size,
                response_format="url"
            )

            image_url = response["data"][0]["url"]
            return ToolOutput(result="Success", image_url=image_url)

        except openai.OpenAIError as e:  # Fix incorrect error reference
            print(f"API error: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
