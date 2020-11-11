from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import ImageInServer
from django.shortcuts import redirect


@api_view(['GET'])
@permission_classes([AllowAny])
def get_image_view(request: Request, image_name: str):
    image = ImageInServer.objects.filter(name=image_name).first()
    if not image:
        return Response("Not found", status=404)
    return redirect(image.get_redirect_url())


