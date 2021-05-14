# 1
# product(2,2) # 4
# product(2,-2) # -4
# '''

# # define product below:
# def product(x, y):
#     return x * y
# print(product(2,2))
# print(product(2,-2))

#2
# return_day(1) # "Sunday"
# return_day(2) # "Monday"
# return_day(3) # "Tuesday"
# return_day(4) # "Wednesday"
# return_day(5) # "Thursday"
# return_day(6) # "Friday"
# return_day(7) # "Saturday"
# return_day(41) # None
# '''

# def return_day(k):
#     days = ["Sunday","Monday","Tuesday", "Wednesday","Thursday","Friday","Saturday"]
#     if k in range(1,8):
#         return days[k-1]
#     return None

#3
# last_element([1,2,3]) # 3
# last_element([]) # None
# '''

# def last_element(num):
#     if len(num) != 0:
#        return num[-1]
#     return None

# ####
# def last_element(n):
#     if n:
#        return n[-1]
#     return None

#4
# number_compare(1,1) # "Numbers are equal"
# number_compare(1,0) # "First is greater"
# number_compare(2,4) # "Second is greater"
# '''

# def number_compare(x,y):
#     if x > y:
#         return "First is greater"
#     elif x < y:
#         return "Second is greater"
#     return "Numbers are equal"

#5
# single_letter_count("Hello World", "h") # 1
# single_letter_count("Hello World", "z") # 0
# single_letter_count("HelLo World", "l") # 3
# '''

# #define single_letter_count below:

# def single_letter_count(word,letter):
#     word = str(word.lower())
#     letter = str(letter.lower())
#     return word.count(letter)

# ###
# def single_letter_count(string,letter):
#     return string.lower().count(letter.lower())

#6
# multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
# '''

# # flesh out multiple_letter count:
# def multiple_letter_count(string):
#      return {k:string.count(k) for k,v in string}

#7
# list_manipulation([1,2,3], "remove", "end") # 3
# list_manipulation([1,2,3], "remove", "beginning") #  1
# list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
# list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
# '''

# def list_manipulation(l,a,b,c):
#     if a == "remove" and b == "end":
#         l.pop()
#         return l
#     elif a == "remove" and b == "begining":
#         l.pop(0)
#         return l
#     elif a == "add" and b == "end":
#         l.append(c)
#         return l
#     elif a == "add" and b == "begining":
#         l.insert(0,c)
#         return l
# print(list_manipulation([1,2,3],"add","end",33))
#

#8
# is_palindrome('testing') # False
# is_palindrome('tacocat') # True
# is_palindrome('hannah') # True
# is_palindrome('robert') # False
# is_palindrome('amanaplanacanalpanama') # True
# '''

# def is_palindrome(string):
#     x = len(string)
#     for a in range(0,x):
#       return string[a] == string[-a-1]
#
# tu dodatkowo wersja ze sliceing i opcja ze spacjami branymi pod uwagę
# def is_palindrome(string):
#     stripped = string.replace(" ", "")
#     return stripped == stripped[::-1]

#9
# frequency([1,2,3,4,4,4], 4) # 3
# frequency([True, False, True, True], False) # 1
# '''

# def frequency(list,value):
#     return list.count(value)
# print(frequency([0,3,4,5,3,7,3,8,2,3,1],3))

#10
# multiply_even_numbers([2,3,4,5,6]) # 48
# '''

# def multiply_even_numbers(list):
#     b = 1
#     for a in list:
#         if a%2 == 0:
#            b = a * b
#     return b
# print(multiply_even_numbers([1,2,3,5,6,7,9,4]))

#11
# capitalize("tim") # "Tim"
# capitalize("matt") # "Matt"
# '''

# def capitalize(string):
#     return string[:1].upper() + string[1:]
# print(capitalize("kamila"))
#

#12
# compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
#'''
# moja wersja
# def compact(list):
#     return [a for a in list if bool(a) == True]

# uroszczona bo z założenia warunek przyjmuje wartości prawdziwe
# def compact(l):
#     return [val for val in l if val]
#
# 13
# dwie table z ktorych otrzymamy tabele tylko z elementami z obu tabel
#
# def intersection(t1,t2):
#     return [a for a in t1 if a in t2]

# rozwiązanie z pomocą sets methods
# def intersection(t1,t2):
#     return [a for a in set(t1) & set(t2)]

# print(intersection([1,2,3,4,5],[6,2,8,5,1,9]))

#14
# def isEven(num):
#     return num % 2 == 0

# partition([1,2,3,4], isEven) # [[2,4],[1,3]]
# '''
### sposób bez dodatkowej funkcji ale z uzyciem if not w przypadku boolian
# def partition(list):
#       return [[a for a in list if a],[a for a in list if not a]]
# print(partition([2,0,3,None,"abc",""]))

# przyklad z dodatkową funkcja
# def ismytruth(k):
#       return bool(k)

