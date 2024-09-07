from django.shortcuts import render
from .models import ResumeCategory, Resume, WorkCategory, Work, Blog, Contact

def index_view(request):
    resume = Resume.objects.all()
    work = Work.objects.all()
    contact = Contact.objects.all()
    blog = Blog.objects.all()
    workcateg = WorkCategory.objects.all()
    context = {
        "resumes": resume,
        "works" : work,
        "contacts" : contact,
        "blogs" : blog,
        "workcategs": workcateg,
    }
    return render(request, "index.html", context)

def blog_view(request):
    return render(request, "blog.html")



