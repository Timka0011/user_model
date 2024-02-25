from collections.abc import Callable
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render
from .models import Article

# Create your views here.
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy


class AricleListView(ListView):
    model = Article
    template_name = "home.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "detail.html"


class CreateArticleView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "create.html"
    fields = ["title", "text", "image"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateArticleView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "update.html"
    fields = ["title", "text", "image"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class DeleteArticleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
