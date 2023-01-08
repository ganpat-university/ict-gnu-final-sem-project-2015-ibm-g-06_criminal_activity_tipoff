from django.contrib import admin
from django.urls import path,re_path,include
from .views import *
urlpatterns = [
	# re_path('',include("login_V1.urls"),name="login"),
	# re_path('',include("main.urls"),name="main"),
	re_path('home/',home_page,name="home_page"),
	re_path('about_us/',about_us,name="about_us"),
	re_path('something/',something,name="something"),
	path('report/',report,name="report"),
	path('report/person/',report_person,name="report_person"),
	path('report/activity/',report_activity,name="report_activity"),

    # re_path('admin/', admin.site.urls ,name="my_admin"),
    
]