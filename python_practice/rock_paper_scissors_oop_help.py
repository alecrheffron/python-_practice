from random import randrange


class Player(object):
    def __init__(self, who = 'you'):
        self.score = 0
        self.who = who

    def choose(self):
        choice = int(input("Rock [1] Paper [2] Scissors [3]"))
        return choice

    def win_round(self):
        self.score += 1

    def win_game(self):
        print("{} wins!!!".format(self.who).upper())

class ComputerPlayer(Player):
    def __init__(self, who = None):
        Player.__init__(self, WHO = 'THE COMPUTER')

    def