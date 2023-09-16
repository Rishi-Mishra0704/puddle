from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.details, name='detail'),
    path('new/', views.new_item, name='new'),
]