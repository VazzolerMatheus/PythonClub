from django.contrib import admin
from .models import Event, Meeting, MeetingMinutes, Resource


admin.site.register(Resource)
admin.site.register(Event)
admin.site.register(MeetingMinutes)
admin.site.register(Meeting)
