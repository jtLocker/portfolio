from django.shortcuts import render
from .models import Blog
from django.db.models.functions import ExtractMonth, ExtractDay
import datetime
# Create your views here.

def blogcore(request):
    blogs = Blog.objects.annotate(
    month=ExtractMonth('pub_date')
    # day=ExtractDay('pub_date')
)

    return render(request, "blog/blogcore.html", {"blogs" : blogs})