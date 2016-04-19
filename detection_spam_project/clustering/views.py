#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render
<<<<<<< HEAD
import ecran1
import ecran2
import ecran3
=======
from clustering.form import ScreenOneForm
from pprint import pprint

def home2(request):
	"""Test"""
	text = """ <h1> Welcome home ! </h1>
				<p>
					<div class="stepper" data-role="stepper"></div>
				</p>
			"""
	return HttpResponse(text)
>>>>>>> ad113266250242ef697fd11e4d5bda688e10f0e5

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
	

<<<<<<< HEAD

=======
	return render(request, 'ecran'+id_screen+'.html', {'id_screen' : id_screen})
>>>>>>> ad113266250242ef697fd11e4d5bda688e10f0e5
