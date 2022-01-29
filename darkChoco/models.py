from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class Letter(models.Model):
    letter_text = models.TextField(max_length=200)
    to_user = models.ForeignKey(User, on_delete = models.CASCADE)
    from_user = models.CharField(max_length=10)
    send_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.letter_text
