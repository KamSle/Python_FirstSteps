print("How many kilometers did you cycle today?")
km = input()
mile = float(km)/1.609344
mile = round(mile,2)
print(f"You ride {mile}")