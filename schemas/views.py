from django.shortcuts import render
from django.views.generic import View


class AddSchemaView(View):
    def get(self, request):
        user_authenticated = request.user.is_authenticated

        return render(
            request,
            "new_schema.html",
            context={"user_authenticated": user_authenticated,
                     "active_page": "add_schema"},
        )