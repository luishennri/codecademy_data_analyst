# List of paintings in de museum
paintings = ['The Two Fridas', 'My Dress Hangs Here',
             'Tree of Hope', 'Self Portrait With Monkeys']

# List of dates
dates = [1939, 1933, 1946, 1940]

# Each painting is paired with its date
paintings = list(zip(paintings, dates))

# Appending more paintings
paintings.append(['The Broken Column', 1944])
paintings.append(['The Wounded Deer', 1946])
paintings.append(['Me and My Doll', 1937])

# List to enumerate each painting
audio_tour_number = []

# Adding each number in the list
for i in range(len(paintings)):
    audio_tour_number
    audio_tour_number.append(i+1)

# Each painting and date is paired with its number
master_list = list(zip(audio_tour_number, paintings))

print(master_list)
