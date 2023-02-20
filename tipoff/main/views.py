from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.


def home_page(request):
	return render(request,"home/homepage.html",{})


def about_us_function(request):
	return render(request,"about_us/about_us.html",{})

def something(request):
	return render(request,"something/something.html",{})


def report(request):
	return render(request,"report/report.html",{})
	
def report_person(request):
	if request.method == 'POST':
		# if person_report_id: # if edit
		# 	form = person_report_form(request.POST, instance=edit) 
		# else: # if create
		print ("here");
		form = person_report_form(request.POST)
		if form.is_valid():
			candidate = form.save(commit=False)
			candidate.save()
			print("saved :: ", candidate)
			return redirect('home_page')
		else:
			print ("error",form.errors)
			context['errors'] = form.errors.as_ul()	

	return render(request,"report/report_person.html",{})

def report_activity(request):
		
		if request.method == 'POST':

		# if person_report_id: # if edit
		# 	form = person_report_form(request.POST, instance=edit) 
		# else: # if create
			form = activity_report_form(request.POST)
			if form.is_valid():
				candidate = form.save(commit=False)
				candidate.save()
				print("saved :: ", candidate)
				return redirect('home_page')
			else:
				context['errors'] = form.errors.as_ul()	

		return render(request,"report/report_activity.html",{})


def admin_home(request):
	my_person_reports = person_report.objects.all().filter(
		invistigated=False
	)
	my_activity_reports = activity_report.objects.all().filter(
		invistigated=False
	)
	print("asdasd")
	context = {
		"my_person_reports":my_person_reports,
		"my_activity_reports":my_activity_reports,
	}
	return render(request,"admin/home.html",context)

