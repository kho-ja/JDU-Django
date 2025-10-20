from django import forms
from .models import Student


class StudentSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Student
        fields = [
            "name",
            "age",
            "email",
            "password",
        ]
