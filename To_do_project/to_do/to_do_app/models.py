from django.db import models


# Create your models here.


class Register(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)  # Assuming passwords can be strings
    confirm_password = models.CharField(max_length=255)  # Assuming passwords can be strings

    def __str__(self):
        return self.username


class Task(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
