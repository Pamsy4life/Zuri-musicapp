from django.db import models
from datetime import datetime 

# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)

    def __str__(self):
        return self.first_name 

class Song(models.Model):
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_released = models.DateField(default=datetime.today)
    #artist_id = models.IntegerField()
    likes = models.IntegerField()

    
    def __str__(self):
        return self.title


class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    #song_id = models.IntegerField()

    def __str__(self):
        return self.content
