import os

def get_presentations():
    """
    Returns the list of presentations available
    """
    presentations_path = os.path.join(os.path.dirname(__file__), 'presentations')

    presentations = []

    for filename in os.listdir(presentations_path):
        if filename.endswith('.pdf'):
            presentation_path = os.path.join(presentations_path, filename)
            presentations.append((os.path.basename(presentation_path).replace('.pdf', ''), presentation_path))

    return presentations

if __name__ == '__main__':
    print(get_presentations())
