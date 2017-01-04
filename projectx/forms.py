from django import forms
from .models import Clubs

class ClubForm(forms.Form):
	name = forms.CharField(label='Club Name', max_length=100,required=True)
	website = forms.CharField(label='Website', max_length=100,required=False)

	class Meta:
		model = Clubs
		fields = {'name' , 'email' , 'website' , 'meeting_times' , 'president' , 'treasurer' , 'icc_rep'}

	def save(self, commit=True):
		club = Clubs()
		club.name = self.cleaned_data['name']
		club.website = self.cleaned_data['website']

		if commit:
			club.save()

		return club