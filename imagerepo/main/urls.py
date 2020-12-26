from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_images, name='gallery'),
    path('add/', views.add_image, name='add'),
    path('images/<int:image_id>/', views.edit_image, name='edit'),
    path('delete/<int:image_id>/', views.delete_image, name='delete'),
]