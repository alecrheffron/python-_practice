# Challenge One

import re
zen = []
with open('zen.txt', 'r') as f:
    zen.append(f.read())

m = re.findall("Dutch",
               zen[0])

print(m)

# Challene Two

stuff = "Arizona 479, 75, 501, 870. California 209, 213, 650"

l = re.findall("\d..",
               stuff)

print(l)

halloween = "The ghost that says boo haunts the loo."

n = re.findall('.oo',
               halloween)

print(n)