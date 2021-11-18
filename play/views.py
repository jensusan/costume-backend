from django.shortcuts import render, redirect
from .models import Play, Character, Todo, Tracker
from .forms import PlayForm, CharacterForm, TodoForm, TrackerForm
from rest_framework import generics
from .serializers import PlaySerializer, TrackerSerializer, TodoSerializer, CharacterSerializer


# Create your views here.
class PlayList(generics.ListCreateAPIView):
    queryset= Play.objects.all()
    serializer_class = PlaySerializer


class PlayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer


class CharacterList(generics.ListCreateAPIView):
    queryset= Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class TodoList(generics.ListCreateAPIView):
    queryset= Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TrackerList(generics.ListCreateAPIView):
    queryset= Tracker.objects.all()
    serializer_class = TrackerSerializer


class TrackerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer


