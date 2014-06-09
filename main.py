'''
Brandon McLear, Kirk Smith, and Courtney Lang
Kitchen Assistant
'''

import sys

''' Import the User and Recipe classes '''
import sub
User = sub.User
Recipe = sub.Recipe

''' Main has user "log in", parses input text file for commands, 
and attempts to carry out those commands '''
def main():
	''' Get username '''
	usr_name = raw_input("What is your username? ")
	print
	usr = User(usr_name)

	''' Open text file and begin parsing '''
	input_file = open(sys.argv[1])
	for line in input_file:
		''' New recipe; read the ingredients, make a new Recipe object,
		and store the new recipe in the User's kitchen '''
		if line[0] == 'r':
			line = line.split()
			rec_name = line[1]
			r_ings = {}
			for line in input_file:
				if line[0] == '0':
					break
				line = line.split()
				r_ings[line[1]] = line[0]
			new_rec = Recipe(rec_name, r_ings)
			usr.recipes[rec_name] = new_rec

		''' Add ingredients; read the ingredients and put them in
		the User's kitchen '''
		if line[0] == 'a':
			for line in input_file:
				if line[0] == '0':
					break
				line = line.split()
				usr.ingredients[line[1]] = line[0]
		
		''' Print a recipe; read which Recipe, find it, print it '''
		'''to do: what if recipe doesn't exist? '''
		if line[0] == 'p':
			line = line.split()
			if line[1] in usr.recipes.keys():
				this_rec = usr.recipes[line[1]]
				print this_rec.name
				for k, v in this_rec.ings.iteritems():
					print k, v
				print
			else:
				print "No recipe for ", line[1]

		''' Make a recipe; take in a Recipe, check if the User has it
		If not, print out that the Recipe does not exist
		If so, check if the User has enough ingredients
		If not, print out what the User needs to make the Recipe
		If so, subtract the proper ingredient amounts from the
		kitchen and tell the user that the recipe has been made '''
		if line[0] == 'm':
			line = line.split()
			if line[1] in usr.recipes.keys():
				this_rec = usr.recipes[line[1]]
				new_amts = {}
				need_amts = {}
				can_make = True
				for i, n in this_rec.ings.iteritems():
					if int(usr.ingredients[i]) < int(n):
						need_amts[i] = int(n) - int(usr.ingredients[i])
						can_make = False
						continue
					new_amts[i] = int(usr.ingredients[i]) - int(n)
				if can_make:
					for ing, amt in new_amts.iteritems():
						usr.ingredients[ing] = amt
					print "Made", line[1]
					print
				else:
					print "Cannot make recipe, need:"
					for ing, amt in need_amts.iteritems():
						print ing, amt
					print
			else:
				print "No recipe for", line[1]
				print

		''' Print kitchen contents; print all of 
		the Ingredients in the kitchen '''
		if line[0] == 'k':
			print "In the kitchen:"
			usr.print_ingredients()
			print

if __name__ == "__main__":
	main()









