# from colorama import init
# from termcolor import colored
# # # use colorama to make termcolor work on Windows too
# init()
 
# # # then use termcolor for all colored text output
# print(colored('Hello, World!', 'green', 'on_red'))


from colorama import init
from termcolor import colored
init()
from pyfiglet import figlet_format

clr = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

message = input("What message do you want to print: ")
colorr = input("What colour: ")

if colorr not in clr:
   colorr = "magenta"
print(colored(figlet_format(message),color=colorr))

