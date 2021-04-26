import glob
import os
from pprint import pprint
from jinja2 import Template
pages = []

all_html_files = glob.glob("content/*.html")

for file_path in all_html_files:
    file_name = os.path.basename(file_path)
    name_only, extension = os.path.splitext(file_name)
    output_path = "docs/" + (file_name)
    pages.append({
    "filename": file_path,
    "title": name_only,
    "output": output_path,
    })

pprint(pages)

for page in pages:
    page_html = open(page['filename']).read()
    template_html = open("templates/base.html").read()
    title = page['title']
    template = Template(template_html)
    output = template.render(
        title=title,
        content=page_html
    )
    open(page['output'], "w+").write(output)





def main():
    
    def read_in():
        base = open("templates/base.html").read()
        content = open(page["filename"]).read()
        updated_page = base.replace("{{title}}", page["title"])
        updated_page = updated_page.replace("{{content}}", content)
        return updated_page

    def export_update():
        open(page["output"], "w+").write(read_in())

    for page in pages:
        export_update()

# main()