from .models import User, VkUser, UserPosition, City, UserInfo, UserInterest
from typing import Dict, List
from .validate_vk_mini_apps import validate_request
from random import choice
import string
from rest_framework.authtoken.models import Token
from .serializers import UserInfoUpdateSerializer, UserPositionSerializer
from rest_framework.request import Request
from .serializers import FullUserSerializer
from questions.models import AnswerMark
from django.db.models import Avg
from django.db.models.query import Q


def register_user(data: Dict):
    user = User.objects.create(username=data.get('vk_user_id'), password=_get_random_str())
    vk_user = VkUser.objects.create(user=user, vk_user_id=data.get('vk_user_id'))
    user_position = UserPosition.objects.create(user=user)
    UserInfo.objects.create(user=user)
    token = Token.objects.create(user=user)
    return {"success": True, "data": {"token": token.key, "new": True}}


def auth_or_register(request: Request):
    data = validate_request(request.data.get('url'))
    if not data:
        return {"errors": "Bad request", "success": False}

    print(data.get('vk_user_id'))
    vk_user = VkUser.objects.filter(vk_user_id=data.get('vk_user_id')).first()
    if not vk_user:
        return register_user(data)
    else:
        token = Token.objects.filter(user=vk_user.user).first()
        return {'success': True, "data": {"token": token.key}}


def _get_random_str():
    return "".join(choice(string.ascii_letters) for i in range(16))


def get_user_position(user: User, data: Dict):
    user_position = UserPosition.objects.filter(user=user).first()
    user_position.latitude = data.get('latitude', user_position.latitude)
    user_position.longitude = data.get('longitude', user_position.longitude)
    user_position.save()
    user_data = dict(UserPositionSerializer(user_position).data)
    user_data['score'] = AnswerMark.objects.filter(answer__commentator=user_data.get('id')).all().aggregate(Avg('mark'))['mark__avg']
    return {"success": True, "data": user_data}


def update_user_info(user: User, data: Dict) -> Dict:
    ser = UserInfoUpdateSerializer(data=data)
    if ser.is_valid():
        user_info = UserInfo.objects.filter(user=user).first()
        ser.update(user_info, ser.validated_data)

        user_data = dict(FullUserSerializer(user).data)
        user_data['score'] = AnswerMark.objects.filter(answer__commentator=user).all().aggregate(Avg('mark'))['mark__avg']
        return {"success": True, 'data': user_data}
    else:
        return {"success": False, 'errors': ser.errors}


def update_interests(user: User, data: Dict) -> Dict:
    if data.get('interests') and isinstance(data.get('interests'), list):
        user.userinfo.interests.clear()
        for item_id in data.get('interests'):
            interest = UserInterest.objects.filter(pk=item_id).first()
            print(interest)
            if interest:
                user.userinfo.interests.add(interest)

        user.userinfo.save()
        return {"success": True, "data": "ok"}
    return {'success': False, "errors": "invalid format"}


def get_users_geo(user: User) -> Dict:
    user_positions = UserPosition.objects.filter(~Q(latitude=None, longitude=None)).exclude(user=user).all()
    user_positions_ser = UserPositionSerializer(user_positions, many=True)
    positions_with_score = []
    for item in list(user_positions_ser.data):
        user_data = dict(item)
        user_data['score'] = AnswerMark.objects.filter(answer__commentator=user_data.get('id')).all().aggregate(Avg('mark'))['mark__avg']
        positions_with_score.append(user_data)
    return {"success": True, "data": positions_with_score}

