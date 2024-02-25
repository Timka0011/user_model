from django.urls import path
from .views import Home, SignUp

urlpatterns = [
    # path('', Home, name='home' ),
    path('signup/', SignUp.as_view(), name='signup')
]
