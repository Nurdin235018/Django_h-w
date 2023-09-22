from django.urls import path
from .views import CategoryDetailView, CategoryListCreateView, TagListCreateView, TagDetailView, PostListCreateView, PostDetailView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
    path('tags/', TagListCreateView.as_view()),
    path('tags/<int:pk>/', TagDetailView.as_view()),
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view())
]
