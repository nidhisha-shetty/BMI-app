from django import forms
from .models import BMI

class BMI_forms(forms.ModelForm):
	class Meta:
		model = BMI
		fields = [
			'name',
			'height_in_cms',
			'weight',
		]