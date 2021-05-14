names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]
# print(min(names))
# print(max(names))
# print(min(len(name) for name in names))
# print(max(len(name) for name in names))
# print(max(names, key=lambda name: len(name)))


# finds the minimum length of a name in names
min(len(name) for name in names) # 3

# find the longest name itself
max(names, key=lambda n:len(n)) #Ollivander

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
min(songs, key=lambda s: s['playcount']) #{"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title'] #YMCA