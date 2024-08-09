from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return "{} - {}".format(self.name , self.subject)


class NewsLetter(models.Model):
    email = models.EmailField(max_length=254)
    
    
    def __str__(self) -> str:
        return "{}".format(self.email )
