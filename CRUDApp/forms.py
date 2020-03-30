from django import forms

from .models import murid


class FormMurid(forms.ModelForm):
    class Meta:
        model = murid
        fields = "__all__"
