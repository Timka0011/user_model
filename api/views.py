from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArticleSerializer
from article.models import Article
from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from article.models import Article
from rest_framework.response import Response
from rest_framework import status

from .authentication import TokenAuthentication
# from .permissions import StaffUserPermessions

class AticleView(APIView):

    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    def get(self, request, pk=None):
        if pk:
            article = self.get_object(pk=pk)
            serializer = ArticleSerializer(article, many=False)
            return Response(serializer.data, status=200)
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data, status=204)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleView(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        print(serializer.validated_data)
        print(serializer.validated_data['title'])
        return super().perform_create(serializer)


class ArticleUpdateView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        return super().perform_update(serializer)

    