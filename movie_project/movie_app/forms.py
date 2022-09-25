from django import forms
from .models import movies

class movieform(forms.ModelForm):
    class Meta:
        model=movies
        fields=['name','description','year','image']
