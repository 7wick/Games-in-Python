def show(b):
    print("\n "+b[7] + '\t||\t' + b[8] + '\t||\t' + b[9])
    print("-------------------")
    print(" "+b[4] + '\t||\t' + b[5] + '\t||\t' + b[6])
    print("-------------------")
    print(" "+b[1] + '\t||\t' + b[2] + '\t||\t' + b[3]+"\n")

def check(p1,p2,b):
    if( ((b[7]==p1) and (b[8]==p1) and (b[9]==p1)) or ((b[4]==p1) and (b[5]==p1) and (b[6]==p1)) or ((b[1]==p1) and (b[2]==p1) and (b[3]==p1)) or ((b[7]==p1) and (b[4]==p1) and (b[1]==p1)) or ((b[8]==p1) and (b[5]==p1) and (b[2]==p1)) or ((b[9]==p1) and (b[6]==p1) and (b[3]==p1)) or ((b[7]==p1) and (b[5]==p1) and (b[3]==p1)) or ((b[9]==p1) and (b[5]==p1) and (b[1]==p1)) ):
        return 1

    elif( ((b[7]==p2) and (b[8]==p2) and (b[9]==p2)) or ((b[4]==p2) and (b[5]==p2) and (b[6]==p2)) or ((b[1]==p2) and (b[2]==p2) and (b[3]==p2)) or ((b[7]==p2) and (b[4]==p2) and (b[1]==p2)) or ((b[8]==p2) and (b[5]==p2) and (b[2]==p2)) or ((b[9]==p2) and (b[6]==p2) and (b[3]==p2)) or ((b[7]==p2) and (b[5]==p2) and (b[3]==p2)) or ((b[9]==p2) and (b[5]==p2) and (b[1]==p2)) ):
        return 2
    else:
        return 0

def get(c,b):
    if(c%2!=0): #player 1 plays
        f = True
        while f:
            i = int(input("Player 1 choose a vacant position\t"))
            if(i < 1 or i > 9 or b[i] != ""):
                print("*****Invalid entry.*****\n")
            else:
                b[i]=p1
                f = False
    else: #player 2 plays
        f=True
        while f:
            i = int(input("Player 2 choose a vacant position\t"))
            if (i < 1 or i > 9 or b[i] != ""):
                print("*****Invalid entry.*****\n")
            else:
                b[i] = p2
                f=False
    return b

b=["#","","","","","","","","",""]
n1=input("Player 1 enter your name: ").upper()
p1=input(n1+" choose a character: ")
n2=input("Player 2 enter your name: ").upper()
p2=input(n2+" choose a different character: ")
print("\n*****Let`s BEGIN!*****")
show(b)
c=1
flag=True
while flag:
    get(c,b)
    c+=1
    show(b)
    temp=check(p1,p2,b)
    if temp==1:
        flag=False
        print("*****{} WON. Congratulations!!*****\n".format(n1))
        break
    elif temp==2:
        flag = False
        print("*****{} WON. Congratulations!!*****\n".format(n2))
        break
    elif (b[1]!="" and b[2]!="" and b[3]!="" and b[4]!="" and b[5]!="" and b[6]!="" and b[7]!="" and b[8]!="" and b[9]!=""):
        flag = False
        print("*****It`s a DRAW!!*****\n")
        break
print("******* MATCH OVER!! *******\n")