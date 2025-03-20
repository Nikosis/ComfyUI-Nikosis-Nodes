# ComfyUI/custom_nodes/comfyui-nikosis-nodes/nodes/text_concatenate_nikosis.py
# A custom ComfyUI node to concatenate multiple text inputs with a delimiter and whitespace cleaning option

# Text Concatenate (nikosis)

import os

NODE_FILE = os.path.abspath(__file__)
CUSTOM_NODE_ROOT = os.path.dirname(os.path.dirname(NODE_FILE))


class TextConcatenateNikosis:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_a": ("STRING", {"forceInput": True, "default": ""}),
                "text_b": ("STRING", {"forceInput": True, "default": ""}),
                "delimiter": ("STRING", {"default": ", ", "multiline": False}),
                "clean_whitespace": (["true", "false"], {"default": "true"}),
            },
            "optional": {
                "text_c": ("STRING", {"default": ""}),
                "text_d": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "text_concatenate"
    CATEGORY = "Nikosis/Text"

    def text_concatenate(self, text_a, text_b, delimiter, clean_whitespace, **kwargs):
        # Silently default to "true" if clean_whitespace is invalid
        if clean_whitespace not in ["true", "false"]:
            clean_whitespace = "true"

        text_inputs = []

        # Handle special case for newline delimiter
        if delimiter in ("\n", "\\n"):
            delimiter = "\n"

        # Process required inputs
        if clean_whitespace == "true":
            text_a = text_a.strip() if text_a else ""
            text_b = text_b.strip() if text_b else ""
        if text_a:
            text_inputs.append(text_a)
        if text_b:
            text_inputs.append(text_b)

        # Process optional inputs
        for k in sorted(kwargs.keys()):
            v = kwargs[k]
            if isinstance(v, str):
                if clean_whitespace == "true":
                    v = v.strip()
                if v:
                    text_inputs.append(v)

        # Join and return
        merged_text = delimiter.join(text_inputs)
        return (merged_text,)

NODE_CLASS_MAPPINGS = { "TextConcatenateNikosis": TextConcatenateNikosis }
NODE_DISPLAY_NAME_MAPPINGS = { "TextConcatenateNikosis": "🖌️ Text Concatenate (nikosis)" }
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'TextConcatenateNikosis']