
from django.urls import path
from . import views

urlpatterns=[

   #index is a function inside the view.py file
   path('', views.index, name='index'),

   path('getResources/', views.getResources, name='resources'),

   path('getMeetings/', views.getMeetings, name='meetings'),

   path('meetingdetails/<int:id>/', views.meetingDetails, name='meetingdetails'),

   #url for the forms NewResouce
   path('newresource/', views.newResource, name="newresource"),


   # login and logou messages in html
   path('loginmessage/', views.loginmessage, name='loginmessage'),
   
   path('logoutmessage/', views.logoutmessage, name='logoutmessage'),

  	
  	#First atribute on Path("ex/") is just the directory that will appear on the navigation bar

  	# By assigning the url a name you can use this value as a reference in view methods and templates, 
	# which means any future changes made to the url regular expression, automatically update all url definitions 
	# in view methods and templates.

]



