"""
my_list = list()

with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)
"""

import csv

"""
with open("st.csv", "w", newline='') as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(["one",
                "two",
                "three"])
    w.writerow(["four",
                "five",
                "six"])
"""

"""
with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
"""

# Challenge 2
"""
answer = input("What is the best movie ever? ")
with open("best_movie.txt", "w") as f:
    f.write(answer)
"""

# Challenge 3
with open("movie.csv", "w", newline='') as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(["Top Gun",
                "Risky Business",
                "Minority Report"])
    w.writerow(["Titanic",
                "The Revenant",
                "Inception"])
    w.writerow(["Training Day",
                "Man on Fire",
                "Flight"])