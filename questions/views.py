from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from .services import get_questions, get_question_per_id, create_question, \
    create_answer, do_mark


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_questions_view(request: Request):
    response = get_questions(request.query_params.get('part', None))
    return Response(response, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_question_per_id_view(request: Request, question_id: int):
    response = get_question_per_id(request.user, question_id)
    if response.get('errors'):
        return Response(response, status=402)
    return Response(response, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_question_view(request: Request):
    response = create_question(request.user, request.data)
    if response.get('errors'):
        return Response(response, status=422)
    return Response(response, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_answer_view(request: Request, question_id: int):
    response = create_answer(question_id, request.user, request.data)
    if response.get('errors'):
        return Response(response, status=422)
    return Response(response, status=200)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def do_mark_to_answer_view(request: Request, answer_id: int):
    response = do_mark(answer_id, request.user, request.data)
    if response.get('errors'):
        return Response(response, status=422)
    return Response(response, status=200)


