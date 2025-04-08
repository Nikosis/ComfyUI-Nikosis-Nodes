# Import mappings from individual node files

from .aspect_ratio_nikosis import AspectRatioNikosis
from .text_concatenate_nikosis import TextConcatenateNikosis
from .prompt_multiple_styles_selector_nikosis import PromptMultipleStylesSelectorNikosis
from .prompt_camera_angle_selector_nikosis import PromptCameraAngleSelectorNikosis

NODE_CLASS_MAPPINGS = {
    "AspectRatioNikosis": AspectRatioNikosis,
    "TextConcatenateNikosis": TextConcatenateNikosis,
    "PromptMultipleStylesSelectorNikosis": PromptMultipleStylesSelectorNikosis,
    "PromptCameraAngleSelectorNikosis": PromptCameraAngleSelectorNikosis,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AspectRatioNikosis": "Aspect Ratio (nikosis)",
    "TextConcatenateNikosis": "Text Concatenate (nikosis)",
    "PromptMultipleStylesSelectorNikosis": "Styles Selector (nikosis)",
    "PromptCameraAngleSelectorNikosis": "Camera Angle Selector (nikosis)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
