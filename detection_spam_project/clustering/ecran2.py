#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render
from clustering.form import ScreenOneForm

def view_screen(request):

	if request.method == 'POST': #just work in screen 2 and 3
		form = ScreenOneForm(request.POST)
		#on a ici toutes les données de l'écran 1 obtenu via POST
		#on doit traiter les champs demandés via l'id de la colonne obtenu sur champClassification

		return render(request, 'ecran2.html', {'id_screen': 2})
	else: #si on a pas bien valider le formulaire, on retourne sur l'ecran 1 pour le faire
		return render(request, 'ecran1.html', {'id_screen': 1}) 

