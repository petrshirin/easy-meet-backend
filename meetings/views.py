from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from .services import get_list_meetings, get_meeting_per_id, user_to_meeting, create_new_meeting, edit_meeting


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_list_meetings_view(request: Request) -> Response:
    response = get_list_meetings(request)
    return Response(response, status=200)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_meeting_view(request: Request, meeting_id: int) -> Response:
    response = get_meeting_per_id(meeting_id, request.user)
    if response.get('errors'):
        return Response(response, status=401)
    return Response(response, status=200)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def meeting_action_view(request: Request, meeting_id: int) -> Response:
    response = user_to_meeting(meeting_id, request.user, request.data.get('action', 'subscribe'))
    if response.get('errors'):
        return Response(response, status=401)
    return Response(response, status=201)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_meeting_view(request: Request) -> Response:
    response = create_new_meeting(request.user, request.data)
    if response.get('errors'):
        return Response(response, status=401)
    return Response(response, status=201)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_meeting_view(request: Request, meeting_id: int) -> Response:
    response = edit_meeting(request.user, request.data, meeting_id)
    if response.get('errors'):
        return Response(response, status=401)
    return Response(response, status=201)



