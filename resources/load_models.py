from resources.models import load_models

models = load_models('resources/models')
# Use the loaded models
for name, model in models.items():
    print(f"Loaded model: {name}")
