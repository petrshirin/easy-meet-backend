from .models import User, Question, Answer, AnswerMark
from typing import Dict, List
from random import choice
import string
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from .serializers import QuestionSerializer, AnswerSerializer, AnswerMarkPostSerializer, \
    AnswerMarkSerializer, QuestionPostSerializer, AnswerPostSerializer


def get_questions(part: str = None) -> Dict:
    if part:
        questions = Question.objects.filter(deleted=False, part=part)
    else:
        questions = Question.objects.filter(deleted=False)
    questions = questions.order_by('-date_created').all()
    questions_ser = QuestionSerializer(questions, many=True)
    return {'success': True, 'data': questions_ser.data}


def get_question_per_id(user: User, question_id: int) -> Dict:
    question = Question.objects.filter(deleted=False, pk=question_id).first()
    if not question:
        return {'success': False, 'errors': "question not found"}
    questions_ser = QuestionSerializer(question)
    data_ser = dict(questions_ser.data)
    for answer in data_ser['answers']:
        mark = AnswerMark.objects.filter(answer_id=answer['id'], user=user).first()
        if mark:
            answer['mark'] = mark.mark
    return {'success': True, 'data': data_ser}


def create_question(user: User, data: Dict) -> Dict:
    question_ser = QuestionPostSerializer(data=data)
    if question_ser.is_valid():
        Question.objects.create(**question_ser.validated_data, creator=user)

        return {'success': True, 'data': 'ok'}
    return {'success': False, 'errors': question_ser.errors}


def create_answer(question_id, user: User, data: Dict) -> Dict:
    question = Question.objects.filter(pk=question_id, deleted=False).first()
    if not question:
        return {'success': False, 'errors': "question not found"}
    answer_ser = AnswerPostSerializer(data=data)
    if answer_ser.is_valid():
        Answer.objects.create(**answer_ser.validated_data, commentator=user, question=question)
        return {'success': True, 'data': 'ok'}
    return {'success': False, 'errors': answer_ser.errors}


def do_mark(answer_id: int, user: User, data: dict) -> Dict:
    answer = Answer.objects.filter(pk=answer_id, deleted=False).first()
    if not answer:
        return {'success': False, 'errors': "answer not found"}
    answer_mark_ser = AnswerMarkPostSerializer(data=data)

    if answer_mark_ser.is_valid():
        AnswerMark.objects.create(answer=answer, **answer_mark_ser.validated_data, user=user)
        return {'success': True, 'data': 'ok'}
    return {'success': False, 'errors': answer_mark_ser.errors}




