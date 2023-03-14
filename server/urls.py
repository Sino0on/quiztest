from django.urls import path
from .views import *


urlpatterns = [
    path('quiz/list/', QuizListView().as_view()),
    path('result/list/', ResultListView().as_view()),
    path('result/create/', ResultCreateView().as_view()),
]