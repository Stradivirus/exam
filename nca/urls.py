from django.urls import path
from . import views

urlpatterns = [
    # ... 다른 URL 패턴들 ...
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result_view, name='result_view'),
    path('', views.quiz, name='quiz'),
]

