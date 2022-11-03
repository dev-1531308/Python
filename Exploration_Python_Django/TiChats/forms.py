from django import forms



from TiChats.models import Chat, Couleur



class ChatForm(forms.ModelForm):

    class Meta:

        model = Chat

        fields = [ "nom", "age","activitePref", "couleur","photo"]



class CouleurForm(forms.ModelForm):

    class Meta:

        model = Couleur

        fields = [ "nomCouleur" ]