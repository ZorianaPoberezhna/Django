from django.db import models
from django.contrib.auth.models import User
from destinations.models import Destination

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    start_data = models.DateField()
    end_data = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.destination.name} ({self.start_data} to {self.end_data})"

