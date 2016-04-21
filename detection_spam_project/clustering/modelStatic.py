#-*- coding: utf-8 -*-
#modele permettant de faire les stats pour le tableau de lecran2
class Stats:
	# idStat : id de la stat (prit dans le formulaire)
	# nom : nom de la stat : freq_something
	# min : minimum de la colonne normalise
	# max : maximum de la colonne normalise
	# moyenne : moyenne de la colonne normalise
	#ecart-type : ecart-type de la colonne normalise
	
	
	def __init__(self, id):
		idStat = id
		nom = ""
		min = 0
		max = 0
		moyenne = 0
		ecart_type = 0

	def _get_nom(self):
		return self._nom
		
	def _set_nom(self, newName):
		self._nom = newName

	nom = property(_get_nom, _set_nom)