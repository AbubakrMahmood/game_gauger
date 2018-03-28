from django import forms
from django.contrib.auth.models import User
from .models import Game, Review, UserProfile, Categories

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['categories']

class GameForm(forms.ModelForm):
    game = forms.CharField(max_length=128,
                           help_text="Please enter the game name.")

    genre = forms.CharField(max_length=30,
                             help_text="What is its main genre?")

    publisher = forms.CharField(max_length=50,
                             help_text="Who is the main publisher?")

    developer = forms.CharField(max_length=50,
                             help_text="Who is the main developer?")

    logo = forms.ImageField(help_text="Please add an image here, not adding one is fine too :).",
                            initial = 'None/no-img.jpg', required=False)

    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Game
        fields = ('game','genre', 'publisher', 'developer', 'logo')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('game', 'user_name', 'comment', 'rating')
