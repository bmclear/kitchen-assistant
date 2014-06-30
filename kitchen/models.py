from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to="profile_images", blank=True)

    def __unicode__(self):
        return self.user.username
    
class UserKitchen(models.Model):
    user = models.ForeignKey(UserProfile)
    
    def __unicode__(self):
        return self.user.username + "'s kitchen"

class UserIngredient(models.Model):
    kitchen = models.ForeignKey(UserKitchen)
    name = models.CharField(max_length=128, unique=True)
    amount = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class UserRecipe(models.Model):
    kitchen = models.ForeignKey(UserKitchen)
    name = models.CharField(max_length=128)
    instructions = models.TextField()

    def __unicode__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=128)
    instructions = models.TextField()

    def __unicode__(self):
        return self.name
