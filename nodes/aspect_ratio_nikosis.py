# ComfyUI/custom_nodes/ComfyUI-Nikosis-Nodes/nodes/aspect_ratio_nikosis.py

import os
import torch

NODE_FILE = os.path.abspath(__file__)
CUSTOM_NODE_ROOT = os.path.dirname(os.path.dirname(NODE_FILE))  # Up to .../ComfyUI-Nikosis-Nodes/

MANIFEST = {
    "name": "Aspect Ratio (nikosis)",
    "version": (1, 0, 0),
    "author": "Nikosis",
    "project": "https://github.com/Nikosis/ComfyUI-Nikosis-Nodes",
    "description": "A custom ComfyUI node to generate an aspect ratio",
}

class Aspect_Ratio_Nikosis:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
    
        aspect_ratios = ["custom",
                                  "1:1 square 1024x1024",
                                  "3:4 portrait 896x1152",
                                  "5:8 portrait 832x1216",
                                  "9:16 portrait 768x1344",
                                  "9:21 portrait 640x1536",
                                  "4:3 landscape 1152x896",
                                  "3:2 landscape 1216x832",
                                  "16:9 landscape 1344x768",
                                  "21:9 landscape 1536x640"]
        
        return {
            "required": {
                "width": ("INT", {"default": 1024, "min": 64, "max": 8192}),
                "height": ("INT", {"default": 1024, "min": 64, "max": 8192}),
                "aspect_ratio": (aspect_ratios,),
                "swap_dimensions": (["Off", "On"],),
                "upscale_factor": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 100.0, "step":0.1}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64})
            }
        }
    RETURN_TYPES = ("INT", "INT", "FLOAT", "INT", "LATENT", )
    RETURN_NAMES = ("width", "height", "upscale_factor", "batch_size", "empty_latent", )
    FUNCTION = "aspect_ratio"
    CATEGORY = "Nikosis/Aspect Ratio"

    def aspect_ratio(self, width, height, aspect_ratio, swap_dimensions, upscale_factor, batch_size):
        if aspect_ratio == "1:1 square 1024x1024":
            width, height = 1024, 1024
        elif aspect_ratio == "3:4 portrait 896x1152":
            width, height = 896, 1152
        elif aspect_ratio == "5:8 portrait 832x1216":
            width, height = 832, 1216
        elif aspect_ratio == "9:16 portrait 768x1344":
            width, height = 768, 1344
        elif aspect_ratio == "9:21 portrait 640x1536":
            width, height = 640, 1536
        elif aspect_ratio == "4:3 landscape 1152x896":
            width, height = 1152, 896
        elif aspect_ratio == "3:2 landscape 1216x832":
            width, height = 1216, 832
        elif aspect_ratio == "16:9 landscape 1344x768":
            width, height = 1344, 768
        elif aspect_ratio == "21:9 landscape 1536x640":
            width, height = 1536, 640

        if swap_dimensions == "On":
            width, height = height, width
             
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])

        return(width, height, upscale_factor, batch_size, {"samples":latent}, )  

NODE_CLASS_MAPPINGS = {
    "Aspect Ratio (nikosis)": Aspect_Ratio_Nikosis,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Aspect Ratio (nikosis)": "🖌️ Aspect Ratio (nikosis)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
