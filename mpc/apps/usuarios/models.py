from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetail(models.Model):
    id_user_detail = models.AutoField(primary_key=True)
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()