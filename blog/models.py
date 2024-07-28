from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    
class BlogPost(models.Model):
    title =  models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    category = models.ManyToManyField(Category)
    image_filed = models.ImageField(upload_to='blog/' , default='/blog/feature-img1.jpg')
    counted_view = models.IntegerField(default=0)  #(default=0)
    status = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    
    
    def __str__(self) -> str:
        return " {} - {}".format(self.title , self.id)
    
    
    class Meta:
        db_table_comment = "Question answers"
        
    
        
