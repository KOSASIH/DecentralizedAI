import os

def get_example_configurations():
    """
    Returns a dictionary of example configurations

    Returns:
        dict: A dictionary of example configurations
    """
    example_configurations = {
        "model_file_path": os.path.join(os.path.dirname(__file__), "models", "example.pkl"),
        "dataset_file_path": os.path.join(os.path.dirname(__file__), "datasets", "example.csv"),
        "visualization_file_path": os.path.join(os.path.dirname(__file__), "visualizations", "example.png"),
        "customization_file_path": os.path.join(os.path.dirname(__file__), "customizations", "example.json"),
    }
    return example_configurations


if __name__ == "__main__":
    example_config = get_example_configurations()
    print(example_config)
