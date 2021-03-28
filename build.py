top = open("templates/top.html").read()
index = open("content/index.html").read()
testimonials = open("content/testimonials.html").read()
contact = open("content/contact.html").read()
bottom = open("templates/bottom.html").read()

indexFull = top + index + bottom
testimonialsFull = top + testimonials + bottom
contactFull = top + contact + bottom

open("docs/indexFull.html", "w+").write(indexFull)
open("docs/testimonialsFull.html","w+").write(testimonialsFull)
open("docs/contactFull.html", "w+").write(contactFull)
