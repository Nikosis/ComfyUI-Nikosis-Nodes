from ..utils.pathfinder import JsonConfigLoader


class PromptCameraAngleSelectorNikosis:
    def __init__(self):
        self.loader = JsonConfigLoader("angles.json")

    @classmethod
    def INPUT_TYPES(cls):
        # Temporary instance to get options (won’t persist beyond registration)
        loader = JsonConfigLoader("angles.json")
        angle_options = ["No Style"]
        angles_data = loader.get_data()
        if angles_data:
            angle_options.extend(list(angles_data.keys()))

        return {
            "required": {
                "angle": (angle_options, {"default": "No Style"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("positive_prompt",)
    FUNCTION = "commence"
    CATEGORY = "Nikosis Nodes/prompt"

    def commence(self, angle="No Style"):
        angles_data = self.loader.get_data()
        if angle == "No Style" or not angles_data:
            return "",
        prompt = angles_data.get(angle, {}).get("prompt", "")
        return prompt if prompt else "",


NODE_CLASS_MAPPINGS = {"PromptCameraAngleSelectorNikosis": PromptCameraAngleSelectorNikosis, }
NODE_DISPLAY_NAME_MAPPINGS = {"PromptCameraAngleSelectorNikosis": "Camera Angle Selector (nikosis)", }
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'PromptCameraAngleSelectorNikosis']
