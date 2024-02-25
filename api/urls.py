from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("auth/", obtain_auth_token),


    path("", views.AticleView.as_view(), name="list"),
    path("create/", views.ArticleCreateView.as_view(), name="create"),
    path("<int:pk>/", views.AticleView.as_view(), name="create"),
    path("<int:pk>/update/", views.ArticleUpdateView.as_view(), name="update"),
]
