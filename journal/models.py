from django.db import models


class ReceivedEmail(models.Model):
    email_address = models.CharField(max_length=30)
    email = models.TextField(max_length=3000)
