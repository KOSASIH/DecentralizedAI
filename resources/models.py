import os
import json

def get_model_paths(model_dir):
    """
    Returns a list of paths for all model files in the given directory
    Args:
        model_dir (str): The path to the directory containing the model files
    Returns:
        list: A list of paths for all model files in the given directory
    """
    model_paths = []
    for root, dirs, files in os.walk(model_dir):
        for file in files:
            if file.endswith('.json'):
                model_paths.append(os.path.join(root, file))
    return model_paths

def load_model(model_path):
    """
    Loads a model from a JSON file
    Args:
        model_path (str): The path to the JSON file containing the model
    Returns:
        dict: The loaded model
    """
    with open(model_path, 'r') as f:
        return json.load(f)

def load_models(model_dir):
    """
    Loads all models from the given directory
    Args:
        model_dir (str): The path to the directory containing the model files
    Returns:
        dict: A dictionary mapping model names to their loaded models
    """
    model_paths = get_model_paths(model_dir)
    models = {}
    for model_path in model_paths:
        model_name = os.path.basename(model_path).split('.')[0]
        models[model_name] = load_model(model_path)
    return models
