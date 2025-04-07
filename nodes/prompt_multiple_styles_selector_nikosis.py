import os
import json


NODE_FILE = os.path.abspath(__file__)
CUSTOM_NODE_ROOT = os.path.dirname(os.path.dirname(NODE_FILE))
CONFIG_DIR = os.path.join(CUSTOM_NODE_ROOT, "config")
STYLES_PATH = os.path.join(CONFIG_DIR, "styles.json")


if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR, exist_ok=True)


class PromptMultipleStylesSelectorNikosis:
    @classmethod
    def INPUT_TYPES(cls):
        style_options = ["No Style"]
        if os.path.exists(STYLES_PATH):
            with open(STYLES_PATH, 'r') as f:
                styles = json.load(f)
                style_options.extend(list(styles.keys()))

        return {
            "required": {
                "style1": (style_options, {"default": "No Style"}),
                "style2": (style_options, {"default": "No Style"}),
                "style3": (style_options, {"default": "No Style"}),
                "style4": (style_options, {"default": "No Style"}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "commence"
    CATEGORY = "Nikosis Nodes/prompt"

    def __init__(self):
        self.styles = None
        self.styles_path = STYLES_PATH

    def commence(self, style1="No Style", style2="No Style", style3="No Style", style4="No Style"):
        if self.styles is None and os.path.exists(self.styles_path):
            with open(self.styles_path, 'r') as f:
                self.styles = json.load(f)
        if self.styles is None:
            return "", ""

        selected_styles = [style1, style2, style3, style4]
        if all(s == "No Style" for s in selected_styles):
            return "", ""

        pos_prompts = []
        neg_prompts = []

        for style in selected_styles:
            if style in self.styles and style != "No Style":
                pos_prompt = self.styles[style].get("prompt", "")
                neg_prompt = self.styles[style].get("negative_prompt", "")
                if pos_prompt:
                    pos_prompts.append(pos_prompt)
                if neg_prompt:
                    neg_prompts.append(neg_prompt)

        positive_prompt = ", ".join(pos_prompts)
        negative_prompt = ", ".join(neg_prompts)

        return positive_prompt, negative_prompt

NODE_CLASS_MAPPINGS = { "PromptMultipleStylesSelectorNikosis": PromptMultipleStylesSelectorNikosis }
NODE_DISPLAY_NAME_MAPPINGS = { "PromptMultipleStylesSelectorNikosis": "Prompt Multiple Style Selector (nikosis)" }
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'PromptMultipleStylesSelectorNikosis']
