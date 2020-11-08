from django.contrib import admin
from .models import AnswerMark, Answer, Question

# Register your models here.
admin.site.register(Answer)
admin.site.register(AnswerMark)
admin.site.register(Question)
