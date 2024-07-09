import random

class Player:
    def __init__(self, name):
         self.p1 = 0
         self.c1 = 0
         self.name = name


class RockPaperScissors:
    def game(self):
        gw = 1
        gt = 1
        while True:
            while p1 or c1 != gw:
                print("Best {} outta {}.... You: {}, Me: {}".format(gw, gt, p1, c1))
                return self.round()
            if p1 == gw:
                print("You win!!")
                p1 += 1
            elif c1 == gw:
                print("I win!!")
                c1 += 1
            keep_playing = "Wanna keep playing?: "
            p1a = input(keep_playing).lower()
            if p1a == "yes" or "yeah" or "y":
                gw += 1
                gt += 2
                print("Best {} out of {}".format(gw, gt))
            elif p1a == "no" or "nah" or "n":
                print("Okay, bye bye then")
                break
            else:
                 print("That's not what I asked... whatever i quit")
                 break




    def round(self):
        game_pieces = ["Rock", "Paper", "Scissors"]
        msg = "Rock, Paper, Scissors: "
        p1g = input(msg).capitalize()
        c1g = game_pieces[random.randint(0, 2)]
        if ((p1g == game_pieces[0] and c1g == game_pieces[2]) or
            (p1g == game_pieces[2] and c1g == game_pieces[1]) or
            (p1g == game_pieces[1] and c1g == game_pieces[0])):
                print("I picked {}...".format(c1g))
                print("You Win!\n")
        elif ((p1g == game_pieces[0] and c1g == game_pieces[1]) or
              (p1g == game_pieces[2] and c1g == game_pieces[0] ) or
              (p1g == game_pieces[1] and c1g == game_pieces[2])):
                print("HA! I picked {}!!".format(c1g))
                print("You lose bitch!!\n")
        elif p1g == c1g:
            print("{}?... that's what i picked\n".format(p1g))
        else:
            print("That's not what i asked...")


    def wins(self, p1g, c1g, p1, c1):


    def winner(self, win[0], win[1], win[2]):
        w = "{} beats {}, {} wins this round"
        w = w.format(wins)
        print(w)



game = RockPaperScissors()
game.game()