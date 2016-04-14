#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	"""Test"""
	text = """ <h1> Welcome home ! </h1>
				<p>
					<div class="stepper" data-role="stepper"></div>
				</p>
			"""
	return HttpResponse(text)

def view_screen(request, id_screen):
	text = "affichage de l'écran numéro #{0} ! ".format(id_screen)
	return HttpResponse(text)
