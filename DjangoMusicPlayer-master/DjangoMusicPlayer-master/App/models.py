from django.db import models

# Create your models here.
class Song(models.Model):
    title= models.TextField(blank=True)
    artist= models.TextField(blank=True)
    image= models.ImageField(blank=True)
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2
    def __str__(self):
        return self.title
