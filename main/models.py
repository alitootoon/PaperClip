from django.db import models
from django.contrib.auth.models import Permission, User


class Histogram(models.Model):
    image_id = models.AutoField(primary_key=True)
    histogram = models.CharField(max_length=250, unique=True)
    image_title = models.CharField(max_length=500)
    image = models.FileField(upload_to='media')

    def __str__(self):
        return self.image_title


class Data(models.Model):
    user = models.ForeignKey(User, default=1)
    histogram = models.ForeignKey(Histogram, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=500)
    data_name = models.CharField(max_length=500)
    data_file = models.FileField()

    def __str__(self):
        return self.data_name
