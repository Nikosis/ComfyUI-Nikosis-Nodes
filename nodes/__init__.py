# Import mappings from individual node files

from .aspect_ratio_nikosis import AspectRatioNikosis
from .text_concatenate_nikosis import TextConcatenateNikosis
from .prompt_multiple_styles_selector_nikosis import PromptMultipleStylesSelectorNikosis

NODE_CLASS_MAPPINGS = {
    "AspectRatioNikosis": AspectRatioNikosis,
    "TextConcatenateNikosis": TextConcatenateNikosis,
    "PromptMultipleStylesSelectorNikosis": PromptMultipleStylesSelectorNikosis,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AspectRatioNikosis": "Aspect Ratio (nikosis)",
    "TextConcatenateNikosis": "Text Concatenate (nikosis)",
    "PromptMultipleStylesSelectorNikosis": "Prompt Multiple Styles Selector (nikosis)",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']