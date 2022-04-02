from django.db import models
import uuid
from userdetail.models import Profile


class CanteenInfo(models.Model):
    profile_id = models.OneToOneField(Profile, on_delete=models.CASCADE, null =True, blank=True)
    canteen_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True,)
    active_or_not = models.BooleanField()
    last_scan_date_and_time = models.DateTimeField(auto_now_add=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        a = self.last_scan_date_and_time
        b = self.end_time
        return str(f'{a} {b}')
