from django.contrib import admin
from .models import Room, Marker, Meetup, MeetupPhoto


admin.site.register(Room)
admin.site.register(Marker)
admin.site.register(Meetup)
admin.site.register(MeetupPhoto)
