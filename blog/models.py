from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title =  models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    # author = models.IntegerField()
    # category = models.IntegerField()
    counted_view = models.IntegerField(default=0)  #(default=0)
    status = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    
    
    def __str__(self) -> str:
        return " {} - {}".format(self.title , self.id)
    class Meta:
        db_table_comment = "Question answers"