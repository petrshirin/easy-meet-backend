from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from .services import auth_or_register, get_user_position, \
    update_user_info, update_interests, get_users_geo


@api_view(['POST'])
@permission_classes([AllowAny])
def authorize_user_view(request: Request) -> Response:
    response = auth_or_register(request)
    if response.get('errors'):
        return Response(response, status=422)
    else:
        return Response(response, status=201)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_user_position_view(request: Request) -> Response:
    response = get_user_position(request.user, request.data)
    return Response(response, status=201)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_user_info_view(request: Request) -> Response:
    response = update_user_info(request.user, request.data)
    if response.get('errors'):
        return Response(response, status=422)
    else:
        return Response(response, status=201)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_interests_view(request: Request) -> Response:
    response = update_interests(request.user, request.data)
    if response.get('errors'):
        return Response(response, status=422)
    else:
        return Response(response, status=201)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_interests_view(request: Request) -> Response:
    response = update_interests(request.user, request.data)
    if response.get('errors'):
        return Response(response, status=422)
    else:
        return Response(response, status=200)

