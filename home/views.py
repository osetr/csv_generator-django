from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        user_authenticated = request.user.is_authenticated

        return render(
            request,
            "home.html",
            context={"user_authenticated": user_authenticated,
                     "active_page": "home"},
        )