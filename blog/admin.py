from django.contrib import admin
from blog.models import BlogPost
# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    # list_display = ['name' , 'email' , 'message']
    date_hierarchy = 'updated_date'
    list_display = ['title','status' , 'counted_view' , 'published_date']
    empty_value_display = '-empty-'
    search_fields = ["title" , "content"]
    list_filter = ['status']
    ordering = ['-create_date']

    
