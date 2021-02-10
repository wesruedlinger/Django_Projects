from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class LatestPostFeed(Feed):
    title = 'Tech Weasel Blog'
    link = '/blogApp/'
    description = 'New posts of Tech Weasel blog.'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return truncatewords(item.body, 30)