from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogcore, name = 'blogscore'),
]