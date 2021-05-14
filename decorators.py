# def be_polite(fn):
#     def wrapper():  # without argument
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper

# # greet = be_polite(greet)   # instaed we use decorator syntax
# @be_polite
# def greet():
#     print("My name is Colt.")

# # rage = be_polite(rage)    # Instead we use decorator syntax
# @be_polite
# def rage():
# 	print("I HATE YOU!")

# greet()
# rage()

# # This version only accepts one argument
# # def shout(fn): 
# #     def wrapper(name):    # with one argument # fn order doesnt work here
# #         return fn(name).upper()
# #     return wrapper

# # This version works with any number of args
# def shout(fn):
#     def wrapper(*args, **kwargs):  # with any number of arguments
#         return fn(*args, **kwargs).upper()
#     return wrapper

# @shout
# def greet(name):
#     return f"Hi, I'm {name}."

# @shout
# def order(main, side):  # two arguments need to call shout on at least two arguments
#     return f"Hi, I'd like the {main}, with a side of {side}, please."

# @shout
# def lol():
# 	return "lol"

# print(greet("todd"))
# print(order(side="burger", main="fries"))
# print(lol())


###



# do_nothing(1, 2, 3,a="hi",b="bye")

# # Should print (on two lines):
# # Here are the args: (1, 2, 3)
# # Here are the kwargs: {"a": "hi", "b": "bye"}
# '''

# from functools import wraps

# def show_args(fn):
#     @wraps(fn)
#     def wrapper(*args,**kwargs):
#         print(f'Here are the args: {args}')
#         print(f'Here are the kwargs: {kwargs}')
#         return fn(*args,**kwargs)
#     return wrapper

# @show_args
# def do_nothing(*args, **kwargs):
#     pass
       
# print(do_nothing(1, 2, 3,a="hi",b="bye"))    

####

# @double_return 
# def add(x, y):
#     return x + y
    
# add(1, 2) # [3, 3]

# @double_return
# def greet(name):
#     return "Hi, I'm " + name

# greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
# '''

# from functools import wraps

# def double_return(fn):
#     @wraps(fn)
#     def wrapper(*args,**kwargs):
#         return [fn(*args,**kwargs),fn(*args,**kwargs)]
#     return wrapper

# @double_return
# def add(a,b):
#     return a+b
# @double_return
# def greet(name):
#     return "Hi, I'm " + name    

# print(greet("Colt"))
# print(add(1,2))    

####

# '''
# @ensure_fewer_than_three_args
# def add_all(*nums):
#     return sum(nums)

# add_all() # 0
# add_all(1) # 1
# add_all(1,2) # 3
# add_all(1,2,3) # "Too many arguments!"
# add_all(1,2,3,4,5,6) # "Too many arguments!"
# '''

# from functools import wraps

# def ensure_fewer_than_three_args(fn):
#     @wraps(fn)
#     def wrapper(*args,**kwargs):
#         if len(args)<=2:    
#             return fn(*args,**kwargs)
#         return "Too many arguments!!"    
#     return wrapper

# @ensure_fewer_than_three_args
# def add_all(*nums):
#     return sum(nums)

# print(add_all(1,2))    
# print(add_all(1,2,3))    


#####

# '''
# @only_ints 
# def add(x, y):
#     return x + y
    
# add(1, 2) # 3
# add("1", "2") # "Please only invoke with integers."
# '''

# from functools import wraps

# def only_ints(fn):
#     @wraps(fn)
#     def wrapper(*args,**kwargs):
#         if any([arg for arg in args if type(arg) != int]):
#             return "Please only invoke with integers."
#         return fn(*args,**kwargs)
#     return wrapper
  

# @only_ints
# def add(a,b):
#     return a+b       

# print(add(1,2))
# print(add(1,"a"))

#####



# show_secrets(role="admin") # "Shh! Don't tell anybody!"
# show_secrets(role="nobody") # "Unauthorized"
# show_secrets(a="b") # "Unauthorized"


# from functools import wraps

# def ensure_authorized(fn):
#     @wraps(fn)
#     def wrapper(*args,**kwargs):
#         if "role" in kwargs:
#             if "admin" in kwargs.values():
#                 return fn(*args,**kwargs)
#         return "Unauthorized"       
#     return wrapper    

# # other solution

# # from functools import wraps
 
# # def ensure_authorized(fn):
# #     @wraps(fn)
# #     def wrapper(*args, **kwargs):
# #         if kwargs.get("role") == "admin":
# #             return fn(*args, **kwargs)
# #         return "Unauthorized"
# #     return wrapper

# @ensure_authorized
# def show_secrets(*args, **kwargs):
#     return "Shh! Don't tell anybody!"    

# print(show_secrets(role="admin"))
# print(show_secrets(a="b"))

###

# @delay(3)
# def say_hi():
#     return "hi"

# say_hi()
# # should print the message "Waiting 3s before running say_hi" to the console
# # should then wait 3 seconds
# # finally, should invoke say_hi and return "hi"
# '''

# from functools import wraps
# from time import sleep

# def delay():