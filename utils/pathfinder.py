import os
import json


class JsonConfigLoader:
    def __init__(self, filename):
        # Build path
        node_file = os.path.abspath(__file__)
        custom_node_root = os.path.dirname(os.path.dirname(node_file))
        config_dir = os.path.join(custom_node_root, "config")
        self.file_path = os.path.join(config_dir, filename)

        # Create config directory if it doesn’t exist
        try:
            if not os.path.exists(config_dir):
                os.makedirs(config_dir, exist_ok=True)
        except OSError as e:
            print(f"Warning: Could not create config directory {config_dir}: {e}")

        # Load the JSON file
        self.data = {}
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as f:
                    loaded_data = json.load(f)
                    if isinstance(loaded_data, dict):
                        self.data = loaded_data
                    else:
                        print(f"Warning: {self.file_path} does not contain a valid dictionary")
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load {self.file_path}: {e}")

    def get_data(self):
        """Return the loaded JSON data."""
        return self.data
