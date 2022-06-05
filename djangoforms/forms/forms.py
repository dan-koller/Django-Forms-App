from django import forms
from .models import Participants


class RegistrationForm(forms.Form):
    name = forms.CharField(label="your name")
    age = forms.IntegerField(label="your age")
    favorite_lang = forms.CharField(label="your favorite language")
    birthday = forms.DateField(label="your birthday")

    class Meta:
        model = Participants

        fields = [
            "name",
            "age",
            "favorite_lang",
            "birthday"
        ]
