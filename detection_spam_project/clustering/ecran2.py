#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from clustering.form import ScreenOneForm
import ecran1
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
			print "fichier : "
			print fichier
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

	# [ 3.72 ] [1] 
	print params

	currentLine = []
	matrix = []
	data = []
	test = []
	#ouverture fichier
	for line in fichier.readlines():
		currentLine = line.split(",")
		#on doit rstrip toutes les infos de cette liste pour ne pas avoir de \n
		#il faut donc la parcourrir et les enlever
		for number in currentLine:
			number.rstrip()
			matrix.append(number)
	#test = data.readlines()
	#print number
	#print matrix


	
	#i = 0 #index les lignes vont jusqu'a 57
	#line = data.split(",")



	print "matrix = " + str(matrix)
	#for eachNumber in line:
		#print line
		#print eachNumber
		#if "\n" in line:
			#print "\n trouvé"
			#gaucheEtDroite = line.split('\n')
			#print gaucheEtDroite
	"""reader = csv.reader(data)

	for row in reader:
		print row
			#row[i] = (float(row[i]) - minArr[i])

	print yeah"""

	#print data
	#print ""
	#print line

	#cherche toutes les colonnes correspondantes et crée un tableau a la volée contenant les valeurs de chaque colonne

	#normalise chaque colonne

	#retourne le resultat
	return "oui"