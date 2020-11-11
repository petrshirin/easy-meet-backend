from django.db import models

# Create your models here.


class Server(models.Model):
    name = models.CharField(max_length=255)
    host = models.URLField(max_length=512)


class ImageInServer(models.Model):
    name = models.CharField(max_length=255)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def get_redirect_url(self):
        return f"{self.server.host}/media/img/{self.name}"

