
from django.forms import ModelForm
from .models import user_table

class InputForm(ModelForm):
     class Meta:
         model = user_table
         fields = ['username', 'password']