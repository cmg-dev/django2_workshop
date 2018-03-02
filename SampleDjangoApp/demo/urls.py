from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alternative/', views.index_alternative, name='index'),
    path('solve/', views.solve, name='solver'),
    path('solution/', views.solution, name='solution'),
    path('<str:greeting>/', views.test_with_argument),
]
