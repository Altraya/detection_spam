#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render

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
	if int(id_screen) > 3:
		raise Http404

	"""text = "affichage de l'écran numéro #{0} ! ".format(id_screen)
	return HttpResponse(text)"""

	return render(request, 'ecran'+id_screen+'.html', {'id_screen': id_screen})
