''' 
	User class attributes:
	- Name of User (string)
	- Dictionary of ingredients (dict[string] = int)
	- Dictionary of recipes (dict[string] = Recipe)

	User class methods:
	- Print recipes
	- Print ingredients
'''
class User:
	def __init__(self, _name):
		self.name = _name
		self.ingredients = {}
		self.recipes = {}
	def print_recipes(self):
		for k, v in self.recipes.iteritems():
			print k
			for i, n in v.ings.iteritems():
				print i, n
	def print_ingredients(self):
		for k, v in self.ingredients.iteritems():
			print k, v

'''
	Recipe class attributes:
	- Name of Recipe (string)
	- Dictionary of ingredients (dict[string] = int)
'''
class Recipe:
	def __init__(self, _name, _ings):
		self.name = _name
		self.ings = _ings






