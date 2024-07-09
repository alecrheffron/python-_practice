"""
tv = ["GOT",
      "Narcos",
      "Vice"]
coms = ["Arrested Development",
         "friends",
         "Always Sunny"]
all_shows = []

for show in tv:
    show = show.capitalize()
    all_shows.append(show)

for show in coms:
    show = show.capitalize()
    all_shows.append(show)

print(all_shows)
"""

"""
Nested loop examples

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)

print(added)

while input('y or n? ') != 'n':
    for i in range(1, 6):
        print (i)
"""


"""
Monty Python Questionaire

qs = ["Name?: ",
      "Color?: ",
      "Quest?: "]
n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3
"""

some_shows = ["The Walking Dead",
              "Entourage",
              "The Sopranos",
              "The Vampire Diaries"]
for index, show in enumerate(some_shows):
    print(show)
    print(index)

for i in range(25,51):
    print(i)

list1 = [8,
         19,
         148,
         4]
list2 = [9,
         1,
         33,
         83]
multiplied = []
for i in list1:
    for j in list2:
        multiplied.append(i * j)

print(multiplied)

while True:
    print('Type "q" to be a quitter')
    a = input("Guess a number: ")
    if a == "23":
        print("You Got it!!!")
        break
    if a == "q":
        print("QUITTER!!!")
        break
    print("Try again bitch")

