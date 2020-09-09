from allauth.account.forms import (
    SignupForm,
    LoginForm,
)


# Override signup form from allauth so that it could have desirable view
class SignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
        self.field_order = ["username", "email", "password1", "password2"]
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter unique name"}
        )
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter email"}
        )
        self.fields["email"].label = "Email"
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Repeat password"}
        )


# Override login form from allauth so that it could have desirable view
class SignInForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter your name"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter password"}
        )
