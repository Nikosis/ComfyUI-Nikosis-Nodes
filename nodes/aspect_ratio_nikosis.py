# ComfyUI/custom_nodes/comfyui-nikosis-nodes/nodes/aspect_ratio_nikosis.py
# A custom ComfyUI node to generate an empty latent for SDXL (4 channels) or SD3/Flux (16 channels)

# Aspect Ratio (nikosis)

import torch
import comfy.model_management as comfy_mm

class AspectRatioNikosis:
    def __init__(self):
        self.device = comfy_mm.intermediate_device()

    @classmethod
    def INPUT_TYPES(cls):
        preset_ratios = [
            "custom",
            "1:2 portrait 704x1408",
            "11:21 portrait 704x1344",
            "4:7 portrait 768x1344",
            "3:5 portrait 768x1280",
            "13:19 portrait 832x1216",
            "2:3 portrait 768x1152",
            "13:18 portrait 832x1152",
            "7:9 portrait 896x1152",
            "14:17 portrait 896x1088",
            "15:17 portrait 960x1088",
            "15:16 portrait 960x1024",
            "1:1 square 1024x1024",
            "16:15 landscape 1024x960",
            "17:15 landscape 1088x960",
            "17:14 landscape 1088x896",
            "9:7 landscape 1152x896",
            "24:17 landscape 1152x832",
            "3:2 landscape 1152x768",
            "19:13 landscape 1216x832",
            "5:3 landscape 1280x768",
            "7:4 landscape 1344x768",
            "12:7 landscape 1344x704",
            "2:1 landscape 1408x704",
            "21:10 landscape 1472x704",
            "12:5 landscape 1536x640",
            "5:2 landscape 1600x640",
            "26:9 landscape 1664x576",
            "3:1 landscape 1728x576",
        ]

        return {
            "required": {
                "model_type": (["SDXL", "SD3/Flux"], {"default": "SD3/Flux"}),
                "preset_aspect_ratio": (preset_ratios, {"default": "custom"}),
                "width": ("INT", {"default": 1024, "min": 16, "max": 16384, "step": 16, "disableInput": True}),
                "height": ("INT", {"default": 1024, "min": 16, "max": 16384, "step": 16, "disableInput": True}),
                "swap_dimensions": ("BOOLEAN", {"default": False, "label_off": "Disabled", "label_on": "Enabled"}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64}),
            }
        }

    RETURN_TYPES = ("LATENT", "INT", "INT")
    RETURN_NAMES = ("latent", "width", "height")
    FUNCTION = "commence"
    CATEGORY = "Nikosis Nodes/latent"

    def commence(self, model_type, preset_aspect_ratio, width, height, swap_dimensions, batch_size):

        # Use preset dimensions if not "custom"
        if preset_aspect_ratio != "custom":
            width_str, height_str = preset_aspect_ratio.split(" ")[-1].split("x")
            width, height = int(width_str), int(height_str)

        # Swap dimensions if requested
        if swap_dimensions:
            width, height = height, width

        # Ensure dimensions are multiples of 16
        width = self.round_to_multiple(width, 16)
        height = self.round_to_multiple(height, 16)

        # Set channel count based on model type
        channels = 4 if model_type == "SDXL" else 16  # 4 for SDXL, 16 for SD3/Flux

        # Create latent tensor
        latent = torch.zeros([batch_size, channels, height // 8, width // 8], device=self.device)

        return {"samples": latent}, width, height

    @staticmethod
    def round_to_multiple(value, multiple):
        """Round value to the nearest multiple of 'multiple'."""
        value = max(64, min(value, 16384))
        return (value // multiple) * multiple


NODE_CLASS_MAPPINGS = {"AspectRatioNikosis": AspectRatioNikosis}
NODE_DISPLAY_NAME_MAPPINGS = {"AspectRatioNikosis": "Aspect Ratio (nikosis)"}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'AspectRatioNikosis']
