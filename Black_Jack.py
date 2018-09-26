import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,'Queen': 10, 'King': 10, 'Ace': 11}
used_cards = []

def play():
    flag = True
    while flag:
        l = [random.choice(ranks), random.choice(suits)]
        s = str(l[0]) + str(l[1])
        if not (s in used_cards):
            used_cards.append(s)
            flag = False
            return l

def hit(x, s):
    flag=True
    while(x<21 and flag):
        if((int(input("Press 1 to HIT or 2 to STAND  ")) == 1)):
            li=play()
            x=x+values[li[0]]
            print("{} got {} and {}`s total={}".format(s, str(li[0])+" of "+str(li[1]), s, x))
        else:
            flag=False
            break
    return x

bet1 = int(input("***Welcome to Black Jack***\nLet`s play\nChoose your bet player 1: "))
bet2 = int(input("Choose your bet player 2: "))
print("******The cards are shuffled!******")
first = play()
second = play()
print("Player 1 has got first two cards as: {} and {}".format((str(first[0])+" of "+str(first[1])), (str(second[0])+" of "+str(second[1]))))
player1 = values[first[0]]+values[second[0]]
first = play()
second = play()
print("Player 2 has got first two cards as: {} and {}".format((str(first[0])+" of "+str(first[1])), (str(second[0])+" of "+str(second[1]))))
player2 = values[first[0]]+values[second[0]]
if(player1<21):
    print("***Player 1 plays first!***")
player1=hit(player1,"Player 1")
if(player1>21): #busted
    print("Player 1 BUSTED. Player 2 won the bet of {}!!".format(bet1+bet2))
else:
    print("***Player 2 plays now!***")
    player2 = hit(player2, "Player 2")
    if (player2 > 21):  # busted
        print("Player 2 BUSTED. Player 1 won the bet of {}!!".format(bet1+bet2))
    else:
        print("*****GAME OVER*****")
        print("Player`s total={} and Player 2`s total={}".format(player1, player2))
        if(player2>player1):
            print("**CONGRATULATIONS. Player 2 won the bet of {}!!**".format(bet1+bet2))
        elif(player2<player1):
            print("CONGRATULATIONS. Player 1 won the bet of {}!!".format(bet1+bet2))
        else:
            print("It`s a DRAW. You both lost the bet!!")