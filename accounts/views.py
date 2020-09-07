from django.shortcuts import render
from allauth.account.views import LoginView, SignupView
from .forms import SignUpForm, SignInForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout


class SignUpView(SignupView):
    form_class = SignUpForm

    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        user_authenticated = self.request.user.is_authenticated
        ret.update({"user_authenticated": user_authenticated, "active_page": "sign_up"})
        return ret


class SignInView(LoginView):
    form_class = SignInForm

    def get_context_data(self, **kwargs):
        errors = []
        if self.request.method == "POST":
            username = self.request.POST["login"]
            password = self.request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if not user.is_active:
                    errors.append("Your account has been deactivated")
                else:
                    login(self.request, user)
                    return redirect("home_v")
            else:
                errors.append("Incorrect username or password")
        ret = super().get_context_data(**kwargs)
        user_authenticated = self.request.user.is_authenticated
        ret.update(
            {
                "user_authenticated": user_authenticated,
                "active_page": "sign_in",
                "errors": errors,
            }
        )
        return ret


def LogOutView(request):
    logout(request)
    return redirect("home_v")