from django.shortcuts import render, redirect
from .models import Play, Character, Todo, Tracker
from .forms import PlayForm, CharacterForm, TodoForm, TrackerForm


# Create your views here.
def play_list(request):
    plays = Play.objects.all()
    return render(request, 'play/play_list.html', {'plays': plays} )


def character_list(request):
    characters = Character.objects.all()
    return render(request, {'characters': characters} )


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, {'todos': todos} )


def tracker_list(request):
    trackers = Tracker.objects.all()
    return render(request, {'trackers': trackers} )


def play_detail(request, pk):
    play = Play.objects.get(id=pk)
    return render(request, {'play': play})


def character_detail(request, pk):
    character = Character.objects.get(id=pk)
    return render(request, {'character': character})


def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, {'todo': todo})


def tracker_detail(request, pk):
    tracker = Tracker.objects.get(id=pk)
    return render(request, {'tracker': tracker})


def play_create(request):
    if request.method == 'POST':
        form = PlayForm(request.POST)
        if form.isValid():
            play = form.save()
            return redirect('play_detail', pk=play.pk)
    else:
        form = PlayForm()
    return render(request, {'form': form})


def character_create(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.isValid():
            character = form.save()
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm()
    return render(request, {'form': form})


def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.isValid():
            todo = form.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()
    return render(request, {'form': form})


def tracker_create(request):
    if request.method == 'POST':
        form = TrackerForm(request.POST)
        if form.isValid():
            tracker = form.save()
            return redirect('tracker_detail', pk=tracker.pk)
    else:
        form = TrackerForm()
    return render(request, {'form': form})


def play_edit(request, pk):
    play = Play.objects.get(pk=pk)
    if request.method == "POST":
        form = PlayForm(request.POST, instance=play)
        if form.is_valid():
            play = form.save()
            return redirect('play_detail', pk=play.pk)
    else:
        form = PlayForm(instance=play)
    return render(request, {'form': form})


def character_edit(request, pk):
    character = Character.objects.get(pk=pk)
    if request.method == "POST":
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            character = form.save()
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm(instance=character)
    return render(request, {'form': form})


def todo_edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, {'form': form})


def tracker_edit(request, pk):
    tracker = Tracker.objects.get(pk=pk)
    if request.method == "POST":
        form = TrackerForm(request.POST, instance=tracker)
        if form.is_valid():
            tracker = form.save()
            return redirect('tracker_detail', pk=tracker.pk)
    else:
        form = TrackerForm(instance=tracker)
    return render(request, {'form': form})


def play_delete(request, pk):
    Play.objects.get(id=pk).delete()
    return redirect('play_list')


def character_delete(request, pk):
    Character.objects.get(id=pk).delete()
    return redirect('character_list')


def todo_delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect('todo_list')


def tracker_delete(request, pk):
    Tracker.objects.get(id=pk).delete()
    return redirect('tracker_list')