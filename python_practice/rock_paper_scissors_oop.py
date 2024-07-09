import random


class Player:
    def __init__(self, name):
        self.wins = 0
        self.gesture = None
        self.name = name

    def win_round(self):
        self.wins += 1



class Game:
    def __init__(self):
        name1 = input("What's your name: ")
        name2 = input("What's the computer's name: ")
        self.p1 = Player(name1)
        self.c1 = Player(name2)
        self.gwin = [1, 1]

    def round(self):
        p1n = self.p1.name
        c1n = self.c1.name
        p1w = self.p1.wins
        c1w = self.c1.wins
        gw = self.gwin
        print("\n")
        while True:
            while p1w != gw[0]:
                while c1w != gw[0]:
                    self.play_game()
            if p1w == gw[0]:
                m = input("Wanna keep playing? Yes to keep going or anything else to quit").capitalize()
                if m == "Yes":
                    gw[0] += 1
                    gw[1] += 2
                else:
                    break
            elif c1w == gw:
                m = input("Wanna keep playing? Yes to keep going or anything else to quit").capitalize()
                if m == "Yes":
                    gw[0] += 1
                    gw[1] += 2
                else:
                    break


    def score(self, p1n, p1w, c1n, c1w):
        d = "The score is -- {}:{}  {}:{} "
        d = d.format(p1n, p1w, c1n, c1w)
        print(d)


    def play_game(self):
        p1n = self.p1.name
        c1n = self.c1.name
        p1w = self.p1.wins
        c1w = self.c1.wins
        game_pieces = ("Rock", "Paper", "Scissors")
        rockw = "Rock crushes Scissors"
        paperw = "Paper suffocates Rock"
        scissorw = "Scissor dismembers paper"
        p1v = "... you win"
        c1v = "... I WIN!!"
        p1g = input("Rock, Paper, Scissors: ").capitalize()
        c1g = game_pieces[random.randint(0, len(game_pieces)) - 1]
        if p1g == c1g:
            print("Ugh... I picked {} too".format(p1g))
        elif p1g == game_pieces[0] and c1g == game_pieces[2]:
            print(rockw + p1v)
            self.score(p1n, p1w, c1n, c1w)
            self.p1.win_round()
        elif p1g == game_pieces[2] and c1g == game_pieces[1]:
            print(scissorw + p1v)
            self.p1.win_round()
        elif p1g == game_pieces[1] and c1g == game_pieces[0]:
            print(paperw + p1v)
            self.p1.win_round()
        elif p1g == game_pieces[2] and c1g == game_pieces[0]:
            print(rockw + c1v)
            self.c1.win_round()
        elif p1g == game_pieces[1] and c1g == game_pieces[2]:
            print(scissorw + c1v)
            self.c1.win_round()
        elif p1g == game_pieces[0] and c1g == game_pieces[1]:
            print(paperw + c1v)
            self.c1.win_round()
        else:
            print("That's not what i asked...\n")




game = Game()
game.round()