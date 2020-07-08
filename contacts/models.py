from django.db import models

class Contacts(models.Model):
    contact_first_name = models.CharField(max_length=50)
    contact_last_name = models.CharField(max_length=50)
    contact_email = models.EmailField()
    contact_location = models.CharField(max_length=50)
    contact_notes = models.CharField(max_length=200)

    class Meta:
        db_table = "contacts"
