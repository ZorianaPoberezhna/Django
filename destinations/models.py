from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    lost_season = models.CharField(max_length=50)

    def __str__(self):
        return self.name