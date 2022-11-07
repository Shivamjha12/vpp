from django.db import models
# Create your models here.

class login_det(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date_time