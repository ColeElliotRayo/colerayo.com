top = open("templates/top.html").read()
index = open("content/index.html").read()
testimonials = open("content/testimonials.html").read()
contact = open("content/contact.html").read()
bottom = open("templates/bottom.html").read()

indexFull = top + index + bottom
testimonialsFull = top + testimonials + bottom
contactFull = top + contact + bottom

open("docs/index.html", "w+").write(indexFull)
open("docs/testimonials.html","w+").write(testimonialsFull)
open("docs/contact.html", "w+").write(contactFull)
