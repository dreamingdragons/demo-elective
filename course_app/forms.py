from django import forms

from .models import db

class apply_form(forms.Form):
	roll_no = forms.CharField(max_length=8)
	name = forms.CharField()
	email = forms.EmailField()
	CHOICES = (('csa','Computer Science A'),('csb','Computer Science B'),('bca','BCA'),('it','Information Technology'),
		('ct','Computer Technology'),('ss','Software Systems'),('mca','MCA'),('da','Data Analysis'),('net','Networking'))
	department = forms.ChoiceField(choices=CHOICES)
	CHOICES = ((1,'I year'),(2,'II year'),(3,'III year'))
	year = forms.ChoiceField(choices=CHOICES)

	def clean_roll_no(self,*args,**kwargs):
		roll_no = self.cleaned_data.get('roll_no')
		if db.objects.filter(roll_no=roll_no).exists():
			raise forms.ValidationError('User alread registered...')
		return roll_no