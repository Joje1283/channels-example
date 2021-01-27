from chat import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<room_name>/', views.room, name='room'),
]