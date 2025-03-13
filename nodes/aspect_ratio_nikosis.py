# ComfyUI/custom_nodes/ComfyUI-Nikosis-Nodes/nodes/aspect_ratio_nikosis.py
# A custom ComfyUI node to generate an empty latent for SDXL (4 channels) or SD3/Flux (16 channels)

# Aspect Ratio (nikosis)

import os
import torch
import comfy.model_management as comfy_mm

NODE_FILE = os.path.abspath(__file__)
CUSTOM_NODE_ROOT = os.path.dirname(os.path.dirname(NODE_FILE))


class AspectRatioNikosis:
    def __init__(self):
        self.device = comfy_mm.intermediate_device()

    @classmethod
    def INPUT_TYPES(cls):
        aspect_ratios = [
            "custom",
            "1:1 square 1024x1024",
            "2:3 portrait 832x1216",
            "3:4 portrait 896x1152",
            "4:5 portrait 960x1200", 
            "9:16 portrait 768x1344",
            "9:21 portrait 640x1536",
            "10:16 portrait 800x1280",
            "3:2 landscape 1216x832",            
            "4:3 landscape 1152x896",
            "5:4 landscape 1200x960",
            "16:9 landscape 1344x768",
            "16:10 landscape 1280x800",
            "21:9 landscape 1536x640",
        ]
        
        return {
            "required": {
                "model_type": (["SDXL", "SD3/Flux"], {"default": "SDXL"}),  # Switch between SDXL and SD3/Flux
                "aspect_ratio": (aspect_ratios, {"default": "custom"}),
                "width": ("INT", {"default": 1024, "min": 64, "max": 16384, "step": 8}),
                "height": ("INT", {"default": 1024, "min": 64, "max": 16384, "step": 8}),
                "swap_dimensions": (["Off", "On"], {"default": "Off"}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64}),
            }
        }
    
    RETURN_TYPES = ("LATENT", "INT", "INT")
    RETURN_NAMES = ("empty_latent", "width", "height")
    FUNCTION = "generate_ar_latent"
    CATEGORY = "Latent/Utilities"

    def generate_ar_latent(self, model_type, aspect_ratio, width, height, swap_dimensions, batch_size):
        # Use preset dimensions if not "custom"
        if aspect_ratio != "custom":
            width_str, height_str = aspect_ratio.split(" ")[-1].split("x")
            width, height = int(width_str), int(height_str)
        
        # Swap dimensions if requested
        if swap_dimensions == "On":
            width, height = height, width
        
        # Ensure dimensions are multiples of 8
        width = self.round_to_multiple(width, 8)
        height = self.round_to_multiple(height, 8)
        
        # Set channel count based on model type
        channels = 4 if model_type == "SDXL" else 16  # 4 for SDXL, 16 for SD3/Flux
        
        # Create latent tensor
        latent = torch.zeros([batch_size, channels, height // 8, width // 8], device=self.device)
        
        return {"samples": latent}, width, height
    
    @staticmethod
    def round_to_multiple(value, multiple):
        """Round value to the nearest multiple of 'multiple'."""
        return ((value + multiple - 1) // multiple) * multiple

NODE_CLASS_MAPPINGS = {
    "AspectRatioNikosis": AspectRatioNikosis,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AspectRatioNikosis": "🖌️ Aspect Ratio (nikosis)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'AspectRatioNikosis']
