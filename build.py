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
            "title": "Index",
        } ,
    ]
    for page in pages:
        print(page)

    page_title = page["title"]
    print (page_title)

    template = open("templates/base.html").read()
    # index generation
    index_content = open("content/index.html").read()
    finished_index_page = template.replace("{{content}}", index_content)
    open("docs/index.html", "w+").write(finished_index_page)
    # testimonials generation
    testimonials_content = open("content/testimonials.html").read()
    finished_testimonials_page = template.replace("{{content}}", testimonials_content)
    open("docs/testimonials.html", "w+").write(finished_testimonials_page)
    # contact generation
    contact_content = open("content/contact.html").read()
    finished_contact_page = template.replace("{{content}}", contact_content)
    open("docs/contact.html", "w+").write(finished_contact_page)


#    indexFull = top + index + bottom
#    testimonialsFull = top + testimonials + bottom
#    contactFull = top + contact + bottom
#    open("docs/index.html", "w+").write(indexFull)
#    open("docs/testimonials.html","w+").write(testimonialsFull)
#    open("docs/contact.html", "w+").write(contactFull)

main() 