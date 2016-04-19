from django import forms

class ScreenOneForm(forms.Form):
	databaseFile = forms.FileField(required=True)
	n = forms.CharField(label="Choose n observations", required = True)
	k = forms.CharField(label="Choose k clusters", required = True)
	champsClassification = forms.ChoiceField(required = True)
