from django.forms import ModelForm
from .models import Administrator


class AdministratorForm(ModelForm):
    class Meta:
        model = Administrator
        fields = ['title', 'image', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'input'})
        self.fields['description'].widget.attrs.update({'class': 'input'})
