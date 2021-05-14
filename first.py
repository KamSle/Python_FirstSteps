# print("hello")


# #####
# things = dict(name = 'Matt', age = 18, high = 1.72, language = 'polish', country = 'Japan', city = 'Tokyo', man = True)
# #print(things.values())
# print(things.keys())
# print(things.items())


## 
# class Train:
#     def __init__(self, num_car):
#         self.num_car = num_car

#     def __repr__(self):
#         return "{} car train".format(self.num_car)
        
#     def __len__(self):
#         return self.num_car
# cart=Train(4)
# print(cart)
# print(len(cart))

##
# def my_for(iterable, fun):
#     iterator = iter(iterable)
#     while True:
#         try:
#             thing=next(iterator)
#         except StopIteration:
#             break
#         else:
#             fun(thing)
# def square(x):
#     print(x*x)             
# my_for("loki",print)   
# my_for([1,2,3,4,5],square)  

## zadanie 
# kombucha_song = make_song(5, "kombucha")
# next(kombucha_song) # '5 bottles of kombucha on the wall.'
# next(kombucha_song) # '4 bottles of kombucha on the wall.'
# next(kombucha_song) # '3 bottles of kombucha on the wall.'
# next(kombucha_song) # '2 bottles of kombucha on the wall.'
# next(kombucha_song) # 'Only 1 bottle of kombucha left!'
# next(kombucha_song) # 'No more kombucha!'
# next(kombucha_song) # StopIteration

# default_song = make_song()
# next(default_song) # '99 bottles of soda on the wall.'
# '''

def make_song(times = 99,drink = 'soda'):
    t = times
    for t in range(times,-1,-1):
        if  t>1:
            yield f"{t} bottels of {drink} on the wall"
        elif t == 1:
            yield f"Only 1 bottle of the {drink} left"
        else:
            yield f"No more {drink}"    
    t -= 1
new_song = make_song(3,'cola')
old_song = make_song()
print(next(old_song))
print(next(new_song))
print(next(new_song))
print(next(new_song))
print(next(new_song))


