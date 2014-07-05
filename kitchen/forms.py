from django import forms
from kitchen.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(help_text="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(help_text="Email", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    website = forms.URLField(help_text="Website", widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    picture = forms.ImageField(help_text="Profile Picture", required=False)

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