# def partition(list, ismytruth):
#     return [[a for a in list if ismytruth(a)],[a for a in list if not ismytruth(a)]]

# print(partition([2,0,3,None,"abc",""], ismytruth))

#15
#zdefiniować funkcję która zwraca True jak jeden z argumentow jest = purple i False jak nie zawiera

# def contains_purple(*args):
#     if "purple" in args:
#         return True
#     return False


#16
# funkcja która dodaje z przodu (prefix) lub z tyłu (suffix) wartość klucza do stringu na indexie 0 lub zwraca sam string
# moje rozwiązanie z joinem

# def combine_words(string,**kwargs):
#     if "prefix" in kwargs:
#         return "".join([kwargs["prefix"],string])
#     elif "suffix"  in kwargs:
#         return ''.join([string,kwargs["suffix"]])
#     return string

# rozwiązanie z '+'

# def combine_words(string,**kwargs):
#     if "prefix" in kwargs:
#         return kwargs["prefix"] + string
#     elif "suffix"  in kwargs:
#         return string + kwargs["suffix"]
#     return string

# print(combine_words("work",prefix="home"))

#17
# def sum_even_values(*numb):
#     return sum([v for v in numb if v%2 == 0])
# print(sum_even_values(1,2,3,4,5))


#18
#function that adds only floats
# sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
# sum_floats(1,2,3,4,5) # 0
# '''

# def sum_floats(*numb):
#     return sum(num for num in numb if type(num) == float)
# print(sum_floats(2.3,4.5,2.33,5,6,7,'HI'))

#19
#function that accepts two strings return new string interwaven and ziped together

# def interleave(str1,str2):
#     # li = list(zip(str1,str2))
#     # lu = [''.join(char) for char in li]
#     # return ''.join(lu)
    # the way combine everything together
#     return ''.join(''.join(char) for char in zip(str1,str2))
# print(interleave("hl","eo"))

#20
# triple_and_filter([1,2,3,4]) # [12]
# triple_and_filter([6,8,10,12]) # [24,36]
# '''

# def triple_and_filter(li):
#     # return list(map(lambda i: i*3,filter(lambda l: l%4 == 0,li)))
#     # ## second way
#       return list(filter(lambda l: l%4 == 0,map(lambda l: l*3,li)))
# print(triple_and_filter([1,3,8,2,4]))

#21
# names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
# extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
# '''

# def extract_full_name(callya):
#       return list(map(lambda l: l["first"] + " "+ l["last"],callya))

# # another way
# #     def extract_full_name(l):
# #           return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))
# print(extract_full_name(names))

# 22
# Write a function called divide, which accepts two parameters (you can call them num1 and num2).
# The function should return the result of num1 divided by num2. If you do not pass the correct type of arguments to the function,
# it should return the string "Please provide two integers or floats". If you pass as the second argument a 0,
# Python will raise a ZeroDivisionError, so if this function is invoked with a 0 as the value of num2, return the string
# "Please do not divide by zero"

    # divide(4,2)  2
    # divide([],"1")  "Please provide two integers or floats"
    # divide(1,0)  "Please do not divide by zero"

# def divide(num1,num2):
#    try: num1/num2
#    except TypeError:
#        return "Please provide two integers or floats"
#    except ZeroDivisionError:
#        return "Please do not divide by zero"
#    return num1/num2
# print(divide(1,0))

# ### komunikat gdy używam returna w except
# # PS C:\Users\kamil\Desktop\python_time\kam_code> python first_functions.py
# # Please do not divide by zero
# # PS C:\Users\kamil\Desktop\python_time\kam_code>

# def divide(num1,num2):
#    try: num1/num2
#    except TypeError:
#        print("Please provide two integers or floats")
#    except ZeroDivisionError:
#        print("Please do not divide by zero")
#    return num1/num2
# print(divide(1,0))

### komunikat gdy używam printa w except
# PS C:\Users\kamil\Desktop\python_time\kam_code> python first_functions.py
# Please do not divide by zero
# Traceback (most recent call last):
#   File "first_functions.py", line 288, in <module>
#     print(divide(1,0))
#   File "first_functions.py", line 287, in divide
#     return num1/num2
# ZeroDivisionError: division by zero

#23
#zdefiniwać funkcje ktora zwraca prawde jak jednym z argumentow jest skrot klawisza uzywajac/importujac modulu wbudowanego 

## my way
# from keyword import iskeyword as isk
# def contains_keyword(*word):
#     return any([isk(w) for w in word])

# ## the other way
# from keyword import iskeyword as isk
# def contains_keyword(*args):
#     for item in args:
#         if isk(item): return True
#     return False

# print(contains_keyword('def','hahaha','chicken','alaska'))

#24

# from colorama import init
# from termcolor import colored
 
# # use colorama to make termcolor work on Windows too
# init()
 
# # then use termcolor for all colored text output
# print(colored('Hello, World!', 'green', 'on_red'))