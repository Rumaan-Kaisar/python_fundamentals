
# Courses: colt_py_bootcamps    133


""" How to Sort the Dictionary by Value in Ascending or Descending Order
Remember the sorted() method accepts a third value called reverse.
    reverse with a value of True will arrange the sorted dictionary in descending order. """

footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(sorted_footballers_by_goals)

print(converted_dict)

# Output: {'Pele': 150, 'Ronaldo': 132, 'Messi': 125, 'Eusebio': 120, 'Cruyff': 104}
# You can see the output is reversed because we passed reverse=True to the sorted() method.

# If you don’t set reverse at all or you set its value to false, the dictionary will be arranged in ascending order. That’s the default.




# Data modeling using 'list' and 'dictionary'
# spotify playlist project

playlist = {
    'title': 'Ho Ho Ho !!!',
    'songs': [
        {'song_title': 'serious thing', 'artists': ['Bohoma'], 'duration': 2.5},
        {'song_title': 'nothing_else', 'artists': ['Bohoma', 'Paranoya'], 'duration': 6.5},
        {'song_title': 'WTF', 'artists': ['Aaah ha', 'kitty'], 'duration': 4.5},
        {'song_title': 'MeowMeow', 'artists': ['Garfield'], 'duration': 2.0}
    ]
}

total_length = 0
for song in playlist['songs']:
    # the loop variable "song" represents a single dictionary now
    print(song['song_title'])
    total_length += song['duration']

print(f"Total length is {total_length}")

# Note: this data is more similar to API generated data, 
    # EG: spotify API returns nested dictionaries with various parameters


# python py_ch2_3_4_dict_list_spotfy.py


# -------------|    Instructor version    |-------------
playlist = {
	'title': 'patagonia bus', 
	'author': 'colt steele', 
	'songs': [
		{'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
		{'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
		{'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
	]
}

total_length = 0
for song in playlist['songs']:
	total_length += song['duration']

print(total_length)

