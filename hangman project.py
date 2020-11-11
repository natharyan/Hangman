print("""HELLO!!!
THIS IS A PROGRAM FOR THE GAME HANGMAN""")
print("THEME OF THE GAME: COMPUTER SCIENCE")
print()    
print("""INSTRUCTIONS:

YOU WILL SEE A FEW LETERS AS A HINT,
USING THEM YOU HAVE THE TO GUESS THE CORRECT TERM
EACH DASH REPRESENTS A SINGLE LETTER
""")

l=['ip address','processor','bandwidth','big data','cloud storage','code',
   'debug','disk storage','ethernet','hacker']

#len(l)=11
import random


while True:
    z=0
    u=0
    r=""
    a=l[random.randint(0,len(l)-1)]
    b=list(a)
    c=list(a)
    e=[]
    for i in range(0,random.randint(2,len(a)-1)):
        y=b[random.randint(0,len(a)-1)]
        if y!=" " and y not in e:
            p=b.index(y)
            b[p]=' __ '
            e+=[y]
    f=e
    print("Guess the Word:")
    print()
    t=""
    for i in range(len(b)):
        t+=b[i]
    print(t)
    
    while True:
        if z==0:
            print("""
                     *===*
                     |   |
                         |
                         |
                         |
                         |
                     """)
        if z==1:
            
            print("""
                     *===*
                     |   |
                     O   |
                         |
                         |
                         |
                     """)
        if z==2:
            
            print("""
                     *===*
                     |   |
                     O   |
                     |   |
                         |
                         |
                     """)
        if z==3:
            
            print("""
                     *===*
                     |   |
                     O   |
                    /|   |
                         |
                         |
                     """)


        if z==4:
            
            print("""
                     *===*
                     |   |
                     O   |
                    /|\  |
                         |
                         |
                     """)

        if z==5:
            
            print("""
                     *===*
                     |   |
                     O   |
                    /|\  |
                    /    |
                         |
                     """)
        s=input("WORD: ")
        print()
        if s in e:
            d=c.index(s)
            b[d]=s
            for i in range(len(b)):   
                r+=b[i]
        print(r,"\n")

        if s not in e and s in b:
            print("the letter","'",s,"'","has no further repitions\n")

        if s in e:
            e.remove(s)


        if s not in b:
            if z==0:
                print("WHOOPS")
                print("TRIES REMAINING: 5")
            if z==1:
                print("YOU CAN STILL DO THIS!!")
                print("TRIES REMAINING: 4")
            if z==2:
                print("GETTING IN THE DANGER ZONE....")
                print("TRIES REMAINING: 3")
            if z==3:
                print("FOCUS!!!!")
                print("TRIES REMAINING: 2")
            if z==4:
                print("LAST CHANCE","(⊙＿⊙')")
                print("TRIES REMAINING: 1")
            z+=1

        

        

        if z==6:
            print("""
                     *===*
                     |   |
                     O   |
                    /|\  |
                    / \  |
                         |
                     """)
            print("YOU LOSE :(\n")
            print("CORRECT WORD:",a)
            print("*********************************************")
            u=1
            break
            
        if r==a:
            print("YOU WIN!!\n")
            print("*********************************************")
            break
        r=""

    if u==0:
        print("YOU'RE AMAZING AT THIS!!")
        x=input("PLAY AGAIN? ")

    if u==1:
        print("NO WORRIES!")
        x=input("TRY AGAIN? ")
        

    if x=='no' or x=='NO':
        print("THANK YOU FOR PLAYING!!")
        break
    
