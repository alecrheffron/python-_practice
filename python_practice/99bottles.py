x = 99
song_1 = "bottles of beer on the wall"
song_2 = "bottles of beer, you take one down and pass it around"
while x > 1:
    print("{} {}, {} {}, {} {}".format(x, song_1, x, song_2, x-1, song_1))
    x -= 1
print("Last {}, last {}, you're drunk".format(song_1.replace("bottles", "bottle"), song_2.replace("bottles", "bottle")))