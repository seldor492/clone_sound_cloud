from django import forms
from django.forms import ModelForm
from modules.Artistas.models import Artista

GENEROS = (
    ("LA","Latina"),
    ("PO","Pop"),
    ("RO","Rock"),
    ("IA","Indie/Alternativa"),
    ("DA","Dance"),
    ("HH","Hip Hop"),
    ("RB","Rhythm and Blues"),
    ("CO","Country"),
    ("FA","Folk & Americana"),
    ("ME", "Metal"),
    ("SO", "Soul"),
    ("JA", "Jazz"),
    ("BL", "Blues"),
    ("PU", "Punk"),
    ("FU", "Funk"),
    ("CL", "Clásica"),

)

class AddArtistaForm(forms.Form):

    nombre = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':'mdl-textfield__input',
                'id':'input_nombre',
            }
        )
    )
    nacionalidad = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':'mdl-textfield__input',
                'id':'input_nacionalidad',
            }
        )
    )
    acerca_de = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'class':'mdl-textfield__input',
                'id':'input_acerca_de',
            }
        )
    )
    tipo_artista = forms.ChoiceField(
        choices=(('G','Grupo'),('S','Solista')),
        widget = forms.Select(
            attrs={
                'class':'mdl-textfield__input',
                'id':'input_tipo_artista',
            }
        )
    )
    genero = forms.ChoiceField(choices=GENEROS,
        widget = forms.Select(
            attrs={
                'class':'mdl-textfield__input',
                'id':'input_genero',
            }
        )
    )

class AddAlbumForm(forms.Form):
    nombre = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':'mdl-textfield__input',
                'id':'input_nombre',
            }
        )
    )
    anio = forms.IntegerField(
        widget = forms.NumberInput(
            attrs={
                'class':'mdl-textfield__input',
                'id':'input_anio',
            }
        )
    )

    genero = forms.ChoiceField(choices=GENEROS,
        widget = forms.Select(
            attrs={
                'class':'mdl-textfield__input',
                'id':'input_genero',
            }
        )
    ) 
