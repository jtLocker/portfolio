from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogcore, name = 'blogscore'),
    path('<int:blog_id>/', views.detail, name = 'detail')
]