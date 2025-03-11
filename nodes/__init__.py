# Import mappings from individual node files

from .prompt_multiple_styles_selector_nikosis import NODE_CLASS_MAPPINGS as PMSS_NODE_CLASS, NODE_DISPLAY_NAME_MAPPINGS as PMSS_NODE_DISPLAY
from .text_concatenate_nikosis import NODE_CLASS_MAPPINGS as TC_NODE_CLASS, NODE_DISPLAY_NAME_MAPPINGS as TC_NODE_DISPLAY
from .aspect_ratio_nikosis import NODE_CLASS_MAPPINGS as AR_NODE_CLASS, NODE_DISPLAY_NAME_MAPPINGS as AR_NODE_DISPLAY

# Combine all node class mappings into a single dictionary
NODE_CLASS_MAPPINGS = { **PMSS_NODE_CLASS, **TC_NODE_CLASS, **AR_NODE_CLASS }


# Combine all node display name mappings into a single dictionary
NODE_DISPLAY_NAME_MAPPINGS = { **PMSS_NODE_DISPLAY, **TC_NODE_DISPLAY, **AR_NODE_DISPLAY }

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
