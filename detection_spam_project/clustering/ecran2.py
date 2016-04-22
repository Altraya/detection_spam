#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from clustering.form import ScreenOneForm
from clustering.modelStatic import Stats
from . import ecran1
import json
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
			#ici on peut travailler sur notre fichier
			idColumns = request.POST.getlist('champsClassification')
			tabNameColumns = matchNameColumn(idColumns)
			#normalisation
			resultNormalize = normalizeMe(idColumns, fichier)
			#tableau contenant des objets Stats pour pouvoir remplir correctement la vue
			tabObjectStats = matchStats(resultNormalize, tabNameColumns)

			return render(request, 'ecran2.html', {'id_screen': 2, 'objetsStats' : tabObjectStats, 'tabStatsRaw' : resultNormalize})

	else: #si on a pas bien valider le formulaire, on retourne sur l'ecran 1 pour le faire
		return render(request, 'ecran1.html', {'id_screen': 1}) 

#
#	Fonction de normalisation de champs
#	@params : tableaux multidimentionnel contenant les ids des champs de classification a normaliser
#	@fichier : le fichier dans lequel se trouve les champs a normaliser
#	@return : tableau contenant les tableaux resultats des champs normalisés
#
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

#
#	Permet de savoir le nom des colonnes correspondantes a l'id pour l'affichage
#
def matchNameColumn(idColumns):
	tabNameColumns = []

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

	for index, choice in enumerate(tabChoice):
		for idColumn in idColumns:

			if int(idColumn) == int(choice[0]):
				#print "idColumn : "+str(idColumn)+" choice : "+str(choice[0])
				tabNameColumns.append(choice[1])
			
	return tabNameColumns

#
# Permet de remplir des objets stats avec toutes les stats que l'on souhaite pour notre vue
# grace a nos champs normalises
# @params : normalizedColumns toutes nos colonnes normalisees grace a normalizeMe
# @return : un tableau contenant des objets stats remplit
#
def matchStats(normalizedColumns, tabNameColumns):
	tabObjectStats = []
	for index, normalizedColumn in enumerate(normalizedColumns):
		currentStat = Stats(index, normalizedColumn)
		tabObjectStats.append(currentStat)

	for index, objectStat in enumerate(tabObjectStats):
		objectStat._set_nom(tabNameColumns[index])

	return tabObjectStats
		#print "min S : "
		#print(currentStat.minS)
		#print "max s :"
		#print(currentStat.maxS)
		#print "moyenne : "
		#print(currentStat.moyenne)
		#print "ecart_type"
		#print(currentStat.ecart_type)

