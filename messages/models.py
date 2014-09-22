import json
import requests

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from .encoders import MyEncoder


class Message(models.Model):
    sent_by = models.ForeignKey(User)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


def send_notification(sender, **kwargs):
    m = kwargs['instance']
    data = {
        "sent_by": m.sent_by.email,
        "content": m.content,
        "created_at": m.created_at
    }
    response =\
        requests.post(
            url=settings.WEBHOOK_URL,
            data=json.dumps(data, cls=MyEncoder),
            headers={'content-type': 'application/json'}
        )

post_save.connect(send_notification, sender=Message)
