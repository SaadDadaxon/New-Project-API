from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .permission import IsOwnerOrReadOnly
from ..models import Article, Category, Comment, Tag, SubContent, SubContentImage
from .serializers import ArticleGETSerializers, ArticlePOSTSerializers, CommentSerializers, CategorySerializer, \
    TagSerializers, SubContentSerializers, SubContentImageSerializers, MineSubContentSerializers


class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListAPI(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class ArticleListCreateApi(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGETSerializers
        return ArticlePOSTSerializers


class ArticleRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGETSerializers
        return ArticlePOSTSerializers


class SubContentListCreateAPI(generics.ListCreateAPIView):
    queryset = SubContent.objects.all()
    serializer_class = SubContentSerializers

    def get_queryset(self, *args, **kwargs):
        sb = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            sb = sb.filter(article_id=article_id)
            return sb
        return []

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MineSubContentSerializers
        return SubContentSerializers

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx


class SubImageListCreateAPI(generics.ListCreateAPIView):
    queryset = SubContentImage.objects.all()
    serializer_class = SubContentImageSerializers


class CommentListCreateAPI(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            qs = qs.filter(article_id=article_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx



