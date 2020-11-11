from django.urls import path
from .views import get_image_view

urlpatterns = [
    path("<str:image_name>", get_image_view)
]
