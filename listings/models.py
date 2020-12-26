from django.db import models
from django.db.models.deletion import DO_NOTHING
from datetime import datetime
from realtors.models import Realtor

# Create your models here.

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor,on_delete=DO_NOTHING)
    title = models.CharField(max_length=200)
    addresss = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5,decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')
    photo_2 = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')
    photo_3 = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')
    photo_4 = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')
    photo_5 = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')
    photo_6 = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title

