from rest_framework import serializers
from .models import Meeting
from users.serializers import UserSerializer


class MeetingSerializer(serializers.ModelSerializer):

    date = serializers.DateField(format='%d.%m.%Y')
    time = serializers.TimeField(format="%H:%M")
    creator = UserSerializer()

    class Meta:
        model = Meeting
        fields = ['id', 'name', 'date', 'time', 'creator', 'place', 'price', 'max_participant', 'comment', 'invite_url']


class MeetingPostSerializer(serializers.ModelSerializer):

    date = serializers.DateField(format='%Y-%m-%d', input_formats=['%Y-%m-%d'])
    time = serializers.TimeField(format="%H:%M", input_formats=["%H:%M"])

    class Meta:
        model = Meeting
        fields = ['name', 'date', 'time', 'place', 'max_participant', 'comment', 'invite_url']


class MeetingCardSerializer(serializers.ModelSerializer):

    date = serializers.DateField(format='%d.%m.%Y')
    time = serializers.TimeField(format="%H:%M")

    members = UserSerializer(many=True)

    class Meta:
        model = Meeting
        fields = ['id', 'name', 'date', 'time', 'members']




