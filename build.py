import glob
import os
pages = []

from pprint import pprint

all_html_files = glob.glob("content/*.html")

for file_path in all_html_files:
    file_name = os.path.basename(file_path)
    # print("file_name:", file_name)
    name_only, extension = os.path.splitext(file_name)
    # print(name_only)
    output = "docs/" + (file_name)
    # print(output)
    pages.append({
    "filename": file_path,
    "title": file_path,
    "output": output,
    })

pprint(pages)

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

main()