# ComfyUI/custom_nodes/ComfyUI-Nikosis-Nodes/__init__.py

# Import the consolidated mappings from the nodes subfolder
from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# Confirmation message
print("Nikosis Nodes Loaded ")
