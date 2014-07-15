from django import forms
from kitchen.models import UserProfile, UserIngredient, UserRecipe
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

class IngredientForm(forms.ModelForm):
    name = forms.CharField(help_text="Ingredient Name", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserIngredient
        fields = ('name',)
        exclude = ['user']

class RecipeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'rec_title', 'placeholder': 'Title'}))
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'class': 'rec_ing', 'placeholder': 'Ingredients'}))
    instructions = forms.CharField(widget=forms.Textarea(attrs={'class': 'rec_dir', 'placeholder': 'Directions'}))

    class Meta:
        model = UserRecipe
        fields = ('name', 'ingredients', 'instructions',)
        exclude = ['user',]
