from django.db import models

# Create your models here.
# class Register(models.Model):
#     fullName = models.CharField(max_length=50)
#     username = models.CharField(max_length=255, blank=True)
#     email = models.EmailField()
#     phoneNumber = models.IntegerField()
#     password = models.CharField(widget=models.PasswordInput)
#     confirmPassword = models.CharField(widget=models.PasswordInput)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
    
    
#     def __str__(self) -> str:
#         return "{} - {}".format(self.name , self.subject)