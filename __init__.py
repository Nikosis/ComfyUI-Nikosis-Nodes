# ComfyUI/custom_nodes/comfyui-nikosis-nodes/__init__.py

import os
import toml

# Import the consolidated mappings from the nodes subfolder
from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# Confirmation message
toml_path = os.path.join(os.path.dirname(__file__), "pyproject.toml")

try:
    with open(toml_path, "r") as f:
        data = toml.load(f)
    version = data["project"]["version"]
except (FileNotFoundError, KeyError):
    version = "Unknown"

# Print with empty lines and version
print(f"\n\n\033[32mNikosis Nodes Loaded Successfully - v{version}\033[0m\n")
