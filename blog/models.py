from django.db import models
from django.db.models.functions import datetime, ExtractMonth
# Create your models here.


## ExtractMonth() ??? tryting to get the month for the card
class Blog(models.Model):
    title = models.CharField(("Test"), max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

