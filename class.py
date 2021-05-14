# A User class with both instance attributes and instance methods and  class attributes and methods

## class attributes and methods are used far less often than instance attributes and instance methods.

class User:

## active_users = 0    # class attribute

	def __init__(self, first, last, age): ## our dunder method // anything with dunder method should go on the top of the class
		self.first = first
		self.last = last
		self.age = age
        User.active_users += 1  # any time a new user is created and it runs automatically This code is referring to the class attribute 
                                # or a class viariable. Active Users who we're adding one to it.

    # # def logout(self):
    # #     User.active_users -= 1
    # #     return f"{self.first} has logout"

    # defined instance methods
	def full_name(self):                      ## each instance of the User class made from this blueprint has its own full name method and that full
		return f"{self.first} {self.last}"    ## name is going to return its particular first name and its particular last name separated by space.

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):   
		self.age += 1
		return f"Happy {self.age}th, {self.first}"

	# def say_hi():
	#    print("Hi")                       # you need to have self in the prantasis even if you're not using it inside the method most
										   # of the time though pretty much 100 percent of the time you will be using it inside the method 
										   # until we talk about class methods.


# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)

# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))

# print(user2.initials())
# print(user1.initials())

# print(user2.is_senior())
# print(user1.age) #Print age before we update it
# print(user1.birthday()) #updates age
# print(user1.age) #Print new value of age

# # print(User.active_users)  # don't refer to the instances anymore just use you're not active users.
# # user1 = User("Joe", "Smith", 68)
# # user2 = User("Blanca", "Lopez", 41)
# # print(User.active_users)  ## we should see zero and then to after we create these two users and then two
# # print(user2.logout())
# # print(User.active_users) 



# 1 
# my way of define a class 
# Define Bank Account Below:
# class BankAccount:
#     def __init__(self, owner, balance = 0.0):
#         self.owner = owner
#         self.balance = balance

# 	def balance(self):
# 		return self.balance	
    
#     def deposit(self, number):
#         self.balance += number 
#         return self.balance
        
#     def withdraw(self, num):    
#         self.balance -= num
#         return self.balance

# ## the other way 
# class BankAccount:
 
#     def __init__(self, name):
#         self.owner = name
#         self.balance = 0.0
 
#     def getBalance(self):
#         return self.balance
 
#     def withdraw(self, amount):
#         self.balance -= amount
#         return self.balance
 
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance		

# 2 

# class Chicken:
#     total_eggs = 0 
#     def __init__(self, species, name, eggs = 0):
#         self.species = species
#         self.name = name
#         self.eggs = eggs
    
#     def lay_egg(self):
#         self.eggs += 1
#         Chicken.total_eggs += 1
#         return self.eggs


# # the other way 

# class Chicken:
#     total_eggs = 0
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#         self.eggs = 0
    
#     def lay_egg(self):
#         self.eggs += 1
#         Chicken.total_eggs += 1
#         return self.eggs

