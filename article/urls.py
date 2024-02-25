from django.urls import path
from .views import ArticleDetailView, AricleListView, CreateArticleView, UpdateArticleView, DeleteArticleView

urlpatterns = [
    path("", AricleListView.as_view(), name='home'),
    path("article/", CreateArticleView.as_view(), name='create'),
    path("<int:pk>/update", UpdateArticleView.as_view(), name='update'),
    path("<int:pk>/delete", DeleteArticleView.as_view(), name='delete'),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name='detail'),
]