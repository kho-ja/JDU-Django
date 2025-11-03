from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    """
    ModelForm for creating and uploading Application instances.
    """

    class Meta:
        model = Application
        fields = ["title", "description", "file"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Application nomini kiriting",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Application haqida ma'lumot kiriting",
                }
            ),
            "file": forms.FileInput(attrs={"class": "form-control"}),
        }
