from django.forms import ModelForm
from .models import *

class activity_report_form(ModelForm):
	class Meta:
		model = activity_report
		# fields = '__all__'
		exclude = ['invistigated']