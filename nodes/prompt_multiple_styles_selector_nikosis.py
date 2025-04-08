from ..utils.pathfinder import JsonConfigLoader


class PromptMultipleStylesSelectorNikosis:
    def __init__(self):
        self.loader = JsonConfigLoader("styles.json")

    @classmethod
    def INPUT_TYPES(cls):
        # Temporary instance for options
        loader = JsonConfigLoader("styles.json")
        style_options = ["No Style"]
        styles_data = loader.get_data()
        if styles_data:
            style_options.extend(list(styles_data.keys()))

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

    def commence(self, style1="No Style", style2="No Style", style3="No Style", style4="No Style"):
        styles_data = self.loader.get_data()
        if not styles_data or all(s == "No Style" for s in [style1, style2, style3, style4]):
            return "", ""

        pos_prompts = []
        neg_prompts = set()
        for style in [style1, style2, style3, style4]:
            if style != "No Style" and style in styles_data:
                pos_prompt = styles_data[style].get("prompt", "")
                neg_prompt = styles_data[style].get("negative_prompt", "")
                if pos_prompt:
                    pos_prompts.append(pos_prompt)
                if neg_prompt:
                    # Split the negative prompt by commas and strip whitespace
                    terms = [term.strip() for term in neg_prompt.split(",") if term.strip()]
                    neg_prompts.update(terms)

        positive_prompt = ", ".join(pos_prompts)
        negative_prompt = ", ".join(neg_prompts)
        return positive_prompt, negative_prompt


NODE_CLASS_MAPPINGS = {"PromptMultipleStylesSelectorNikosis": PromptMultipleStylesSelectorNikosis}
NODE_DISPLAY_NAME_MAPPINGS = {"PromptMultipleStylesSelectorNikosis": "Styles Selector (nikosis)"}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'PromptMultipleStylesSelectorNikosis']
