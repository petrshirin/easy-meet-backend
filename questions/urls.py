from django.urls import path
from .views import do_mark_to_answer_view, get_question_per_id_view, \
    create_answer_view, create_question_view, get_questions_view

urlpatterns = [
    path('', get_questions_view),
    path('<int:question_id>', get_question_per_id_view),
    path('<int:question_id>/answer/create', create_answer_view),
    path('create', create_question_view),
    path('answer/<int:answer_id>/mark', do_mark_to_answer_view),
]
