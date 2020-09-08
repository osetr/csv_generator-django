from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import NewSchemeForm
from django.contrib.auth.mixins import LoginRequiredMixin
import re
from .models import Schema


class AddSchemaView(LoginRequiredMixin, View):
    login_url = "/users/sign_in/"

    def get(self, request):
        form = NewSchemeForm()
        user_authenticated = request.user.is_authenticated

        return render(
            request,
            "new_schema.html",
            context={
                "user_authenticated": user_authenticated,
                "active_page": "add_schema",
                "form": form,
            },
        )

    def post(self, request):
        def get_json_from_schema(name, separator, columns):
            result = {"scheme_name": name, "separator": separator}
            columns = re.sub(r"<td><a.*?<\/a><\/td>", "", columns)
            columns = re.findall(r"<td.*?\/td>", columns)
            columns = list(map(lambda a: re.search(">(.*?)<", a).group(1), columns))
            result.update(
                {
                    "columns": [
                        {
                            "name": columns[i * 3],
                            "type": columns[i * 3 + 1],
                            "order": columns[i * 3 + 2],
                        }
                        for i in range(int(len(columns) / 3))
                    ]
                }
            )
            for column in result['columns']:
                if re.findall(r"Text", column['type']):
                    column.update({'sentences_amount': re.search("\((.*?)\)", column['type']).group(1)})
                    column.update({'type': 'Text'})
            result['columns'].sort(key=lambda i: int(i['order']))

            return result

        form = NewSchemeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            separator = form.cleaned_data["separator"]
            columns = form.cleaned_data["columns"]
            columns = get_json_from_schema(name, separator, columns)
            schema = Schema(name=name, separator=separator)
            schema.columns = columns['columns']
            schema.save()

        return redirect("add_schema_v")