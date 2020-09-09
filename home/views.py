from django.shortcuts import render
from django.views.generic import View
from schemas.models import Schema
from django.http import Http404, JsonResponse


# user_authenticated serves as a filter of available information on the page
# active_page serves to distinguish active pages and non active in navbar
# schemas storages all schemas of current user
# it will be shown if user authanticated
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


# view to delete schema in click
# as a parametr it takes pk(id) of schema to delete
def delete_schema_ajax(request, pk):
    if request.is_ajax():
        try:
            Schema.objects.get(pk=pk).delete()
            response = "Successfuly deleted"
        except Schema.DoesNotExist:
            response = "Something went wrong"
        finally:
            return JsonResponse({"response": response})
    else:
        raise Http404
