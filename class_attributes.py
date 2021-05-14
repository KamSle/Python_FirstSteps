# Another class with a class attribute, used for validation purposes
class Pet:
	allowed = ['cat', 'dog', 'fish', 'rat'] # class attribute

	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species

	def set_species(self,species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
print(Pet.allowed)  #['cat', 'dog', 'fish', 'rat']
print(cat.allowed)  #['cat', 'dog', 'fish', 'rat']
print(dog.allowed)  #['cat', 'dog', 'fish', 'rat']
print(id(Pet.allowed))  # 2616787603840
print(id(dog.allowed))  # 2616787603840
print(id(cat.allowed))  # 2616787603840

## this is that cat that allowed dog that allowed pet dog allowed all point they all refer to the exact same pet class attribute

# when we set cat up allowed to Tiger and Bear we overrode this arrow we kind of severed this connection and we gave cat 
# its own version of allowed but dog is still pointing to the pet class.

## class attributes exist on the class you can use them for things like keeping track of analytics or you know a count of how many
# instances have been created.
## However if we were only using this(allowed) once when you know a new pet was initialized it would be better to not make it 
# a class attribute just put it in this method and it goes away after the method is done just like any other method or function we've defined.


