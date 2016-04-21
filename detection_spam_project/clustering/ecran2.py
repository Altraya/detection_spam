#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from clustering.form import ScreenOneForm
from . import ecran1
import csv
import re



def view_screen(request):

	if request.method == 'POST': #just work in screen 2 and 3
		form = ScreenOneForm(request.POST, request.FILES)
		#on a ici toutes les données de l'écran 1 obtenu via POST
		#on doit traiter les champs demandés via l'id de la colonne obtenu sur champClassification
		#print form.is_valid(), form.errors, type(form.errors)
		if form.is_valid():
			fichier = request.FILES['fichierData']
			print("fichier : ")
			print(fichier)
			#ici on peut travailler sur notre fichier
			#idColumns = []
			idColumns = request.POST.getlist('champsClassification')
			#normalisation
			resulNormalize = normalizeMe(idColumns, fichier)

			return render(request, 'ecran2.html', {'id_screen': 2})

		else:
			#a traiter quand le formulaire n'est pas valide
			return render(request, 'ecran2.html', {'id_screen': 1})

	else: #si on a pas bien valider le formulaire, on retourne sur l'ecran 1 pour le faire
		return render(request, 'ecran1.html', {'id_screen': 1}) 

"""
	Fonction de normalisation de champs
	@params : tableaux multidimentionnel contenant les ids des champs de classification a normaliser
	@fichier : le fichier dans lequel se trouve les champs a normaliser
	@return : tableau contenant les tableaux resultats des champs normalisés
"""
def normalizeMe(params, fichier):

	linesWithDefaut = [] #line avec des \n
	matrixWithDefaut = []

	#Remplit matrix par chaque ligne
	for line in fichier.readlines():
		linesWithDefaut = line.split(",")
		matrixWithDefaut.append(linesWithDefaut)

	#on doit rstrip toutes les infos de cette liste pour ne pas avoir de \n
	#il faut donc la parcourrir et les enlever	
	#enleve dans chaque ligne remplit precedemment les \n
	for linesWithDefaut in matrixWithDefaut:
		for index, number in enumerate(linesWithDefaut):
			linesWithDefaut[index] = number.rstrip()
		
	#now matrixWithDefaut is a matrix without defaut o/
	#this matrix contain lines of files
	#we need now to search columns we need for next step

	#params contient les valeurs des indices des champs de classification que l'on veut
	#sous forme [u'2', u'3'] par exemple pour les champs 2 et 3

	column = []
	columns = []
	indiceClassification = []
	normalizedColumn = []
	normalizedColumns = []
	
	size = len(params)

	for i in range (size) :
		indiceClassification.append(params[i])


	#cherche toutes les colonnes correspondantes et crée un tableau a la volée contenant les valeurs de chaque colonne
	for currentIndice in indiceClassification:
		for lines in matrixWithDefaut:
			for index, number in enumerate(lines):
				
				if int(currentIndice) == int(index):
					column.append(float(lines[index-1])) #dans le tableau indice a partir de 0 o/
		columns.append(column)
		column = []

	#normalise chaque colonne

	for column in columns:
		minColumn = min(column)
		maxColumn = max(column)

		for index, row in enumerate(column):
			diviseur = maxColumn - minColumn
			if diviseur == 0:
				#si on a le diviseur qui vaut 0 ca veut dire que toute la ligne vaut 0 donc row = 0
				row = 0.00
				
			else:
				numerateur = float(row) - minColumn
				row = numerateur / diviseur
		
			normalizedColumn.append(row)
		normalizedColumns.append(normalizedColumn)
		normalizedColumn = []
		#@todo
		
	#print(normalizedColumns)
	#retourne le resultat
	return normalizedColumns 