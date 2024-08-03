from django import template
from blog.models import BlogPost
register = template.Library()

@register.simple_tag
def posts( ):
    posts = BlogPost.objects.filter(status=1)
    return posts