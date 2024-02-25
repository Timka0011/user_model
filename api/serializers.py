from rest_framework.serializers import ModelSerializer
from article.models import Article
from accounts.models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "number"]


class ArticleSerializer(ModelSerializer):
    # author = CustomUserSerializer()

    class Meta:
        model = Article
        fields = ["id", "title", "text", "author", "timezone"]
