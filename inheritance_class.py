# Inheritance Example Using Super()
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		# Animal.__init__(self,name, species)  # to call things that class Animal already has
		super().__init__(name, species="Cat") # Call init on parent class/ super instead of the class cat refers to - Animal / define species here as Cat for all the class so we don't have to write it ealier in init
		self.breed = breed
		self.toy = toy

	def play(self): 
		print(f"{self.name} plays with {self.toy}")



blue = Cat("Blue","Scottish Fold", "String")  // # here we don't write species becouse we already set it in super() for all Cat class 
blue.play()


# OUR "MODEL" FOR ANIMAL AND CAT
# Animal
# 	species
# 	name

# Cat
# 	species
# 	name
# 	breed
# 	favorite_toy