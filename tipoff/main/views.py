from django.shortcuts import render

# Create your views here.


def home_page(request):
	return render(request,"home/homepage.html",{})


def about_us(request):
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


