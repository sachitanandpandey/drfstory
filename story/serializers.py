from rest_framework import serializers
from .models import Story, Chapter


class ChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chapter
        fields = ['id', 'title']


class ChapterlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'



class StorySerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(many=True,  read_only=True)

    class Meta:
        model = Story
        fields = '__all__'




