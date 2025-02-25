from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='rooms_owned')

    def __str__(self):
        return self.name


class Marker(models.Model):
    title = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='markers')
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='markers_created')

    def __str__(self):
        return self.title


class Meetup(models.Model):
    marker = models.ForeignKey(Marker, on_delete=models.CASCADE, related_name='meetups')
    visit_date = models.DateTimeField()
    attendees = models.ManyToManyField('users.User', related_name='meetups_attended')

    def __str__(self):
        return f"Meetup at {self.marker.title} on {self.visit_date}"


class MeetupPhoto(models.Model):
    marker_visit = models.ForeignKey(Meetup, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='rooms/meetup/photos/')

    def __str__(self):
        return f"Photo for meetup at {self.marker_visit.marker.title} on {self.marker_visit.visit_date}"
