from django import forms
from django.contrib.auth.models import User
from .models import User_Profile
from django.contrib.auth.forms import UserCreationForm


class Userform(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

        labels =(
            'password1','Password',
            'password2','Confirm Password'
        )

class UserProfileInfoform(forms.ModelForm):
    bio = forms.CharField(required=False)
    student = 'student'
   
    user_types = [
        (student,'student'),
        
        
    ]
    user_type = forms.ChoiceField(required=True, choices=user_types)

    class Meta():
        model = User_Profile
        fields = ('bio','user_type')
            