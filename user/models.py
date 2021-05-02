from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    displayname=models.CharField(max_length=50,null=True)
    number=models.CharField(max_length=15)
    address=models.TextField()
    bio=models.TextField()

    REQUIRED_FIELDS=['email']

    class Meta:
        verbose_name="Customuser"
        verbose_name_plural="Customusers"

    def __str__(self):
        return self.username
#intended for the unique id but may not be used idk
    # def save(self,*args, **kwargs):
    #     self.username="user"+ str(self.id)
    #     super().save(*args,**kwargs)