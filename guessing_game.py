from random import randint

random_number = randint(1, 10)
while True:
      number = input("Pick a number from 1 to 10: ")
      number = int(number)
      if number > random_number:   
         print("Too high! Pick once more: ")
      elif number < random_number:
         print ("Too low! Pick once more: ")  
      else:
         print("You won!")     
         play_again = input("Do you want to play again? y/n ")
         if play_again == "y":
            random_number = randint(1, 10)
         else: 
            print("Thank you for the game!")
            break 