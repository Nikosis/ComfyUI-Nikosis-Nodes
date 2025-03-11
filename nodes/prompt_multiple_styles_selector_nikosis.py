# ComfyUI/custom_nodes/ComfyUI-Nikosis-Nodes/nodes/prompt_multiple_styles_selector_nikosis.py

import os
import json

print("Loading prompt_multiple_styles_selector_nikosis.py from comfyui-nikosis-nodes")

NODE_FILE = os.path.abspath(__file__)                           # e.g., .../nodes/prompt_multiple_styles_selector_nikosis.py
CUSTOM_NODE_ROOT = os.path.dirname(os.path.dirname(NODE_FILE))  # Up to .../ComfyUI-Nikosis-Nodes/
CONFIG_DIR = os.path.join(CUSTOM_NODE_ROOT, "config")           # .../ComfyUI-Nikosis-Nodes/config/
STYLES_PATH = os.path.join(CONFIG_DIR, "styles.json")           # .../ComfyUI-Nikosis-Nodes/config/styles.json
TEXT_TYPE = "STRING"

MANIFEST = {
    "name": "Prompt Multiple Styles Selector (nikosis)",
    "version": (1, 0, 0),
    "author": "Nikosis",
    "project": "https://github.com/Nikosis/ComfyUI-Nikosis-Nodes",
    "description": "A custom ComfyUI node to select and combine multiple prompt styles from a styles.json file with dropdowns",
}

if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR, exist_ok=True)

class Prompt_Multiple_Styles_Selector_Nikosis:
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

    RETURN_TYPES = (TEXT_TYPE, TEXT_TYPE)
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "multi_style_prompt"
    CATEGORY = "Nikosis/Text"

    def __init__(self):
        self.styles = None
        self.styles_path = STYLES_PATH

    def multi_style_prompt(self, style1="No Style", style2="No Style", style3="No Style", style4="No Style"):
        if self.styles is None and os.path.exists(self.styles_path):
            with open(self.styles_path, 'r') as f:
                self.styles = json.load(f)
        if self.styles is None:
            return ("", "")

        selected_styles = [style1, style2, style3, style4]
        if all(s == "No Style" for s in selected_styles):
            return ("", "")

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

        return (positive_prompt, negative_prompt)

NODE_CLASS_MAPPINGS = {
    "Prompt Multiple Styles Selector (nikosis)": Prompt_Multiple_Styles_Selector_Nikosis
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Prompt Multiple Styles Selector (nikosis)": "🖌️ Prompt Multiple Style Selector (nikosis)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
