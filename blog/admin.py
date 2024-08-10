from django.contrib import admin
from blog.models import BlogPost
from blog.models import Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    # list_display = ['name' , 'email' , 'message']
    date_hierarchy = 'updated_date'
    list_display = ['title' , 'author','status' , 'counted_view' , 'published_date']
    empty_value_display = '-empty-'
    search_fields = ["title" , "content"]
    list_filter = ['status']
    ordering = ['-create_date']
    summernote_fields = ('content',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
        pass
        


    
