from datetime import timedelta
import datetime

from django.http import HttpResponse
from post_office import mail

from journal.models import ReceivedEmail


def index(request):
    return HttpResponse(
        mail.send(
            'oatman@localhost',  # List of email addresses also accepted
            'from@example.com',
            subject='My email',
            scheduled_time=datetime.datetime.now() + timedelta(seconds=1),
            message='Hi there!',
            html_message='Hi <strong>there</strong>!',
        )
    )


def receive_email(request):
    ReceivedEmail(
        email_address=request.POST.get("from"),
        email=request.POST.get("text")
    ).save()
    return HttpResponse(request)
