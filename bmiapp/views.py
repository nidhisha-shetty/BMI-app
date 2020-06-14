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
 	result=obj.weight / ((obj.height/100) ** 2)
 	messages.info(request, obj.name + " your BMI is " + str(result))
 	if int(result) in range(16, int(18.5)):
 		messages.info(request, "You are UnderWeight")
 	elif int(result) in range(18.5, int(24.9)):
 		messages.info(request, "You are Normal!")
 	elif int(result) in range(25, int(29.9)):
 		messages.info(request, "You are Overweight")
 	elif int(result) in range(30, int(39.9)):
 		messages.info(request, "You are Obese")
 	else:
 		messages.info(request, "You are Extra Obese")
 	context = {
 		'form': form,
		'obj':obj
 	}
 	return render(request, "home.html", context)
	# return HttpResponse("My BMI app")
