from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomCreationForm

# Create your views here.


def Home(request):
    return render(request, "home.html")


class SignUp(CreateView):
    form_class = CustomCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'