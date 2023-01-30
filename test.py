#!/usr/bin/python3

def processNum(a, b , c = 10):
    return a/(a*b)+c

def deductNum(d):
    number = processNum(a,b)
    return number - d

def generateNum(e,f):
    deductedNum = deductNum(d)
    generated = deductedNum ** e // f
    if generated < 50:
        print(str(generated) + ",The value is less than 50.")
    elif generated > 50:
        print(str(generated )+ ",The value is more than 50.")
    else:
        print("Process Malfunctioned")

generateNum(e,f)
