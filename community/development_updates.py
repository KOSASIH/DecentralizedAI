import os
import uuid
import json

development_updates_file_path = os.path.join(os.path.dirname(__file__), "development_updates.json")

development_update_structure = {
    "id": None,
    "title": None,
    "description": None,
    "status": None,
    "assignee": None,
    "date": None,
}

def create_development_update(title, description, status, assignee, date):
    update_id = str(uuid.uuid4())
    new_update = {
        "id": update_id,
        "title": title,
        "description": description,
        "status": status,
        "assignee": assignee,
        "date": date,
    }

    with open(development_updates_file_path, "r") as development_updates_file:
        development_updates_data = json.load(development_updates_file)

    development_updates_data.append(new_update)

    with open(development_updates_file_path, "w") as development_updates_file:
        json.dump(development_updates_data, development_updates_file, indent=4)

    return new_update

def get_development_update(update_id):
    with open(development_updates_file_path, "r") as development_updates_file:
        development_updates_data = json.load(development_updates_file)

    for update in development_updates_data:
        if update["id"] == update_id:
            return update

    return None

def list_development_updates():
    with open(development_updates_file_path, "r") as development_updates_file:
        development_updates_data = json.load(development_updates_file)

    return development_updates_data

def update_development_update(update_id, updated_data):
    with open(development_updates_file_path, "r") as development_updates_file:
        development_updates_data = json.load(development_updates_file)

    for update in development_updates_data:
        if update["id"] == update_id:
            update.update(updated_data)
            break

    with open(development_updates_file_path, "w") as development_updates_file:
        json.dump(development_updates_data, development_updates_file, indent=4)

    return True
