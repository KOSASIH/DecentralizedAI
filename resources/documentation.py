class Documentation:
    def __init__(self):
        self.title = "My Project Documentation"
        self.sections = []
    
    def add_section(self, title, content):
        self.sections.append({
            "title": title,
            "content": content
        })

    def generate_html(self):
        html_content = f"<html><head><title>{self.title}</title></head><body>"

        for section in self.sections:
            html_content += f"<h1>{section['title']}</h1><p>{section['content']}</p>"

        html_content += "</body></html>"

        return html_content
