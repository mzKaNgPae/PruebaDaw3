from django import forms
from .models import Auto

class CrearAuto (forms.ModelForm):
    class Meta:
        model = Auto
        exclude = []
        widgets = {
            'descripcion': forms.Textarea(),
            # 'imagen': forms.FileInput(
            #     attrs={
            #         'class':'btn btn-success col fileinput-button dz-clickable',
            #         'accept':'image/*'
            #     })
        }

    # def __init__(self, *args, **kwargs):
    #     super(CrearAuto, self).__init__(*args, **kwargs)

class ModificarAuto (forms.ModelForm):
    class Meta:
        model = Auto
        exclude = []
        widgets = {
            'descripcion': forms.Textarea()
        }

    