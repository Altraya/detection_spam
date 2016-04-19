#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render
from clustering.form import ScreenOneForm
import ecran1
import ecran2
import ecran3

def home2(request):
	"""Test"""
	text = """ <h1> Welcome home ! </h1>
				<p>
					<div class="stepper" data-role="stepper"></div>
				</p>
			"""
	return HttpResponse(text)

def home(request):
	return render(request,'home.html')


def view_screen(request, id_screen):
	intID = int(id_screen)

	if intID == 1:
		#return render(request, 'ecran'+id_screen+'.html', {'id_screen': id_screen})
		return ecran1.view_screen(request)
	elif intID == 2:
		return ecran2.view_screen(request)
	elif intID == 3:
		return ecran3.view_screen(request)	
	else:
		raise Http404
	

"""
def show(request):
	if request.method == 'POST':
		form = ScreenOneForm(request.POST)

		if form.is_valid():
			choixClassification = form.cleaned_data['choixClassification'];

		else: 
			form = ScreenOneForm()

	return render(request, 'testEcran2.html', locals())

"""