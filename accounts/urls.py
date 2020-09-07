from django.urls import path, include
from .views import *

urlpatterns = [
    path("sign_up/", SignUpView.as_view(), name="sign_up_v"),
    path("sign_in/", SignInView.as_view(), name="sign_in_v"),
    path("logout/", LogOutView, name="logout_v"),
]
