from django.contrib import admin
from index.models import Contact , NewsLetter


# Register your models here.


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):


    date_hierarchy = 'updated_date'
    list_display = ['name' ,'subject' , 'email' , 'created_date']
    empty_value_display = '-empty-'
    search_fields = ["name" , "subject"]
    list_filter = ['email']
    ordering = ['-created_date']
    
@admin.register(NewsLetter)
class NewsLetterModelAdmin(admin.ModelAdmin):
    list_display = ['email']
    

# Apply summernote to all TextField in model.
