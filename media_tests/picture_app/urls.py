from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/', views.create, name='create'),
    path('delete/<int:car_id>', views.delete, name='delete'),
    path('details/<int:car_id>', views.details, name='details')
]
