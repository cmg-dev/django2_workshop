from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:greeting>/', views.test_with_argument),
]
