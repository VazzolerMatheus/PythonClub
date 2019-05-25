from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting, MeetingMinutes
from .forms import ResourceForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request) :
   return render(request, 'PythonApp/index.html')


def getResources(request):

	resources_list = Resource.objects.all()

	return render(request, 'PythonApp/resources.html', {'resources_list' : resources_list})

def getMeetings(request):

				# NAME_OF_THE_TABLE.objects.all()
	meetings_list = Meeting.objects.all()

	return render(request, 'PythonApp/meetings.html', {'meetings_list' : meetings_list})

def meetingDetails(request, id):

	#setting meeting = Meeting table
	meeting = get_object_or_404(Meeting, pk=id)


	#setting details = MeetingMinutes table
	details = MeetingMinutes.objects.filter(meeting = id)

	context = {

		'meeting' : meeting,
		'details' :  details,
	}

	return render(request, 'PythonApp/meetingdetails.html', context= context)



# Views for FORMS _______ Start here __________

@login_required
def newResource(request):

	#create instance of class ResourceForm named 'form'
	form = ResourceForm

	if request.method == 'POST':
		form = ResourceForm(request.POST)

		if form.is_valid():
			post=form.save(commit=True)
			post.save()
			form=ResourceForm()
	else:
		form=ResourceForm()


# Views for FORMS _______ Ends here __________



	return render(request, 'PythonApp/newresource.html', {'form' : form})

def loginmessage(request):
	return render(request, 'PythonApp/login.html')

def logoutmessage(request):
	return render(request, 'PythonApp/logout.html')



