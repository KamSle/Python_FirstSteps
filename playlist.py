playlist = {'title':'mountain_trip',
            'author':'kam sle', 
            'songs':[{'title': 'song1','artist':['blue'],'duration':2.5},
                     {'title': 'song2','artist':['red','green'],'duration':4.45},
                     {'title': 'sosososos','artist':['blue','white'],'duration':2.1}
                     ]}
time = 0                     
for song in playlist['songs']:
    time += song['duration']
    print(time)
