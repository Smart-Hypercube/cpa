from django.db.models import (
    Model,
    TextField,
)


class Message(Model):
    user = TextField(unique=True)
    body = TextField(default='')

    def __str__(self):
        return "{0.user}'s".format(self)
