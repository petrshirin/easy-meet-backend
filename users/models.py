from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)

    @staticmethod
    def get_first_city():
        return City.objects.first()


class VkUser(models.Model):
    vk_user_id = models.IntegerField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_user_profile_url(self):
        return f"https://vk.com/id{self.vk_user_id}"


class UserInterest(models.Model):
    name = models.CharField(max_length=60)


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default=None, null=True)
    second_name = models.CharField(max_length=255, default=None, null=True)
    avatar = models.URLField(null=True, default=True, max_length=1024)
    interests = models.ManyToManyField(UserInterest)


class UserPosition(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_DEFAULT, default=City.get_first_city)
    latitude = models.DecimalField(max_digits=20, decimal_places=12, default=None, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=12, default=None, null=True)






