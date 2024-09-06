from django.shortcuts import render

def index_view(request):
    return render(request, "index.html")

def blog_view(request):
    return render(request, "blog.html")