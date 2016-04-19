from django import forms

class ScreenOneForm(forms.Form):

	databaseFile = forms.FileField(required=True)
	n = forms.CharField(label="Choose n observations", 
		required = True, 
		widget=forms.TextInput(attrs={'class': 'input-control text', 'placeholder': 'Choose n observations'}))
	k = forms.CharField(label="Choose k clusters", required = True, widget=forms.TextInput(attrs={'class': 'input-control text', 'placeholder': '... into k clusters'}))
	
	tabChoice = (
		(1, 'word_freq_make'),
		(2, 'word_freq_address'),
		(3, 'word_freq_all'),
		(4, 'word_freq_3d'),
		(5, 'word_freq_our'),
		(6, 'word_freq_over'),
		(7, 'word_freq_remove'),
		(8, 'word_freq_internet'),
		(9, 'word_freq_order'),
		(10, 'word_freq_mail'),
		(11, 'word_freq_receive'),
		(12, 'word_freq_will'),
		(13, 'word_freq_people'),
		(14, 'word_freq_report'),
		(15, 'word_freq_addresses'),
		(16, 'word_freq_free'),
		(17, 'word_freq_business'),
		(18, 'word_freq_email'),
	)

	champsClassification = forms.ChoiceField(required = True, choices=tabChoice)