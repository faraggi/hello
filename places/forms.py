from django import forms

from .models import Place


# regular form
# class PlacesForm(forms.Form):
# 	iwent = forms.CharField(required=False)
# 	iam = forms.CharField(required=True)
# 	igo = forms.CharField(required=False)

# model form
class PlacesForm(forms.ModelForm):
	class Meta:
		model = Place
		fields = ['iwent', 'iam', 'igo']