from rest_framework import serializers
from .models import UserInfo, User, VkUser, UserInterest, UserPosition


class UserInfoUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ['first_name', 'second_name', 'avatar']


class UserInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInterest
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):

    user_url = serializers.URLField(source='vkuser.get_user_profile_url')
    first_name = serializers.CharField(source='userinfo.first_name')
    second_name = serializers.CharField(source='userinfo.second_name')
    avatar = serializers.URLField(source='userinfo.avatar')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'second_name', 'avatar', 'user_url', 'avatar']


class FullUserSerializer(serializers.ModelSerializer):
    user_url = serializers.URLField(source='vkuser.get_user_profile_url')
    first_name = serializers.CharField(source='userinfo.first_name')
    second_name = serializers.CharField(source='userinfo.second_name')
    interests = UserInterestSerializer(many=True, source='userinfo.interests')
    avatar = serializers.URLField(source='userinfo.avatar')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'second_name', 'avatar', 'user_url', 'interests', 'avatar']


class UserPositionSerializer(serializers.ModelSerializer):

    user_url = serializers.URLField(source='user.vkuser.get_user_profile_url')
    first_name = serializers.CharField(source='user.userinfo.first_name')
    second_name = serializers.CharField(source='user.userinfo.second_name')
    interests = UserInterestSerializer(many=True, source='user.userinfo.interests')
    avatar = serializers.URLField(source='user.userinfo.avatar')

    class Meta:
        model = UserPosition
        fields = ['first_name', 'second_name', 'avatar', 'user_url', 'interests', 'avatar', 'latitude', 'longitude']
