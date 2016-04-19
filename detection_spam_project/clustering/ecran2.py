#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from clustering.form import ScreenOneForm
import ecran1

def view_screen(request):

	if request.method == 'POST': #just work in screen 2 and 3
		form = ScreenOneForm(request.POST, request.FILES)
		#on a ici toutes les données de l'écran 1 obtenu via POST
		#on doit traiter les champs demandés via l'id de la colonne obtenu sur champClassification
		print form.is_valid(), form.errors, type(form.errors)
		if form.is_valid():
			fichier = request.FILES['file']
			print "fichier : "
			print fichier
			return render(request, 'ecran2.html', {'id_screen': 2})

		else:
			# formulaire faux on retourne le remplir
			print "nope"
			return render(request, 'ecran2.html', {'id_screen': 2})

			#return render(request, ecran1.view_screen);

	else: #si on a pas bien valider le formulaire, on retourne sur l'ecran 1 pour le faire
		print "note P"
		return render(request, 'ecran1.html', {'id_screen': 1}) 

