from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.

class TicketCard (models.Model):
  status = models.IntegerField(default=1)
  post_person = models.CharField("PostPerson", max_length=20, default="John Due")
  content = models.TextField("Contents") 
  created = models.DateTimeField("Date", default=timezone.now)

  def __str__(self):
    return self.status