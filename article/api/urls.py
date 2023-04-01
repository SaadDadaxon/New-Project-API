from django.urls import path
from .views import CategoryListAPI, TagListAPI, ArticleListCreateApi, ArticleRUDAPI, CommentListCreateAPI, \
    SubContentListCreateAPI, SubImageListCreateAPI

urlpatterns = [
    path('list-category/', CategoryListAPI.as_view()),
    path('list-tag/', TagListAPI.as_view()),
    path('list-article/', ArticleListCreateApi.as_view()),
    path('rud-article/<int:pk>/', ArticleRUDAPI.as_view()),
    path('article/<int:article_id>/comment-list-create/', CommentListCreateAPI.as_view()),
    path('article/<int:article_id>/content-list-create/', SubContentListCreateAPI.as_view()),
    path('article/<int:article_id>/content-list-create/image/', SubImageListCreateAPI.as_view()),
]
