from django.db import models
from django.contrib.auth.models import User

class TrainingVideo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField()
    order = models.IntegerField() 

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(TrainingVideo, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
