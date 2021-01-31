from django import forms
from .models import Services, Category


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = '__all__'
