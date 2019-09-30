from django.shortcuts import render
from .models import Job

# Create your views here.


#this function does not get manually called at any point - 
#this passes a request, location, and dictionary of objects? to pass

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})