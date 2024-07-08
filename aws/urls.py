from django.urls import path
from . import views

urlpatterns = [
    # ... 다른 URL 패턴들 ...
    path('quiz/', views.aws_quiz, name='aws_quiz'),
    path('result/', views.aws_result_view, name='aws_result_view'),
]