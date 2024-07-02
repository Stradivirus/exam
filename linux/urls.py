from django.urls import path
from . import views

urlpatterns = [
    path('', views.pdf_list, name='pdf_list'),
    path('view/<str:filename>/', views.view_pdf, name='view_pdf'),
    path('view/<str:filename>/result.html', views.result, name='result'),
]
