from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from TiChats.models import Chat, Couleur



class ChatForm(forms.ModelForm):

    class Meta:

        model = Chat

        fields = [ "nom", "age", "ageString","activitePref", "couleur","photo"]



class CouleurForm(forms.ModelForm):

    class Meta:

        model = Couleur

        fields = [ "nomCouleur" ]

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name']