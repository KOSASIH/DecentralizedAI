import os
import json

def create_forums(forum_data):
    """
    Creates forums from forum data.

    Args:
        forum_data (dict): A dictionary of forum data.

    Returns:
        None
    """

    # Create forums directory if it doesn't exist
    if not os.path.exists("community/forums"):
        os.makedirs("community/forums")

    # Iterate through forum data and create forums
    for forum in forum_data:
        with open(f"community/forums/{forum['name']}.json", "w") as forum_file:
            forum_file.write(json.dumps(forum))

# Example forum data
forum_data = [
    {
        "name": "General Discussion",
        "description": "A forum for general discussion about the project.",
        "subforums": [
            {"name": "Introductions", "description": "Introduce yourself to the community."},
            {"name": "Feedback", "description": "Share your feedback about the project."},
            {"name": "Questions", "description": "Ask questions about the project."},
        ]
    },
    {
        "name": "Development",
        "description": "A forum for discussing development-related topics.",
        "subforums": [
            {"name": "Issue Tracking", "description": "Track issues and report bugs."},
            {"name": "Feature Requests", "description": "Request new features for the project."},
            {"name": "Pull Requests", "description": "Review and discuss pull requests."},
        ]
    },
]

# Create forums
create_forums(forum_data)
