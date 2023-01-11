from django.contrib import admin
from django.urls import path,re_path,include
from .views import *
urlpatterns = [
	# re_path('',include("login_V1.urls"),name="login"),
	# re_path('',include("main.urls"),name="main"),
	path('home/',home_page,name="home_page"),
	path('about_us/',about_us_function,name="about_us_name"),
	path('something/',something,name="something"),
	path('report/',report,name="report"),
	path('report/person/',report_person,name="report_person"),
	path('report/activity/',report_activity,name="report_activity"),
	path('my-admin/home/',admin_home,name="admin_home"),
    # re_path('admin/', admin.site.urls ,name="my_admin"),
]