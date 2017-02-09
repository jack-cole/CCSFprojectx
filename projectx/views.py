from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .forms import ClubForm, EditClubForm
from .models import Club, User
from django.db.models import Q

def index(request):
	return render(request, 'index.html')

def listclubs(request):
	clublist = Club.objects.all()
	return render(request, 'clubs.html', {'clublist': clublist})

def editclub(request):
	
	class ClubDataEntry():
		form = None
		president = None
		treasurer = None
		icc_rep = None
		
	if request.user.is_authenticated():
		logged_in_user = request.user

		# get the clubs that the user is an officer of
		clubs = Club.objects.filter(
			Q(president=logged_in_user.id) |
			Q(treasurer=logged_in_user.id) |
			Q(icc_rep=logged_in_user.id)
			)
		
		# handle submitted edits		
		if request.method == 'POST':
			form = EditClubForm(request.POST)
			if form.is_valid():
				# process the data in form.cleaned_data as required
				form.save(user_id = logged_in_user.id)

		# Create a form for each club the user is an officer of
		forms = list()
		for club in clubs:
			club_data = {
				'id': club.id,
				'name': club.name,
				'email': club.email,
				'website': club.website,
				'meeting_times': club.meeting_times,
				'president': club.president,
				'treasurer': club.treasurer,
				'icc_rep': club.icc_rep,
			}
			form = EditClubForm(initial=club_data)
			forms.append(form)

		return render(request, 'editclub.html', {'user': logged_in_user, 'forms': forms})
	
	else:
		return HttpResponseRedirect('/accounts/login/')
	
	

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