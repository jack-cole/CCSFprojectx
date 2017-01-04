from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .forms import ClubForm
from .models import Clubs

def index(request):
	return render(request, 'index.html')

def listclubs(request):
	clublist = Clubs.objects.all()
	return render(request, 'clubs.html', {'clublist': clublist})

def addclub(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ClubForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			form.save()

			# redirect to a new URL:
			return HttpResponseRedirect('/thanks/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = ClubForm()

	return render(request, 'addclub.html', {'form': form})

def thanks(request):
	template = loader.get_template('thanks.html')
	return HttpResponse(template.render(request))