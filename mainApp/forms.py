from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from api import models as apiModels
class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username','password1', 'password2',) 
        #fields = "__all__"
        labels = {
            'email' : 'Email',
        }

class empForm(forms.ModelForm):

    class Meta:
        model = apiModels.empData
        #fields = "__all__"
        exclude = ('eid', 'status')
