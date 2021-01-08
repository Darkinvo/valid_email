import random

# this a , b inha baye b , k bodan hastesh
a,b = 0,0
hads = random.randint(1,99)
print("it is number hads computer :", hads)
you_num = input("enter (b, k, d): ")
# this yani age k bod (you_num): yani number ke computer hads zade small tarz number mane 
if you_num == 'k':
    # this in ta zamani ke (k) hastehs: azash miporse hast ya na 
    while you_num == 'k':
        a=hads
        hads = random.randint(a,99)
        print("it is number hads computer: ", hads)
        you_num = input("enter (b ,k , d):")
        # this age inja (you_num): (b) yani number ke computer hads zade big tar az number mane
        if you_num == 'b':
            while you_num == 'b':
                b= hads
                hads = random.randint(a,b)
                print("it is number hads computer :", hads)
                you_num = input("enter (b ,k , d):")
# this baraxxe balayi hastesh 
if you_num == 'b':
    while you_num == 'b':
        b= hads
        hads = random.randint(1,b)
        print("it is number hads computer :", hads)
        you_num = input("enter (b ,k , d):")
        if you_num == 'k':
            while you_num == 'k':
                a=hads
                hads = random.randint(a,b)
                print("it is number hads computer :", hads)
                you_num = input("enter (b ,k , d):")

if you_num == 'd':
    print("good you did it. woooowwwww!!!!! :D you win baby.")