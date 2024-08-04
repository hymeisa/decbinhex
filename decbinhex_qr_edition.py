# A simple Python game for practicing converting between decimal, binary, and hex.
# Original code with documentation can be found at https://github.com/hymeisa/decbinhex.

import random as r

def db(r):
    return format(r,'08b')
def dh(r):
    return format(r,'02X')
def bd(b):
    return int(b,2)
def bh(b):
    return format(int(b,2),'02X')
def hd(h):
    return int(h,16)
def hb(h):
    return format(int(h,16),'08b')

def dbg():
    t = 0
    while True:
        rn = r.randint(0,255)
        bn = db(rn)
        un = ""
        while un != bn:
            print(f"Decimal: {rn}\nlength: 8")
            un = input("Enter number in binary: ")
            if un.lower() == "exit":
                mm()
        t += 1
        print(f"{bn}\nCorrect! total correct: {t}")
def dhg():
    t = 0
    while True:
        rn = r.randint(0,255)
        hn = dh(rn)
        un = ""
        while un != hn:
            print(f"Decimal: {rn}")
            un = input("Enter in hex: ").upper()
            if un.lower() == "exit":
                mm()
        t += 1
        print(f"{hn}\nCorrect! total correct: {t}")
def bdg():
    t = 0
    while True:
        rn = r.randint(0,255)
        bn = db(rn)
        un = ""
        while un != str(rn):
            print(f"Binary: {bn}")
            un = input("Enter in decimal: ")
            if un.lower() == "exit":
                mm()
        t += 1
        print(f"{rn}\nCorrect! total correct: {t}")
def bhg():
    t = 0
    while True:
        bn = db(r.randint(0,255))
        hn = bh(bn)
        un = ""
        while un != hn:
            print(f"Binary: {bn}")
            un = input("Enter in hex: ")
            if un.lower() == "exit":
                mm()
        t += 1
        print(f"{hn}\nCorrect! total correct: {t}")
def hdg():
    t = 0
    while True:
        rn = r.randint(0,255)
        hn = dh(rn)
        un = ""
        while un != str(rn):
            print(f"Hex: {hn}")
            un = input("Enter in decimal: ")
            if un.lower() == "exit":
                mm()
        t += 1
        print(f"{rn}\nCorrect! total correct: {t}")
def hbg():
    t = 0
    while True:
        hn = dh(r.randint(0,255))
        bn = hb(hn)
        un = ""
        while un != bn:
            print(f"Hex: {hn}")
            un = input("Enter in binary: ")
            if un.lower() == "exit":
                mm()
        t += 1
        print(f"{bn}\nCorrect! total correct: {t}")

def mm():
    print("1. Decimal to binary\n2. Decimal to hex\n3. Binary to decimal\n4. Binary to hex\n5. Hex to decimal\n6. Hex to binary")
    m = input("Select a game: ")
    if m == "1":
        dbg()
    elif m == "2":
        dhg()
    elif m == "3":
        bdg()
    elif m == "4":
        bhg()
    elif m == "5":
        hdg()
    elif m == "6":
        hbg()
    else:
        print("Invalid number. Please try again.")
        mm()

print("Type 'exit' at any time during a game to quit to main menu.")
mm()
