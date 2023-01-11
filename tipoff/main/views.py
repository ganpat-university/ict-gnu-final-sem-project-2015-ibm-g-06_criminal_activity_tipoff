from django.shortcuts import render
from .models import *
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
	print("hello")
	return render(request,"report/report_person.html",{})

def report_activity(request):
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

