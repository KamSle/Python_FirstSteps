# MANUALNA WERSJA GRY KAMIEŃ PAPIER NOŻYCE

# print("..rock..\n..paper..\n..sisors..")
# x = input("(Enter Player 1's choice): ")
# y = input("(Enter Player 2's choice): ")
# print("SHOOT!")
# if (x == 'rock' and y == 'sisors') or (x == 'sisors' and y == 'paper') or (x == 'paper' and y == 'rock'):
#    print("Player 1 WINS!")
# elif (y == 'rock' and x == 'sisors') or (y == 'sisors' and x == 'paper') or (y == 'paper' and x == 'rock'):
#    print("Player 2 WINS!")
# elif x == y : 
#    print("It is a tie!")    
# else:
#    print("Wrong choice!")    
    
# KOMPUTEROWA WERSJA GRY KAMIEŃ PAPIER NOŻYCE 

# import random
# print("..rock..\n..paper..\n..sissors..")
# x = input("(Enter Player 1's choice): ")
# z = random.randint(0, 2)
# if z == 0:
#     y = "rock" 
    
# elif z == 1:
#     y = "paper" 
    
# else:
#     y = "sissors" 
# print (f"Computer choice: {y}")     
# print("SHOOT!")
# if (x == 'rock' and y == 'sissors') or (x == 'sissors' and y == 'paper') or (x == 'paper' and y == 'rock'):
#     print("Player 1 WINS!")
# elif (y == 'rock' and x == 'sissors') or (y == 'sissors' and x == 'paper') or (y == 'paper' and x == 'rock'):
#     print("Computer WINS!")
# elif x == y : 
#     print("It is a tie!")    
# else:
#     print("Wrong choice!")   



# rożnica w korzystaniu z random/randint

# from random import randint
# print("..rock..\n..paper..\n..sissors..")
# x = input("(Enter Player 1's choice): ").lower()
# z = randint(0, 2)
# if z == 0:
#     y = "rock" 
    
# elif z == 1:
#     y = "paper" 
    
# else:
#     y = "sissors" 
# print (f"Computer choice: {y}")     
# print("SHOOT!")
# if (x == 'rock' and y == 'sissors') or (x == 'sissors' and y == 'paper') or (x == 'paper' and y == 'rock'):
#     print("Player 1 WINS!")
# elif (y == 'rock' and x == 'sissors') or (y == 'sissors' and x == 'paper') or (y == 'paper' and x == 'rock'):
#     print("Computer WINS!")
# elif x == y : 
#     print("It is a tie!")    
# else:
#     print("Wrong choice!")      

# GGGGGGGgra z ulepszeniem bo z wynikami

# from random import randint
# player_wins = 0
# computer_wins = 0
# games = 3
# while player_wins < games and computer_wins < games:
#   print("..rock..\n..paper..\n..sissors..")
#   x = input("(Enter Player 1's choice): ").lower()
#   if x == "quit" or x == "q":
#     break
#   z = randint(0, 2)
#   if z == 0:
#     y = "rock" 
#   elif z == 1:
#     y = "paper" 
#   else:
#     y = "sissors" 
#   print (f"Computer choice: {y}")     
#   print("Make a choose!")
#   if (x == 'rock' and y == 'sissors') or (x == 'sissors' and y == 'paper') or (x == 'paper' and y == 'rock'):
#     print("Player WINS!") 
#     player_wins += 1
#     print(f"Player score {player_wins} Computer score {computer_wins}")
#   elif (y == 'rock' and x == 'sissors') or (y == 'sissors' and x == 'paper') or (y == 'paper' and x == 'rock'):
#     print("Computer WINS!")
#     computer_wins += 1
#     print(f"Player score {player_wins} Computer score {computer_wins}") 
#   elif x == y : 
#     print("It is a tie!") 
#     print(f"Player score {player_wins} Computer score {computer_wins}")     
#   else:
#     print("Wrong choice!")     
# print(f"Final score... Player {player_wins} : Computer {computer_wins} ")        
# if player_wins > computer_wins:
#     print("You win! Hi five!")
# elif player_wins == computer_wins:
#     print("It's a TIE")    
# else:
#     print("Computer wins! Good luck next time!")

# wersja gdzie gracz wybiera ile razy chce grac

from random import randint
player_wins = 0
computer_wins = 0
i = 0
games = int(input("How many games do you want to play?: "))
while i < games:
  print("..rock..\n..paper..\n..sissors..")
  x = input("(Enter Player's choice or quit): ").lower()
  if x == "quit" or x == "q":
    break
  z = randint(0, 2)
  if z == 0:
    y = "rock" 
  elif z == 1:
    y = "paper" 
  else:
    y = "sissors" 
  print (f"Computer choice: {y}")     
  if (x == 'rock' and y == 'sissors') or (x == 'sissors' and y == 'paper') or (x == 'paper' and y == 'rock'):
    print("Player WINS!") 
    player_wins += 1
    print(f"Player score {player_wins} Computer score {computer_wins}")
  elif (y == 'rock' and x == 'sissors') or (y == 'sissors' and x == 'paper') or (y == 'paper' and x == 'rock'):
    print("Computer WINS!")
    computer_wins += 1
    print(f"Player score {player_wins} Computer score {computer_wins}") 
  elif x == y : 
    print("It is a tie!") 
    print(f"Player score {player_wins} Computer score {computer_wins}")     
  else:
    print("Wrong choice!")
  i += 1       
print(f"Final score... Player {player_wins} : Computer {computer_wins} ")        
if player_wins > computer_wins:
    print("You win! Hi five!")
elif player_wins == computer_wins:
    print("It's a TIE")    
else:
    print("Computer wins! Good luck next time!")




