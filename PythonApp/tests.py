from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from django.utils import timezone
from .views import getResources, getMeetings, meetingDetails
from django.urls import reverse
# class Meeting_test(TestCase):
#     def create_meeting(self, title="test title", location="test location", agenda="test agenda"):
#         return Meeting.objects.create(title=title, date=timezone.now(), time=timezone.now(), location=location, agenda=agenda )

#     def test_meeting_creation(self):
#         a = self.create_meeting()
#         self.assertTrue(isinstance(a, Meeting))
    
#     def test_each_key(self):
#         a = self.create_meeting()
#         self.assertEqual("test title", a.title)
#         self.assertEqual("test location", a.location)
#         self.assertEqual("test agenda", a.agenda)



class MeetingMinutes_test(TestCase):
    def setup(self):
        meeting = Meeting(title='bla bla bla')
        meetingMinutes = MeetingMinutes(meeting = meeting, attendance ='test attendance', minutesText=60)
        return meetingMinutes

    def test_string(self):
        metmin = self.setup()
        self.assertEqual(str(metmin), metmin.attendance)

    def test_minutes(self):
        metmin = self.setup()
        self.assertEqual(metmin.minutesText, 60)

    # TEST FOR FOREING KEY
    def test_meeting(self):
        metmin = self.setup()
        self.assertEqual(str(metmin.meeting), 'bla bla bla')



# TESTING FOR VIEWS_______________________________________________________________________
class getResources_test(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)

class getMeetings_test(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)


class meetingDetails_test(TestCase):
    def setUp(self):
        self.meeting = Meeting.objects.create(title='blabla', date=timezone.now(), time=timezone.now(), location='locationtest', agenda='agendatest')

    def test_meeting_detail_success(self):
        response = self.client.get(reverse('meetingdetails', args=(self.meeting.id,)))
        # Assert that self.post is actually returned by the post_detail view
        self.assertEqual(response.status_code, 200)
#__________________________________________________________________________________________

    # meeting = models.ForeignKey(Meeting, on_delete = models.DO_NOTHING)
    # attendance = models.CharField(max_length=255)
    # minutesText = models.CharField(max_length=255)

    #  title = models.CharField(max_length=255)
    # date = models.DateField()
    # time = models.TimeField()
    # location = models.CharField(max_length=255)
    # agenda = models.CharField(max_length=255)


