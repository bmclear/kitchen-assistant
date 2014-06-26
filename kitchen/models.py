from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=128, unique=True)
    amount = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to="profile_images", blank=True)

    def __unicode__(self):
        return self.user.username
