from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
  path('plays/', views.PlayList.as_view(), name='play_list'),
  path('plays/<int:pk>', views.PlayDetail.as_view(), name='play_detail'),

  path('characters/', views.CharacterList.as_view(), name='character_list'),
  path('characters/<int:pk>', views.CharacterDetail.as_view(), name='character_detail'),

  path('todos/', views.TodoList.as_view(), name='todo_list'),
  path('todos/<int:pk>', views.TodoDetail.as_view(), name='todo_detail'),
  
  path('trackers/', views.TrackerList.as_view(), name='tracker_list'),
  path('trackers/<int:pk>', views.TrackerDetail.as_view(), name='tracker_detail'),

]