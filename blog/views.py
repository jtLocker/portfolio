from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

# i want be able to retrieve and print "Sep" from date

def blogcore(request):
    blogs = Blog.objects
    return render(request, "blog/blogcore.html", {"blogs" : blogs})

def detail(request, blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/detail.html", {"blog":blogdetail})