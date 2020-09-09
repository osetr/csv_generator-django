from django.urls import path
from .views import SignInView, SignUpView, LogOutView

urlpatterns = [
    path(r"sign_up/", SignUpView.as_view(), name="sign_up_v"),
    path(r"sign_in/", SignInView.as_view(), name="sign_in_v"),
    path(r"logout/", LogOutView, name="logout_v"),
]
