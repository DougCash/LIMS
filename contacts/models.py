from django.db import models

class Locations(models.Model):
    location_name = models.CharField(max_length=50)
    location_timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "locations"
        ordering = ['location_name']


class Contacts(models.Model):
    contact_first_name = models.CharField(max_length=50)
    contact_last_name = models.CharField(max_length=50)
    contact_email = models.EmailField()
    contact_location = models.ForeignKey(Locations, on_delete='SET_DEFAULT', default="")
    contact_notes = models.CharField(max_length=200)
    contact_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contacts"
        ordering = ['contact_last_name']

