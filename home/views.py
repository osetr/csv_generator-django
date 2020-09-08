from django.shortcuts import render
from django.views.generic import View
from schemas.models import Schema
from django.http import Http404, JsonResponse


class HomeView(View):
    def get(self, request):
        user_authenticated = request.user.is_authenticated
        try:
            schemas = Schema.objects.filter(author=request.user).values()
        except TypeError:
            schemas = []
            print("User not authanticated")
        return render(
            request,
            "home.html",
            context={
                "user_authenticated": user_authenticated,
                "active_page": "home",
                "schemas": schemas,
            },
        )


def delete_schema_ajax(request, pk):
    if request.is_ajax():
        try:
            Schema.objects.get(pk=pk).delete()
            response = "Successfuly deleted"
        except Schema.DoesNotExist:
            response = "Something went wrong"

        return JsonResponse({"response": response})
    else:
        raise Http404
