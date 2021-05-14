# for x in range(1,8):
#     print(x)

# for letter in "cooffe":
#   print(letter)

# for letter in "cooffe":
#   print(letter * 10)

# x = 0 
# for a in range(11, 21, 2):
#     x += a
#     print(x)

# pętla z wartością od użytkownika

# times = input("How many times do I've to tell you to clean your hands: ")
# times = int(times)
# for b in range (times):
#     print("Clean your hands, please!")

# pętla spełniająca warunki dla wskazanych wartości parzystych nieparzystych i wybranych 4 i 14

# for c in range(1,21):
#    if c == 4 or c == 14:
#     print(f"{c} is UNLUCKY!")
#    elif c%2 != 0 and c != 4 and c != 14:
#     print(f"{c} is even!")
#    else:
#     print(f"{c} is odd!")      
   
for c in range (1,21):
   if c == 4 or c == 14:
       state = "unlucky"
   elif c%2 != 0 and c != 4 and c != 14:
       state = "even"
   else:
       state = "odd"
   print(f"{c} is {state}!")