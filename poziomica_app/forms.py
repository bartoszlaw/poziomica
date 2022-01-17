from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Pomiary


class PomiaryForm(ModelForm):
    class Meta:
        model = Pomiary
        fields = ['nazwa','wynik']