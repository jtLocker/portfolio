from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(("Test"), max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')