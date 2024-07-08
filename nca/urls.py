from django.urls import path
from . import views

urlpatterns = [
    # ... 다른 URL 패턴들 ...
    path('quiz/', views.nca_quiz, name='nca_quiz'),
    path('result/', views.nca_result_view, name='nca_result_view'),
]