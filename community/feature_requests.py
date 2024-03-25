import os
import json

def create_feature_request(request_data):
    """
    Create a new feature request from the provided data.

    Args:
        request_data (dict): A dictionary containing the feature request data, including the user's name, email, and description of the feature.

    Returns:
        None
    """

    # Check if the feature requests directory exists, and create it if it doesn't
    feature_requests_dir = os.path.join(os.path.dirname(__file__), "feature_requests")
    if not os.path.exists(feature_requests_dir):
        os.makedirs(feature_requests_dir)

    # Generate a unique ID for the feature request
    request_id = generate_unique_id()

    # Add the ID to the request data
    request_data["id"] = request_id

    # Save the feature request data to a JSON file
    with open(os.path.join(feature_requests_dir, f"{request_id}.json"), "w") as request_file:
        json.dump(request_data, request_file, indent=4)

def generate_unique_id():
    """
    Generate a unique ID for the feature request.

    Returns:
        str: A unique ID for the feature request.
    """

    import uuid

    return str(uuid.uuid4())

def get_feature_request(request_id):
    """
    Retrieve the feature request with the given ID.

    Args:
        request_id (str): The ID of the feature request to retrieve.

    Returns:
        dict: The feature request data, or None if the request ID is not found.
    """

    feature_requests_dir = os.path.join(os.path.dirname(__file__), "feature_requests")

    for filename in os.listdir(feature_requests_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(feature_requests_dir, filename)
            with open(filepath, "r") as request_file:
                request_data = json.load(request_file)
                if request_data["id"] == request_id:
                    return request_data

    return None

def list_feature_requests():
    """
    List all feature requests.

    Returns:
        list: A list of dictionaries, each containing the data for a single feature request.
    """

    feature_requests_dir = os.path.join(os.path.dirname(__file__), "feature_requests")

    requests = []

    for filename in os.listdir(feature_requests_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(feature_requests_dir, filename)
            with open(filepath, "r") as request_file:
                request_data = json.load(request_file)
                requests.append(request_data)

    return requests

def update_feature_request(request_id, updated_data):
    """
    Update the feature request with the given ID with the provided data.

    Args:
        request_id (str): The ID of the feature request to update.
        updated_data (dict): A dictionary containing the updated feature request data.

    Returns:
        bool: True if the feature request was updated successfully, False otherwise.
    """

    feature_requests_dir = os.path.join(os.path.dirname(__file__), "feature_requests")

    for filename in os.listdir(feature_requests_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(feature_requests_dir, filename)
            with open(filepath, "r") as request_file:
                request_data = json.load(request_file)
                if request_data["id"] == request_id:
                    request_data.update(updated_data)
                    with open(filepath, "w") as request_file:
                        json.dump(request_data, request_file, indent=4)
Here's an updated version of your code with some improvements:

```python
import os
import json
from uuid import uuid4

def create_feature_request(request_data):
    """
    Create a new feature request from the provided data.

    Args:
        request_data (dict): A dictionary containing the feature request data, including the user's name, email, and description of the feature.

    Returns:
        None
    """

    # Check if the feature requests directory exists, and create it if it doesn't
    feature_requests_dir = os.path.join(os.path.dirname(__file__), "feature_requests")
    os.makedirs(feature_requests_dir, exist_ok=True)

    # Generate a unique ID for the feature request
    request_id = str(uuid4())

    # Add the ID to the request data
    request_data["id"] = request_id

    # Save the feature request data to a JSON file
    with open(os.path.join(feature_requests_dir, f"{request_id}.json"), "w") as request_file:
        json.dump(request_data, request_file, indent=4)

def get_feature_request(request_id):
    """
    Retrieve the feature request with the given ID.

    Args:
        request_id (str): The ID of the feature request to retrieve.

    Returns:
        dict: The feature request data, or None if the request ID is not found.
    """

    feature_requests_dir = os.path.join(os.path.dirname(__file__), "feature_requests")

    for filename in os.listdir(feature_requests_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(feature_requests_dir, filename)
            with open(filepath, "r") as request_file:
                request_data = json.load(request_file)
                if request_data["id"] == request_id:
                    return request_data

    return None

def list_feature_requests():
    """
    List all feature requests.

    Returns:
        list: A list of dictionaries, each containing the data for a single feature request.
    """

    feature_requests_dir = os.path.join(os.path.dirname(__file__), "feature_requests")

    requests = []

    for filename in os.listdir(feature_requests_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(feature_requests_dir, filename)
            with open(filepath, "r") as request_file:
                request_data = json.load(request_file)
                requests.append(request_data)

    return requests

def update_feature_request(request_id, updated_data):
    """
    Update the feature request with the given ID with the provided data.

    Args:
        request_id (str): The ID of the feature request to update.
        updated_data (dict): A dictionary containing the updated feature request data.

    Returns:
        bool: True if the feature request was updated successfully, False otherwise.
    """

    feature_requests_dir = os.path.join(os.path.dirname(__file__), "feature_requests")

    for filename in os.listdir(feature_requests_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(feature_requests_dir, filename)
            with open(filepath, "r") as request_file:
                request_data = json.load(request_file)
                if request_data["id"] == request_id:
                    request_data.update(updated_data)
                    with open(filepath, "w") as request_file:
                        json.dump(request_data, request_file, indent=4)
                    return True

    return False
