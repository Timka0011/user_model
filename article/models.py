from django.db import models
from accounts.models import CustomUser
from ckeditor.fields import RichTextField

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="image/", blank=True, null=True)
    text = RichTextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timezone = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        # order_by = "-id"

    def get_absolute_url(self):
        return f"/article/{self.id}/"
