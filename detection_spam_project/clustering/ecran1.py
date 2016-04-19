from django.http import HttpResponse, Http404
from django.shortcuts import render
from clustering.form import ScreenOneForm

def view_screen(request):

	print locals()
	print request.POST
	print request.POST.get('n')
	print request.POST.get('k')

	if request.method == 'POST': #just work in screen 2 and 3
		form = ScreenOneForm(request.POST)

	else:
		form = ScreenOneForm()

	return render(request, 'ecran1.html', locals())