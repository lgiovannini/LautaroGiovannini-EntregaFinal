from django import forms

class RopaFormBase(forms.Form):
    type = forms.CharField(max_length=15)
    brand = forms.CharField(max_length=15)
    size = forms.CharField(max_length=15)    

class CrearRopaForm(RopaFormBase):...

class EditarRopaForm(RopaFormBase):...
    
class BuscarRopaForm(forms.Form):
    type = forms.CharField(max_length=15, required=False)