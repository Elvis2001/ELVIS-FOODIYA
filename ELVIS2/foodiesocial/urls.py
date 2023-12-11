from django.urls import path
from foodiesocial.views import PostListView

urlpatterns = [
    path('', PostListView, name='post-list')
]