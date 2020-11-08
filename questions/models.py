from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Question(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=512)
    part = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=now)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=512)
    date_commented = models.DateTimeField(default=now)
    deleted = models.BooleanField(default=False)


class AnswerMark(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField(default=0)



