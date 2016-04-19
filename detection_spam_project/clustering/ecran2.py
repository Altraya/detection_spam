from django.http import HttpResponse, Http404
from django.shortcuts import render

def view_screen(request):

	return render(request, 'ecran2.html', {'id_screen': 2})
