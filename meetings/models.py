from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Meeting(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    date = models.DateField(default=now)
    time = models.TimeField(default=now)
    place = models.CharField(max_length=512)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=None, null=True, blank=True)
    max_participant = models.PositiveIntegerField(default=None, null=True, blank=True)
    comment = models.TextField()
    invite_url = models.URLField(blank=True, null=True, default=None)
    members = models.ManyToManyField(User, related_name='members', blank=True)



