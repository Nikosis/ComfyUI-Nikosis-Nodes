# ComfyUI/custom_nodes/comfyui-nikosis-nodes/nodes/text_concatenate_nikosis.py
# A custom ComfyUI node to concatenate multiple text inputs with a delimiter and whitespace cleaning option

# Text Concatenate (nikosis)

class TextConcatenateNikosis:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_a": ("STRING", {"forceInput": True, "default": ""}),
                "text_b": ("STRING", {"forceInput": True, "default": ""}),
            },
            "optional": {
                "text_c": ("STRING", {"default": ""}),
                "text_d": ("STRING", {"default": ""}),
                "delimiter": ("STRING", {"default": ", ", "multiline": False, "disableInput": True}),
                "clean_whitespace": ("BOOLEAN", {"default": True, "label_off": "Disabled", "label_on": "Enabled", "disableInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "text_concatenate"
    CATEGORY = "Nikosis-Nodes/Text"

    def text_concatenate(self, text_a, text_b, delimiter, clean_whitespace, **kwargs):
        # Handle newline delimiter
        delimiter = delimiter.replace("\\n", "\n")

        # Process all text inputs
        texts = []
        for text in [text_a, text_b, kwargs.get("text_c", ""), kwargs.get("text_d", "")]:
            if clean_whitespace:  # Clean leading/trailing whitespace
                text = text.strip() if text else ""
                text = " ".join(text.split())  # remove spaces in between
            if text:
                texts.append(text)

        # Join and return
        merged_text = delimiter.join(texts)
        return (merged_text,)


NODE_CLASS_MAPPINGS = {"TextConcatenateNikosis": TextConcatenateNikosis}
NODE_DISPLAY_NAME_MAPPINGS = {"TextConcatenateNikosis": "🖌️ Text Concatenate (nikosis)"}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'TextConcatenateNikosis']
