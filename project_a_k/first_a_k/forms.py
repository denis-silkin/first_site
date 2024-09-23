from django.forms import ModelForm
from .models import Administrator


class AdministratorForm(ModelForm):
    class Meta:
        model = Administrator
        fields = ['title', 'image', 'description']
