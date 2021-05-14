# num_list = [1,2,3,4,5]
# first = {num:('even' if num %2 == 0 else 'odd') for num in num_list}
# print(first)
# second = {num:num**2 for num in num_list}
# print(second)
# lit_list = 'ABCDE'
# third = {(lit_list[i].lower():num_list[i] for i in range(0,len(lit_list))}
# print(third)

################################################
# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# # make sure your solution is assigned to the answer variable so the tests can work!
# answer = {list1[i]:list2[i] for i in range(3)}
# print(answer)

###################################################
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
# answer = {k:v for k,v in person}
# print(answer)
# anser2 = dict(person)
# print(anser2)

########################
# answer = {}.fromkeys(['a','e','i','o','u'],0)
# answer2 = {k:0 for k in ['a','e','i','o','u']}
# print(answer)
# print(answer2)

#### with string ### answer = {char:0 for char in 'aeiou'}

#########################

# answer = {i: chr(i) for i in range(65,91)}
# print(answer)

def generate_evens():
    y = []
    x = 2
    while x in range(1,50):
        y.append(x)
        x+= 2
    return y
print(generate_evens())    
