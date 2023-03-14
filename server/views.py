from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics


class QuizListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class ResultListView(generics.ListAPIView):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()


class ResultCreateView(generics.CreateAPIView):
    serializer_class = ResultSerializer
