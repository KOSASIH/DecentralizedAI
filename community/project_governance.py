import os
import uuid
import json

project_governance_file_path = os.path.join(os.path.dirname(__file__), "project_governance.json")

project_governance_structure = {
    "id": None,
    "name": None,
    "description": None,
    "members": None,
}

def create_project_governance(name, description, members):
    project_governance_id = str(uuid.uuid4())
    new_project_governance = {
        "id": project_governance_id,
        "name": name,
        "description": description,
        "members": members,
    }

    with open(project_governance_file_path, "r") as project_governance_file:
        project_governance_data = json.load(project_governance_file)

    project_governance_data.append(new_project_governance)

    with open(project_governance_file_path, "w") as project_governance_file:
        json.dump(project_governance_data, project_governance_file, indent=4)

    return new_project_governance

def get_project_governance(project_governance_id):
    with open(project_governance_file_path, "r") as project_governance_file:
        project_governance_data = json.load(project_governance_file)

    for project_governance in project_governance_data:
        if project_governance["id"] == project_governance_id:
            return project_governance

    return None

def list_project_governances():
    with open(project_governance_file_path, "r") as project_governance_file:
        project_governance_data = json.load(project_governance_file)

    return project_governance_data

def update_project_governance(project_governance_id, updated_data):
    with open(project_governance_file_path, "r") as project_governance_file:
        project_governance_data = json.load(project_governance_file)

    for project_governance in project_governance_data:
        if project_governance["id"] == project_governance_id:
            project_governance.update(updated_data)
            break

    with open(project_governance_file_path, "w") as project_governance_file:
        json.dump(project_governance_data, project_governance_file, indent=4)

    return True
