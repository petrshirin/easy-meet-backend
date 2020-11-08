from rest_framework import serializers
from .models import Question, Answer, AnswerMark
from users.serializers import UserSerializer


class AnswerMarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerMark
        fields = ['mark']


class AnswerSerializer(serializers.ModelSerializer):
    date_commented = serializers.DateTimeField(format='%d.%m.%Y %H:%M')
    commentator = UserSerializer()

    class Meta:
        model = Answer
        fields = ['id', 'commentator', 'comment', 'date_commented']


class QuestionSerializer(serializers.ModelSerializer):

    date_created = serializers.DateTimeField(format='%d.%m.%Y %H:%M')
    answers = AnswerSerializer(many=True, source='answer_set')
    creator = UserSerializer()

    class Meta:
        model = Question
        fields = ['id', 'creator', 'text', 'part', 'date_created', 'answers']


class QuestionPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['text', 'part']


class AnswerPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['comment']


class AnswerMarkPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerMark
        fields = ['mark']





