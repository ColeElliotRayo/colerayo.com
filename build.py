def main():
    pages = [
        {
            "filename": "content/index.html",
            "output": "docs/index.html",
            "title": "Index",
        } ,
        {
            "filename": "content/testimonials.html",
            "output": "docs/testimonials.html",
            "title": "Testimonials",
        } ,
        {
            "filename": "content/contact.html",
            "output": "docs/contact.html",
            "title": "Contact",
        } ,
    ]

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


    # index generation
    # index_content = open("content/index.html").read()
    # finished_index_page = template.replace("{{title}}", page_title)
    # finished_index_page = finished_index_page.replace("{{content}}", index_content)
    # open("docs/index.html", "w+").write(finished_index_page)
    

    # testimonials generation
    # testimonials_content = open("content/testimonials.html").read()
    # finished_testimonials_page = template.replace("{{content}}", testimonials_content)
    # open("docs/testimonials.html", "w+").write(finished_testimonials_page)

    # contact generation
    # contact_content = open("content/contact.html").read()
    # finished_contact_page = template.replace("{{content}}", contact_content)
    # open("docs/contact.html", "w+").write(finished_contact_page)

#    open("docs/index.html", "w+").write(indexFull)
#    open("docs/testimonials.html","w+").write(testimonialsFull)
#    open("docs/contact.html", "w+").write(contactFull)

