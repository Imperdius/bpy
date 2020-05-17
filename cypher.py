import random
import os.path
from os import path
def encrypt():
    check1 = False
    while check1 == False:
        print("Please enter the word you would like to encrypt")
        encWord = input(">")
        if encWord.isalpha() == False:
            print("Please enter a word...")
        else:
            check1 = True
    necWord = ("")
    lencWord = encWord.lower()
    vouels = lencWord.count("a")
    vouels = vouels + lencWord.count("e")
    vouels = vouels + lencWord.count("i")
    vouels = vouels + lencWord.count("o")
    vouels = vouels + lencWord.count("u")
    for i in lencWord:
        aChar = ord(i)
        aChar = aChar + vouels
        necWord = necWord + str(chr(aChar))
    print("Your encrypted word is ", necWord)
    keyl = vouels * 2
    con = ("bcdfghjklmnpqrstvwxyz")
    vol = ("aeiou")
    keycl = (keyl - vouels)
    key = ("")
    for i in range(keycl):
        nextRandomLetter = random.choice(con)
        key = key + nextRandomLetter
    for i in range(vouels):
        nextRandomLetter = random.choice(vol)
        key = key + nextRandomLetter
    savecheck = False
    while savecheck == False:
        print ("Where would you like to save your key? eg: 'C:\\Users\\harry\\Documents\\python\\ciphertests\\test.txt'")
        saveloc = input(">")
        try :
            open(saveloc, "w+")
        except OSError:
            print("That directory does not exist")
        else:
            savecheck = True
            savenamecheck = False
    print(saveloc)
    with open(saveloc, "w+") as f:
        print(key, file=f)
        f.close()
    print("-------------------------------------------------------------------------------------------")
def decrypt():
    necWord = ("")
    loadcheck= False
    while loadcheck == False:
        print("Please enter the address of the folder containing the key")
        loadloc = input(">")
        try:
            open(loadloc)
        except OSError:
            print("That directory does not exist")
        else:
                loadcheck = True
    with open(loadloc) as f:
        key = f.readline()
        f.close()
    vouels = (len(key)) / 2
    vouels = vouels - 1
    ciphertest = False
    while ciphertest == False:
        print("Please enter the cyphertext")
        encWord = input(">")
        if encWord != (""):
            ciphertest = True
    encWord = encWord.lower()
    for i in encWord:
        achar = ord(i)
        achar = achar - vouels
        necWord = necWord + chr(int(achar))
    print("Your word is", necWord)
    print("-------------------------------------------------------------------------------------------")
while True:
    necWord = ("")
    menucheck = False
    print("What would you like to do? Encrypt or decrypt?")
    print("Please enter 'e' or 'd'")
    iRunOutOfVariableNames = input(">").lower()
    if iRunOutOfVariableNames == ("e"):
        encrypt()
    elif iRunOutOfVariableNames == ("d"):
        decrypt()
    else:
        print("Please enter one of the options")
