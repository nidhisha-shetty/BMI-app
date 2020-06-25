from django.shortcuts import render
from django.http import HttpResponse
from .forms import BMI_forms
from .models import BMI
from django.contrib import messages
# Create your views here.
def home_view(request):
 	form = BMI_forms(request.POST or None)
 	if form.is_valid():
 	 	form.save()
 	 	form = BMI_forms()
 	obj=BMI.objects.last()
 	result=obj.weight_in_kgs / ((obj.height_in_cms/100) ** 2)
 	messages.info(request, obj.name + " your BMI is " + str(result))
 	if int(result) in range(16, 19):
 		messages.info(request, "You are UnderWeight")
 	elif int(result) in range(18, 25):
 		messages.info(request, "You are Normal !!")
 	elif int(result) in range(25, 30):
 		messages.info(request, "You are Overweight")
 	elif int(result) in range(30, 40):
 		messages.info(request, "You are Obese")
 	elif int(result) in range(40, 100):
 		messages.info(request, "You are Extra Obese. Kindly consult a doctor")
 	else:
 		messages.info(request, "Incorrect input")
 	context = {
 		'form': form,
		'obj':obj
 	}
 	return render(request, "home.html", context)
	# return HttpResponse("My BMI app")
