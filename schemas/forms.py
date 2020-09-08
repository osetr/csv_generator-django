from django import forms
from django.urls import reverse


class NewSchemeForm(forms.Form):
    SEPARATOR_CHOICES = (
        ("comma", "Comma (',')"),
        ("whitespace", "Whitespace (' ')"),
        ("semicolon", "Semicolon (';')"),
    )
    name = forms.CharField(
        label="Scheme name",
        max_length=64,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter scheme name"}
        ),
    )
    separator = forms.CharField(
        label="Column separator",
        widget=forms.Select(choices=SEPARATOR_CHOICES, attrs={"class": "form-control"}),
    )
    columns = forms.CharField(label="", widget=forms.HiddenInput())
