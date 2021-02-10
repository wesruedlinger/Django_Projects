from django.urls import path
from . import views
from .feeds import LatestPostFeed
from .views import (PostCreateView,
                    PostUpdateView,
                    PostDeleteView, 
                    PostListView,
                    UserPostListView)

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.common_tags, name='post_list_by_tag'),
    path('feed/', LatestPostFeed(), name='post_feed'),
    path('search/', views.post_search, name='post-search'),

]