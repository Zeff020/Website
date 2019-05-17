from django import forms

from .models import Materials_Update

class PostForm(forms.ModelForm):

    class Meta:
        model = Materials_Update
        fields = ('name', 'text')