# resources/legal_documents.py

LEGAL_DOCUMENTS = [
    {
        'name': 'Privacy Policy',
        'description': 'Our privacy policy explains how we collect, use, and protect your personal information.',
        'url': '/privacy-policy'
    },
    {
        'name': 'Terms of Service',
        'description': 'Our terms of service outline the rules and regulations for using our platform.',
        'url': '/terms-of-service'
    },
    {
        'name': 'Copyright Notice',
        'description': 'Our copyright notice explains our ownership of the content on our platform.',
        'url': '/copyright-notice'
    }
]

def get_legal_documents():
    """
    Returns a list of legal documents.

    :return: A list of legal documents.
    """
    return LEGAL_DOCUMENTS

def get_legal_document(document_name):
    """
    Returns the requested legal document.

    :param document_name: The name of the legal document to retrieve.
    :return: The requested legal document.
    """
    for document in LEGAL_DOCUMENTS:
        if document['name'] == document_name:
            return document

    return None

def generate_legal_documents_page():
    """
    Generates a legal documents page for the website.

    :return: The HTML for the legal documents page.
    """
    html = '<h1>Legal Documents</h1>\n'
    html += '<ul>\n'

    for document in LEGAL_DOCUMENTS:
        html += f"<li><a href='{document['url']}'>{document['name']}</a></li>\n"

    html += '</ul>\n'

    return html

if __name__ == '__main__':
    print(generate_legal_documents_page())
