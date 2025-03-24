# ComfyUI/custom_nodes/comfyui-nikosis-nodes/__init__.py

import os
import toml
import logging

# Import the consolidated mappings from the nodes subfolder
from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Confirmation message
toml_path = os.path.join(os.path.dirname(__file__), "pyproject.toml")

try:
    with open(toml_path, "r") as f:
        data = toml.load(f)
    version = data["project"]["version"]
except (FileNotFoundError, KeyError):
    version = "Unknown"

# Print with empty lines and version
logger.info("\n\n\033[32mNikosis Nodes Loaded Successfully - v%s\033[0m\n", version)
