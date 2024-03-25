WHITEPAPERS = {
    'paper1': {
        'title': 'Whitepaper 1: Understanding the Impact of XYZ',
        'author': 'John Doe',
        'description': 'This whitepaper explores the impact of XYZ on the industry and provides insights on how to prepare for its effects.',
        'url': 'https://example.com/whitepapers/paper1.pdf',
        'date_released': 'January 1, 2023'
    },
    'paper2': {
        'title': 'Whitepaper 2: Challenges and Opportunities in ABC',
        'author': 'Jane Smith',
        'description': 'This whitepaper examines the challenges and opportunities in the ABC market, providing insights and recommendations for success.',
        'url': 'https://example.com/whitepapers/paper2.pdf',
        'date_released': 'March 15, 2023'
    },
    # ... add more whitepapers here
}

def get_all_whitepapers():
    return WHITEPAPERS

def get_whitepaper_by_name(whitepaper_name):
    if whitepaper_name in WHITEPAPERS:
        return WHITEPAPERS[whitepaper_name]
    else:
        return None

def get_list_of_whitepapers():
    return list(WHITEPAPERS.keys())

def download_whitepaper(whitepaper_name, save_directory):
    if whitepaper_name not in WHITEPAPERS:
        print(f"Error: the whitepaper '{whitepaper_name}' doesn't exist.")
        return

    whitepaper = WHITEPAPERS[whitepaper_name]

    # Download the whitepaper
    import urllib.request

    urllib.request.urlretrieve(whitepaper['url'], f"{save_directory}/{whitepaper_name}.pdf")

    print(f"Whitepaper '{whitepaper_name}' downloaded successfully.")

def list_whitepapers():
    print("Available whitepapers:")
    for i, whitepaper_name in enumerate(get_list_of_whitepapers(), start=1):
        whitepaper = WHITEPAPERS[whitepaper_name]
        print(f"{i}. {whitepaper['title']} by {whitepaper['author']}")

# Example usage

# Print the list of available whitepapers
list_whitepapers()

# Download the first whitepaper to the current directory
download_whitepaper('paper1', os.getcwd())

# Display the details of the second whitepaper
print(get_whitepaper_by_name('paper2'))

# Print the list of all available whitepapers
print(get_list_of_whitepapers())
