from django.db import models
import uuid
from datetime import datetime
from nextmotion import settings


class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    created_time = models.DateTimeField(default=datetime.now, db_index=True)
    email = models.EmailField()
    used = models.BooleanField(default=False)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='created_invitations',
        on_delete=models.CASCADE, null=True, blank=True)