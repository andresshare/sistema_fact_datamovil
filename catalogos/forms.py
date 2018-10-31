from django import forms

from catalogos.models import  Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=['descripcion','activo']
        labels= {'descripcion':'Descripcion de las categoria','activo':'Estado'},
        widget = {'descripcion':forms.TextInput()}

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })


