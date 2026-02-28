from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostDrraftListView
)

urlpatterns = [
    path("list/", PostListView.as_view(), name="post_list"),    
    path("drafts/", PostDrraftListView.as_view(), name="post_drafts"),    
    path("new/", PostCreateView.as_view(), name="post_new"),    
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),    
    path("<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]