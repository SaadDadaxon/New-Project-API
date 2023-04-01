from django.db import models
from account.models import Profile


class About(models.Model):
    full_name = models.CharField(max_length=228)
    position = models.CharField(max_length=228)
    avatar = models.ImageField(upload_to="about/", null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.full_name

