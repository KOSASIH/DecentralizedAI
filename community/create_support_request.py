import os
import uuid
import json

def create_support_request(request_data):
    """
    Create a new support request from the provided data.

    Args:
        request_data (dict): A dictionary containing the support request data, including the user's name, email, and description of the issue.

    Returns:
        None
    """

    # Check if the support requests directory exists, and create it if it doesn't
    support_requests_dir = os.path.join(os.path.dirname(__file__), "support_requests")
    os.makedirs(support_requests_dir, exist_ok=True)

    # Generate a unique ID for the support request
    request_id = str(uuid4())

    # Add the ID to the request data
    request_data["id"] = request_id

    # Save the support request data to a JSON file
    with open(os.path.join(support_requests_dir, f"{request_id}.json"), "w") as request_file:
        json.dump(request_data, request_file, indent=4)

def get_support_request(request_id):
    """
    Retrieve the support request with the given ID.

    Args:
        request_id (str): The ID of the support request to retrieve.

    Returns:
        dict: The support request data, or None if the request ID is not found.
    """

    support_requests_dir = os.path.join(os.path.dirname(__file__), "support_requests")

    for filename in os.listdir(support_requests_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(support_requests_dir, filename)
            with open(filepath, "r") as request_file:
                request_data = json.load(request_file)
                if request_data["id"] == request_id:
                    return request_data

    return None

def list_support_requests():
    """
    List all support requests.

    Returns:
        list: A list of dictionaries, each containing the data for a single support request.
    """

    support_requests_dir = os.path.join(os.path.dirname(__file__), "support_requests")

    requests = []

    for filename in os.listdir(support_requests_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(support_requests_dir, filename)
            with open(filepath, "r") as request_file:
                request_data = json.load(request_file)
                requests.append(request_data)

    return requests

def update_support_request(request_id, updated_data):
    """
    Update the support request with the given ID with the provided data.

    Args:
        request_id (str): The ID of the support request to update.
        updated_data (dict): A dictionary containing the updated support request data.

    Returns:
        bool: True if the support request was updated successfully, False otherwise.
    """

    support_requests_dir = os.path.join(os.path.dirname(__file__), "support_requests")

    for filename in os.listdir(support_requests_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(support_requests_dir, filename)
            with open(filepath, "r") as request_file:
                request_data = json.load(request_file)
                if request_data["id"] == request_id:
                    request_data.update(updated_data)
                    with open(filepath, "w") as request_file:
                        json.dump(request_data, request_file, indent=4)
                    return True

    return False
