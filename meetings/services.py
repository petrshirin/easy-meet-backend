from .models import User, Meeting
from typing import Dict, List
from rest_framework.request import Request
from django.utils.timezone import now
from .serializers import MeetingCardSerializer, MeetingSerializer, MeetingPostSerializer


def get_list_meetings(request: Request):
    if request.query_params.get('type') == "0":
        meetings = Meeting.objects.all()
    elif request.query_params.get('type') == "1":
        meetings = Meeting.objects.filter(date__gt=now()).all()
    elif request.query_params.get('type') == "2":
        meetings = Meeting.objects.filter(creator=request.user).all()
    elif request.query_params.get('type') == "3":
        meetings = Meeting.objects.filter(date__lt=now()).all()
    else:
        meetings = []
    meetings_ser = MeetingCardSerializer(meetings, many=True)
    return {'success': True, 'data': meetings_ser.data}


def get_meeting_per_id(meeting_id: int, user: User = None) -> Dict:
    meeting = Meeting.objects.filter(pk=meeting_id).first()
    if not meeting:
        return {'success': False, 'errors': "meeting not found"}
    return {'success': True, 'data': {"meeting": MeetingSerializer(meeting).data, 'self': meeting.creator == user, "is_member": user in meeting.members.all()}}


def user_to_meeting(meeting_id: int, user: User, action: str = 'subscribe') -> Dict:
    meeting = Meeting.objects.filter(pk=meeting_id).first()
    if not meeting:
        return {'success': False, 'errors': "meeting not found"}
    if action == 'subscribe':
        meeting.members.add(user)
    else:
        meeting.members.remove(user)
    return {'success': True, 'data': "ok"}


def create_new_meeting(user: User, data: Dict) -> Dict:
    meeting_ser = MeetingPostSerializer(data=data)
    if meeting_ser.is_valid():
        meeting = Meeting.objects.create(**meeting_ser.validated_data, creator=user)
        meeting.members.add(user)
        meeting.save()
        return {'success': True, 'data': {"meeting": MeetingSerializer(meeting).data, 'self': meeting.creator == user}}
    else:
        return {'success': False, 'errors': meeting_ser.errors}


def edit_meeting(user: User, data: Dict, meeting_id: int) -> Dict:
    meeting_ser = MeetingPostSerializer(data=data)
    if meeting_ser.is_valid():
        meeting = Meeting.objects.filter(pk=meeting_id).first()
        if not meeting:
            return {'success': False, 'errors': "meeting not found"}
        meeting_ser.update(meeting, validated_data=meeting_ser.validated_data)
        return {'success': True, 'data': {"meeting": MeetingSerializer(meeting).data, 'self': meeting.creator == user}}
    else:
        return {'success': False, 'errors': meeting_ser.errors}


