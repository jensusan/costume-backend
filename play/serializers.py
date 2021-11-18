from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Play, Tracker, Character, Todo

class PlaySerializer(serializers.HyperlinkedModelSerializer):
    trackers = serializers.HyperlinkedRelatedField(view_name='tracker_detail',
    many=True, read_only=True)

    characters = serializers.HyperlinkedRelatedField(view_name='character_detail',
    many=True, read_only=True)

    todos = serializers.HyperlinkedRelatedField(view_name='todo_detail',
    many=True, read_only=True)
    
    play_url = serializers.ModelSerializer.serializer_url_field(view_name='play_detail')
    
    class Meta:
        model= Play
        fields = ('id', 'title', 'author', 'reference_img', 'concept', 'director_notes', 'play_url', 'trackers', 'characters', 'todos')


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    play = serializers.HyperlinkedRelatedField(view_name='play_detail', read_only=True)

    play_id = serializers.PrimaryKeyRelatedField(queryset=Play.objects.all(), source='play')

    class Meta:
        model=Character
        fields=('id', 'name', 'actor', 'sketches', 'reference_img', 'notes', 'play', 'play_id')


class TrackerSerializer(serializers.HyperlinkedModelSerializer):
    play = serializers.HyperlinkedRelatedField(view_name='play_detail', read_only=True)

    play_id = serializers.PrimaryKeyRelatedField(queryset=Play.objects.all(), source='play')

    class Meta:
        model=Tracker
        fields=('id', 'scene', 'character', 'change', 'notes', 'play', 'play_id')


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    play = serializers.HyperlinkedRelatedField(view_name='play_detail', read_only=True)

    play_id = serializers.PrimaryKeyRelatedField(queryset=Play.objects.all(), source='play')

    class Meta:
        model=Todo
        fields=('id', 'task', 'completed', 'play', 'play_id')

