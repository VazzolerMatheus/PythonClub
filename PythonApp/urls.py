
from django.urls import path
from . import views

urlpatterns=[


			#index is a function inside the view.py file
   path('', views.index, name='index'),

   path('getResources/', views.getResources, name='resources'),

   path('getMeetings/', views.getMeetings, name='meetings'),

   path('meetingdetails/<int:id>', views.meetingDetails, name='meetingdetails')
  
]




