from django import forms
from django.forms.models import ModelForm
from .models import Lead

class LeadModelForm(ModelForm):
    class Meta():
        model = Lead
        fields = (
            'firstname',
            'lastname',
            'age',
            'agent'
        )

class LeadForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    age = forms.IntegerField()
    # agent = forms.Foreign