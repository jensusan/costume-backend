from django import forms
from .models import Play, Tracker, Character, Todo

class PlayForm(forms.ModelForm):

    class Meta:
        model = Play
        fields =('title', 'author', 'reference_img', 'concept', 'director_notes')


class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields =('name', 'actor', 'sketches', 'reference_img', 'notes', 'play')


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields =('task', 'completed', 'play')


class TrackerForm(forms.ModelForm):

    class Meta:
        model = Tracker
        fields =('scene', 'character', 'change', 'notes', 'play')