from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

from .models import *
from .serializer import *

class NewsAPIView(APIView):

    def get(self, request):
        ns = News.objects.all()
        return Response({'news_serializer': NewsSerializer(ns, many=True).data})
    
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'news': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        
        try:
            news = News.objects.get(pk=pk)
        except:
            return Response({"error": "News does not exists"})
        
        serializer = NewsSerializer(data=request.data, instance=news)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'news': serializer.data})
    

    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})
        
        try:
            news = News.objects.get(pk=pk)
        except:
            return Response({"error": "News does not exists"})

        news.delete()
        return Response({'delete': 'Запись успешно удалена'})


# class NewsAPIView(ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
