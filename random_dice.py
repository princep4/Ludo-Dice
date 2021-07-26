import random

ch='y'

while ch=='y':
    r=random.randint(1,6)
    if r==1:
        print("[   ]")
        print("[ 0 ]")
        print("[   ]")
    if r==2:
        print("[    ]")
        print("[ 00 ]")
        print("[    ]")
    
    if r==3:
        print("[0   ]")
        print("[ 0  ]")
        print("[  0 ]")
    
    if r==4:
        print("[0  0]")
        print("[ 0  ]")
        print("[  0 ]")
    if r==5:
        print("[0  0]")
        print("[ 0  ]")
        print("[0  0]")
    
    if r==6:
        print("[0  0]")
        print("[0  0]")
        print("[0  0]")

    ch=input("Enter 'Y' if dice again")


