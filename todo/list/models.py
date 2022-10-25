from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class todo(models.Model):
    Title=models.CharField(max_length=100)
    Note=models.TextField()
    Save_Date=models.DateTimeField(auto_now_add=True)
    Last_Date=models.DateTimeField()
    Status=models.BooleanField()
    Count=models.IntegerField(default=0)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
