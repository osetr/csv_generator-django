from allauth.account.views import LoginView, SignupView
from .forms import SignUpForm, SignInForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout


# Override signup view from allauth so that it could have desirable view
# It takes parametr form_class with overrided signup form from allauth
# user_authenticated serves as a filter of available information on the page
# active_page serves to distinguish active pages and non active in navbar
class SignUpView(SignupView):
    form_class = SignUpForm

    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        user_authenticated = self.request.user.is_authenticated
        ret.update({"user_authenticated": user_authenticated,
                    "active_page": "sign_up"})
        return ret


# Override login view from allauth so that it could have desirable view
# It takes parametr form_class with overrided login form from allauth
# user_authenticated serves as a filter of available information on the page
# active_page serves to distinguish active pages and non active in navbar
# errors just show if user filled incorrect data
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


# Use view for logout user
def LogOutView(request):
    logout(request)
    return redirect("home_v")
