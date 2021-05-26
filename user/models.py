from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#should add a usernamefield soon
class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    displayname=models.CharField(max_length=50,null=True)
    number=models.CharField(max_length=15)
    address=models.TextField()
    bio=models.TextField(null=True)

    REQUIRED_FIELDS=[]

    class Meta:
        verbose_name="Customuser"
        verbose_name_plural="Customusers"



    def __str__(self):
        return self.email
        
#The username is also email 
    def save(self,*args, **kwargs):
        if not self.username:
            self.username=self.email
        super().save(*args,**kwargs)
                