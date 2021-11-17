from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Play(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    reference_img = models.ImageField(upload_to='uploads/', blank=True, null=True)
    concept = models.CharField(max_length=255)
    director_notes = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    notes = models.CharField(max_length=300)
    sketches = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    reference_img = models.ImageField(upload_to='uploads/', blank=True, null=True)
    play_id = models.ForeignKey(Play, related_name='characters', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Todo(models.Model):
    play_id = models.ForeignKey(Play, related_name='todos', on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task


class Tracker(models.Model):
    scene = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    change = models.CharField(max_length=100)
    notes = models.CharField(max_length=300)
    duration = models.CharField(max_length=100)
    play_id = models.ForeignKey(Play, related_name='tracker', on_delete=models.CASCADE)

    def __str__(self):
        return self.scene
    