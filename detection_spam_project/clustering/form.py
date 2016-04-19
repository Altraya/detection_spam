from django import forms

class ScreenOneForm(forms.Form):

	fichierData = forms.FileField(required=True)
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
		(19, 'word_freq_you'),
		(20, 'word_freq_credit'),
		(21, 'word_freq_your'),
		(22, 'word_freq_font'),
		(23, 'word_freq_000'),
		(24, 'word_freq_money'),
		(25, 'word_freq_hp'),
		(26, 'word_freq_hpl'),
		(27, 'word_freq_george'),
		(28, 'word_freq_650'),
		(29, 'word_freq_lab'),
		(30, 'word_freq_labs'),
		(31, 'word_freq_telnet'),
		(32, 'word_freq_857'),
		(33, 'word_freq_data'),
		(34, 'word_freq_415'),
		(35, 'word_freq_85'),
		(36, 'word_freq_technology'),
		(37, 'word_freq_1999'),
		(38, 'word_freq_parts'),
		(39, 'word_freq_pm'),
		(40, 'word_freq_direct'),
		(41, 'word_freq_cs'),
		(42, 'word_freq_meeting'),
		(43, 'word_freq_original'),
		(44, 'word_freq_project'),
		(45, 'word_freq_re'),
		(46, 'word_freq_edu'),
		(47, 'word_freq_table'),
		(48, 'word_freq_conference'),
		(49, 'char_freq_;'),
		(50, 'char_freq_'),
		(51, 'char_freq_['),
		(52, 'char_freq_!'),
		(53, 'char_freq_$'),
		(54, 'char_freq_#'),
		(55, 'capital_run_length_average'),
		(56, 'capital_run_length_longest'),
		(57, 'capital_run_length_total')

	)

	champsClassification = forms.MultipleChoiceField(required = True, choices=tabChoice, widget=forms.SelectMultiple(attrs={'class':'input-control select multiple full-size height100'}))