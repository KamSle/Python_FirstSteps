# Lame function that returns a list of beats.  
# Only runs 100 times
# def current_beat():
# 	max = 100
# 	nums = (1,2,3,4)
# 	i = 0
# 	result = []
# 	while len(result) < max:
# 		if i >= len(nums): i = 0
# 		result.append(nums[i])
# 		i += 1
# 	return result

# Infinite Generator - returns one beat a time, no list used!
# def current_beat():
# 	nums = (1,2,3,4)
# 	i = 0
# 	while True:
# 		if i >= len(nums): i = 0
# 		yield nums[i]
# 		i += 1

## exercise song generator

# def make_song(times = 99,drink = 'soda'):
#     t = times
#     for t in range(times,-1,-1):
#         if  t>1:
#             yield f"{t} bottels of {drink} on the wall"
#         elif t == 1:
#             yield f"Only 1 bottle of the {drink} left"
#         else:
#             yield f"No more {drink}"    
#     t -= 1
# new_song = make_song(3,'cola')
# old_song = make_song()
# print(next(old_song))
# print(next(new_song))
# print(next(new_song))
# print(next(new_song))
# print(next(new_song))


### fibonacci in function vs generator function
# def fib_list(max):
# 	a,b = 0,1
# 	num=[]
# 	while len(num)<max:
# 		num.append(b)
# 		a,b = b,a+b
# 	return num	

# print(fib_list(8))

# def fib_gen(max):
# 	x=0
# 	y=1
# 	count=0
# 	while count<max:
# 		x,y=y,x+y
# 		yield x
# 		count +=1
# for n in fib_gen(10):
#     print(n)		


#### 

# evens = get_multiples(2, 3)
# next(evens) # 2
# next(evens) # 4
# next(evens) # 6
# next(evens) # StopIteration

# default_multiples = get_multiples()
# list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# '''

# def get_multiples(number = 1, count =10):
# 	i=1
# 	s = number
# 	while i <= count:
# 		yield s*i
# 		i +=1
# for n in get_multiples(2,3):
#     print(n)	

# get_mu= get_multiples()	
# print(list(get_mu))

# # other way solution
# def get_multiples(num=1, count=10):
#     next_num = num
#     while count > 0:
#         yield next_num
#         count -= 1
#         next_num += num

######

# '''
# sevens = get_unlimited_multiples(7)
# [next(sevens) for i in range(15)] 
# # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

# ones = get_unlimited_multiples()
# [next(ones) for i in range(20)]
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# '''

# def get_unlimited_multiples(num):
# 	i = 1
# 	while True:
# 		s = num*i
# 		yield s
# 		i+=1
# g=get_unlimited_multiples(6)		
# num_unlimited = [next(g) for i in range(15)]
# print(num_unlimited)	

# # other way solution

# def get_unlimited_multiples(num=1):
#     next_num = num
#     while True:
#         yield next_num
#         next_num += num