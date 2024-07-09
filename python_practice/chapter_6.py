fox = ["the", "fox", "jumped", "over", "the", "fence"]

fox_modified = " ".join(fox).capitalize()

print ("{}.".format(fox_modified))

x = "A screaming comes across the sky."
print(x.replace("s", "$"))

author = "Hemingway"
print (author.index("m"))

numba = "three"
print ("{} {} {}".format(numba, numba, numba))
print (numba * 3)

slicing = "It was a bright cold day in April, and the clocks were striking thirteen."
slicing_index = slicing.index(",")
print (slicing[:slicing_index])