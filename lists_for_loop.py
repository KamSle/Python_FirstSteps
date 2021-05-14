# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# for s in sounds:
#     s
# result = print((sounds[0]+sounds[1]+sounds[3]+sounds[4]+sounds[5]+sounds[6]).upper())

# result = '' 
# for s in sounds:
#     result += s.upper()
# print(result)

# anser = []
# for let in ['Elie','Tim','Matt']:
#     anser.append(let[0])
# print(anser)    

# anser2 = []
# for val in [1,2,3,4,5,6]:
#     if val %2 == 0:
#         anser2.append(val)
# print(anser2)      

# answer = [num for num in [1,2,3,4] if num in [3,4,5,6]]
# print(answer)

# answer = []
# for num in [1,2,3,4]:
#     if num in [3,4,5,6]:
#         answer.append(num)
# print(answer)    

# answer2 = [let[::-1].lower() for let in ['Elie','Tim','Matt']]
# print(answer2)
# print(['Elie','Tim','Matt'][::-1])


# answer2 = []
# for let in ['Elie','Tim','Matt']:
#     answer2.append(let[::-1].lower())
# print(answer2)

# answer = [let for let in "amazing" if let not in ["a","e","i","o","u"]]
# print(answer)

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# total_donations = 0
# for donations in donations.values():
#     total_donations += donations
#     print(total_donations)

# total_donations = sum(donations for donations in donations.values())
# print(total_donations)

# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
if food in bakery_stock:
    print(f'{bakery_stock.get(food)} left')
else:
    print("We don't make that")
      


   