from django.urls import path
from . import views

urlpatterns = [
    path('', views.play_list, name='play_list'),
    path('characters/', views.character_list, name ='character_list'),
    path('todos/', views.todo_list, name ='todo_list'),
    path('trackers/', views.tracker_list, name ='tracker_list'),
    path('plays/<int:pk>/', views.play_detail, name = 'play_detail'),
    path('characters/<int:pk>/', views.character_detail, name = 'character_detail'),
    path('todos/<int:pk>/', views.todo_detail, name = 'todo_detail'),
    path('trackers/<int:pk>/', views.tracker_detail, name = 'tracker_detail'),
    path('plays/new', views.play_create, name='play_create'),
    path('characters/new', views.character_create, name='character_create'),
    path('todos/new', views.todo_create, name='todo_create'),
    path('trackers/new', views.tracker_create, name='tracker_create'),
]