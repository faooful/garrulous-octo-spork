from datetime import timedelta
import datetime

from django.http import HttpResponse
from django.core.mail import send_mail
from post_office import mail


def index(request):
    return HttpResponse(
        mail.send(
            'oatman@localhost',  # List of email addresses also accepted
            'from@example.com',
            subject='My email',
            scheduled_time=datetime.datetime.now() + timedelta(seconds=10),
            message='Hi there!',
            html_message='Hi <strong>there</strong>!',
        )
    )
