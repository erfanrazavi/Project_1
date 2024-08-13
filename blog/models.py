from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

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
    login_require = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    tags = TaggableManager()
    
    
    def __str__(self) -> str:
        return " {} - {}".format(self.title , self.id)
    
    def get_absolute_url(self):
        return reverse('blog:blog-single', kwargs={'pid':self.id})

    class Meta:
        db_table_comment = "Question answers"
        
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['-create_date']
    def __str__(self):
        return " {}".format(self.subject)
    
        
