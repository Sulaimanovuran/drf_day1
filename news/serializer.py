from rest_framework import serializers
from .models import *
from rest_framework.renderers import JSONRenderer



class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    is_publshed = serializers.BooleanField(default=True)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return News.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.is_publshed = validated_data.get('is_publshed', instance.is_publshed)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.save()
        return instance
        
        
        















# def encode():
#     model = NewsModel('Олимпийские игры', "Новость об играх")
#     model_sr = NewsSerializer(model)

#     print(model_sr.data)

#     json = JSONRenderer().render(model_sr.data)
#     print(json)














# class NewsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = News
#         fields = ['title', 'cat_id']