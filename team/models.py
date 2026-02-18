# team/models.py

from django.db import models

class TeamMember(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='team_pics/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.full_name
