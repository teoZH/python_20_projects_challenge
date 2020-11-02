from django.urls import path

from recipes_app import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/',views.create, name='create'),
    path('edit/<int:rec_id>',views.edit, name='edit'),
    path('delete/<int:rec_id>',views.delete, name='delete'),
    path('details/<int:rec_id>',views.details, name= 'details')
]
