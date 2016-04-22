#-*- coding: utf-8 -*-
#modele permettant de faire les stats pour le tableau de lecran2
class Stats:
	# idStat : id de la stat (prit dans le formulaire)
	# nom : nom de la stat : freq_something
	# min : minimum de la colonne normalise
	# max : maximum de la colonne normalise
	# moyenne : moyenne de la colonne normalise
	#ecart-type : ecart-type de la colonne normalise
	#normalizedColumn : la colonne normalise
	
	
	def __init__(self, id, normalizedColumn):
		idStat = id
		self._normalizedColumn = normalizedColumn
		self.goStats(normalizedColumn)

	def _get_nom(self):
		return self._nom

	def _get_minS(self):
		return self._minS

	def _get_maxS(self):
		return self._maxS

	def _get_moyenne(self):
		return self._moyenne 

	def _get_ecart_type(self):
		return self._ecart_type

	def _get__normalizedColumn(self):
		return self._normalizedColumn

	def _set_nom(self, newName):
		self._nom = newName

	def _set_minS(self, minValue):
		self._minS = minValue

	def _set_maxS(self, maxValue):
		self._maxS = maxValue

	def _set_moyenne(self, moyenneValue):
		self._moyenne = moyenneValue

	def _set_ecart_type(self, ecart_typeValue):
		self._ecart_type = ecart_typeValue

	nom = property(_get_nom, _set_nom)
	minS = property(_get_minS, _set_minS)
	maxS = property(_get_maxS, _set_maxS)
	moyenne = property(_get_moyenne, _set_moyenne)
	ecart_type = property(_get_ecart_type, _set_ecart_type)

	def doMoyenne(self, myList):
		return sum(myList, 0.0) / len(myList)

	def doVariance(self, myList):
		m = self.doMoyenne(myList)
		return self.doMoyenne([(x-m)**2 for x in myList])

	def doEcartType(self, myList):
		return self.doVariance(myList)**0.5

	#Permet deffectuer toutes les statistiques en donnant juste une liste a notre fonction
	#Elle soccupe elle meme de tout faire
	def goStats(self, myList):
		self._set_minS(min(myList))
		self._set_maxS(max(myList))
		self._set_moyenne(self.doMoyenne(myList))
		self._set_ecart_type(self.doEcartType(myList))

	def to_JSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)