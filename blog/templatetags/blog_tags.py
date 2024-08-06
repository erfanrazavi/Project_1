from django import template
from blog.models import BlogPost , Category
register = template.Library()

@register.simple_tag
def posts( ):
    posts = BlogPost.objects.filter(status=1)
    return posts

@register.simple_tag 
def upper(value):
    return value.lower()

@register.inclusion_tag('popular-post.html')
def popularPost(arg):
    posts = BlogPost.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts' : posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def categories():
    posts = BlogPost.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    
    
    for name in categories:
        
        
        cat_dict[name] = posts.filter(category=name).count()
       
    return {'categories':cat_dict}
    