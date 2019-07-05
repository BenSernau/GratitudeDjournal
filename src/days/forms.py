from django import forms 
from .models import Day
import datetime
from django.http import HttpResponse

class DayForm(forms.ModelForm):
	today = forms.DateField(label = "", widget = forms.DateInput(
		attrs = {
			"placeholder": "Write the date here...",
			"style": "width: 160px;"
			}
		)
	)
	firstItem = forms.CharField(label = "", widget = forms.Textarea(
		attrs = {
			"placeholder": "Good thing #1...",
			"rows": 5,
			"style": "width: 160px;"
			}
		)
	)
	secondItem = forms.CharField(label = "", widget = forms.Textarea(
		attrs = {
			"placeholder": "Good thing #2...",
			"rows": 5,
			"style": "width: 160px;"
			}
		)
	)
	thirdItem = forms.CharField(label = "", widget = forms.Textarea(
		attrs = {
			"placeholder": "Good thing #3...",
			"rows": 5,
			"cols": 20,
			"style": "vertical-align: top;"
			}
		)
	)	
	class Meta:
		model = Day
		fields = ['today',
				'firstItem', 
				'secondItem',
				'thirdItem']

	def clean_today(self, *args, **kwargs):
		today = self.cleaned_data.get("today")
		for obj in Day.objects.all():
			if  obj.today == today:
				raise forms.ValidationError("You can't have multiple entries for the same day.")
		return today