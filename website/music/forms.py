from django.contrib.auth.models import User
from django import forms

from music.models import Song


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password']

class SongForm(forms.ModelForm):


    class Meta:
        model=Song
        fields = ['song_title', 'file_type', 'is_favorite']


class LoginForm(forms.Form):
    username=forms.CharField(max_length=300)
    password=forms.CharField(widget=forms.PasswordInput)





            #        def clean(self):
 #           form_data = self.cleaned_data
          #  if form_data['password'] != form_data['password_repeat']:
           #     self._errors["password"] = ["Password do not match"]  # Will raise a error message
            #    del form_data['password']
           # return form_data