import os
import uuid
import json

release_notes_file_path = os.path.join(os.path.dirname(__file__), "release_notes.json")

release_note_structure = {
    "id": None,
    "title": None,
    "description": None,
    "version": None,
    "date": None,
}

def create_release_note(title, description, version, date):
    note_id = str(uuid.uuid4())
    new_note = {
        "id": note_id,
        "title": title,
        "description": description,
        "version": version,
        "date": date,
    }

    with open(release_notes_file_path, "r") as release_notes_file:
        release_notes_data = json.load(release_notes_file)

    release_notes_data.append(new_note)

    with open(release_notes_file_path, "w") as release_notes_file:
        json.dump(release_notes_data, release_notes_file, indent=4)

    return new_note

def get_release_note(note_id):
    with open(release_notes_file_path, "r") as release_notes_file:
        release_notes_data = json.load(release_notes_file)

    for note in release_notes_data:
        if note["id"] == note_id:
            return note

    return None

def list_release_notes():
    with open(release_notes_file_path, "r") as release_notes_file:
        release_notes_data = json.load(release_notes_file)

    return release_notes_data
