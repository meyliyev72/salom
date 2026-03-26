from django import forms
from .models import Taom

class StudentForm(forms.ModelForm):
    class Meta:
        model = Taom
        fields = ['title' , 'ingredients' , 'instructions' , 'rasm']