from django.shortcuts import render
from .models import Experience, Education, WorkCategory, Work, Blog, Contact
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def index_view(request):
    experiences = Experience.objects.all()
    works = Work.objects.all()
    contacts = Contact.objects.all()
    workcategs = WorkCategory.objects.all()
    educations = Education.objects.all()
    blogs = Blog.objects.all()

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            new_contact = Contact(name=name, email=email, message=message)
            print(new_contact)
            new_contact.save()
            messages.success(request, "Sizning xabaringiz yuborildi!!!")
            return HttpResponseRedirect(reverse('home-page'))
        except Exception as e:
            messages.error(request, "Xabaringiz yuborishda xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")

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
