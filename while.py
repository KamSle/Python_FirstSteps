# wyświetlamy emotkę odpowiednią ilość razy za pomocą pętli for i while

# while

# p = 1
# while p < 11:
#  print("\U0001f600" * p)
#  p += 1

# for

# for p in range(1,11):
#  print("\U0001f600" * p)

# petla while działa do momentu az wpisze Yes we can

message = input("Can we play tutu together? ")
while message != "Yes we can":   
 message = input(f"{message}\n")
print("superr") 