from django.contrib import admin
from kitchen.models import *

# Register your models here.
admin.site.register(UserProfile)
#admin.site.register(UserKitchen)
admin.site.register(UserIngredient)
admin.site.register(UserRecipe)
admin.site.register(Recipe)
admin.site.register(Ingredient)
