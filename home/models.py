from django.db import models

# Create your models here.

class Video(models.Model):
    thumbnail = models.ImageField(upload_to='home/videos/')
    title = models.CharField(max_length=100)
    url = models.URLField()
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title