from django import forms

class ImgForm(forms.Form):
	imagefile = forms.ImageField()