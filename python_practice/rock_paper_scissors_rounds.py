import random

def rock_paper_scissors():
    x1 = 0
    x2 = 0
    gw = 1
    gt = 1
    game_pieces = "Rock", "Paper", "Scissors"
    msg = "Rock, Paper, Scissors: "
    while True:
        while(x1 < gw or x2 < gw):
            print("Best {} outta {}... You: {}, Me: {}".format(gw, gt, x1, x2))
            p1 = input(msg).capitalize()
            p2 = game_pieces[random.randint(0, len(game_pieces)) - 1]
            if ((p1 == game_pieces[0] and p2 == game_pieces[2]) or
                (p1 == game_pieces[2] and p2 == game_pieces[1]) or
                (p1 == game_pieces[1] and p2 == game_pieces[0])):
                    print("I picked {}...".format(p2))
                    print("You Win!\n")
                    x1 += 1
                    if x1 == gw:
                        break
                    else:
                         print("You: {}, Me: {}".format(x1, x2))
            elif ((p1 == game_pieces[0]  and p2 == game_pieces[1]) or
                (p1 == game_pieces[2] and p2 == game_pieces[0] ) or
                (p1 == game_pieces[1] and p2 == game_pieces[2])):
                    print("HA! I picked {}!!".format(p2))
                    print("You lose bitch!!\n")
                    x2 += 1
                    if x2 == gw:
                        break
                    else:
                        print("You: {}, Me: {}".format(x1, x2))
            elif   p1 == p2:
                print("{}?... that's what i picked\n".format(p2))
            else:
                print("That's not what i asked....\n")
        print ("You: {} Me: {}".format(x1, x2))
        another = input("Wanna keep playing? ").lower()
        if another == "yes":
            gw += 1
            gt += 2
            print("\n")
        elif another == "no":
            print("\n")
            break
        else:
            print("Not what I asked... whatever i quit")
            print("\n")
            break
    if x1 == gw:
        print("You win {} to {}".format(x1, x2))
    elif x2 == gw:
        print("I win {} to {}, suck it".format(x2, x1))


