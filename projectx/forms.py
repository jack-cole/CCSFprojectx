from django import forms
from .models import Club
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


# Form for adding a new Club
class ClubForm(forms.Form):
	name = forms.CharField(label='Club Name', max_length=64,required=True)
	website = forms.CharField(label='Website', max_length=128,required=False)

	class Meta:
		model = Club
		fields = {'name' , 'email' , 'website' , 'meeting_times' , 'president' , 'treasurer' , 'icc_rep'}

	def save(self, commit=True):
		club = Club()
		club.name = self.cleaned_data['name']
		club.website = self.cleaned_data['website']

		if commit:
			club.save()

		return club
	
# Form for editing the a Club that already exists
class EditClubForm(forms.Form):
	id = forms.IntegerField(required=True)
	name = forms.CharField(label='Club Name', max_length=64,required=True)
	website = forms.URLField(label='Website', max_length=128,required=False)
	email = forms.EmailField(label='Email', max_length=256,required=False)
	meeting_times = forms.CharField(label='Meeting Times', max_length=256,required=False)

	class Meta:
		model = Club
		fields = {'id', 'name' , 'email' , 'website' , 'meeting_times'}

	def save(self, commit=True, user_id = None):
		club = Club.objects.filter(id=self.cleaned_data['id'])
		if len(club) == 1:
			club = club[0]
		# check if the person updating the club actually has access
		if user_id in {club.president, club.treasurer, club.icc_rep}:
			club.name = self.cleaned_data['name']
			club.website = self.cleaned_data['website']
			club.email = self.cleaned_data['email']
			club.meeting_times = self.cleaned_data['meeting_times']
	
			if commit:
				club.save()
		else:
			raise ValidationError(message = "User ID " + str(user_id) + " doesn't have permission to edit Club ID " + str(club.id) )

		return club