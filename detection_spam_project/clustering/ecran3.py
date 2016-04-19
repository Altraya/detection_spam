#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render

def view_screen(request):
	#pour marc : http://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html#example-cluster-plot-mini-batch-kmeans-py
	#ca pourra t'inspirer
	#oublie pas dutiliser D3JS pour l'affichage des graphs ! 
	#on doit faire notre propre biblio Kmeans comme en TP mais ca peut t'inspirer
	return render(request, 'ecran3.html', {'id_screen': 3})
