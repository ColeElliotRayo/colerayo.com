import glob
import os
from pprint import pprint
from jinja2 import Template
pages = []

all_html_files = glob.glob("content/*.html")

def populate_dict():
    for file_path in all_html_files:
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        output_path = "docs/" + (file_name)
        pages.append({
        "filename": file_path,
        "title": name_only,
        "output": output_path,
        })

def update_pages():
    for page in pages:
        page_html = open(page['filename']).read()
        template_html = open("templates/base.html").read()
        title = page['title']
        template = Template(template_html)

        output = template.render(
            title=title,
            content=page_html,
            pages=pages
        )
        open(page['output'], "w+").write(output)