from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import BlogPost


class LatestEntriesFeed(Feed):
    title = "blog newest post"
    link = "/rss/feed"
    description = "best blog over"

    def items(self):
        return BlogPost.objects.filter(status=1)
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]
