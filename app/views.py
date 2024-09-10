from django.shortcuts import render
from .models import Experience, Education, WorkCategory, Work, Blog, Contact
from django.views.generic.detail import DetailView

def index_view(request):
    experiences = Experience.objects.all()
    works = Work.objects.all()
    contacts = Contact.objects.all()
    workcategs = WorkCategory.objects.all()
    educations = Education.objects.all()
    blogs = Blog.objects.all()

    context = {
        "experiences": experiences,
        "works": works,
        "contacts": contacts,
        "workcategs": workcategs,
        "educations": educations,
        "blogs": blogs,
    }
    return render(request, "index.html", context)

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog.html'
    slug_field = 'slug'


