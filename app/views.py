from django.shortcuts import render
from .models import Experience, Education, WorkCategory, Work, Blog, Contact

def index_view(request):
    experiences = Experience.objects.all()
    works = Work.objects.all()
    contacts = Contact.objects.all()
    workcategs = WorkCategory.objects.all()
    educations = Education.objects.all()

    context = {
        "experiences": experiences,
        "works": works,
        "contacts": contacts,
        "workcategs": workcategs,
        "educations": educations
    }
    return render(request, "index.html", context)

def blog_view(request):
    blog = Blog.objects.all()
    context = {
    "blogs" : blog,
    }
    return render(request, "blog.html", context)



