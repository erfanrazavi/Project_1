from django.contrib.sitemaps import Sitemap
from blog.models import BlogPost
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return BlogPost.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date
    
   
    