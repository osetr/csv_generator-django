from django import forms


class NewSchemaForm(forms.Form):
    SEPARATOR_CHOICES = (
        ("comma", "Comma (',')"),
        ("whitespace", "Whitespace (' ')"),
        ("semicolon", "Semicolon (';')"),
    )
    name = forms.CharField(
        label="Schema name",
        max_length=64,
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Enter schema name"}
        ),
    )
    separator = forms.CharField(
        label="Column separator",
        widget=forms.Select(
            choices=SEPARATOR_CHOICES,
            attrs={"class": "form-control"}),
        )
    columns = forms.CharField(label="", widget=forms.HiddenInput())
