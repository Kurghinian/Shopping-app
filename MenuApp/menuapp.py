from time import sleep as ts
import os
global balance
balance = "1000$"
username = "administrator"
password = "administratorpassword"
def menu():
    print()
    print("----------")
    print("|Menu Bar|")
    print("----------")
    print("1. Settings")
    print("------------")
    print("2. My Balance")
    print("------------")
    print("3. Shopping")
    print("------------")
    print("4. Exit")
    print("------------")
menu()

def settings():
    print()
    print("----------")
    print("|Settings|")
    print("----------")
    print("1. View Username and Password")
    print("----------")
    print("2. Exit")
def balance():
    print("Please Enter Your Username And Password")
    username1 = input("Enter Your Username  ")
    password1 = input("Enter Your Password  ")
    if username1 == username and password1 == password:
        ts(2)
        balance = "1000$"
        print("Your Balance is", balance)
        clss = input("Do You want clear terminal? y or n ")
        if clss == "y":
            os.system("cls")
    else:
        print("Wrong Username or password")
        print("please go to settings and get your username and password")
        clss = input("Do You want clear terminal? y or n ")
        if clss == "y":
            os.system("cls")

def shopping():
    user = input("Enter Your username")
    pwd = input("enter your password")
    if user == username and pwd == password:
        balance = "1000$"
        bb = 1000
        print("Balance", "-", balance)
        print("----------")
        print("----Shopping Page----")
        print("1. Tea - 50$")
        print("2. Milk - 50$")
        print("3.  Coffe - 60$")
        print("=============")
        print("4. bottle of barbecue - 150$")
        sh = int(input("What do you want?"))
        if sh == 1:
            print("You Buy 1X Tea ", "your Balance", bb - 50 )
            sh = int(input("again?"))
            if sh == 2:
                print("You Buy 1X Milk ", "your Balance", bb - 50 )
            if sh == 3:
                print("You Buy 1X Coffe ", "your Balance", bb - 60 )
            if sh == "4":
                print("You Buy 1X Tea ", "your Balance", bb - 150 )
        if sh == 2:
            print("You Buy 1X Milk ", "your Balance", bb - 50 )
            sh = int(input("again?"))
            if sh == 2:
                print("You Buy 1X Milk ", "your Balance", bb - 50 )
            if sh == 3:
                print("You Buy 1X Coffe ", "your Balance", bb - 60 )
            if sh == "4":
                print("You Buy 1X Tea ", "your Balance", bb - 150 )
        if sh == 3:
            print("You Buy 1X Coffe ", "your Balance", bb - 60 )
            sh = int(input("again?"))
            if sh == 2:
                print("You Buy 1X Milk ", "your Balance", bb - 50 )
            if sh == 3:
                print("You Buy 1X Coffe ", "your Balance", bb - 60 )
            if sh == "4":
                print("You Buy 1X Tea ", "your Balance", bb - 150 )
        if sh == "4":
            print("You Buy 1X Tea ", "your Balance", bb - 150 )
            sh = int(input("again?"))
            if sh == 2:
                print("You Buy 1X Milk ", "your Balance", bb - 50 )
            if sh == 3:
                print("You Buy 1X Coffe ", "your Balance", bb - 60 )
            if sh == "4":
                print("You Buy 1X Tea ", "your Balance", bb - 150 )

def exit():
    os.system("exit")            
option = int(input("Enter Your Option  "))





if option == 2:
    balance()
if option == 1:
    settings()
    option1 = int(input("Enter Your Option"  ))
    if option1 == 1:
        print("username", "-", username)
        print("password", '-', password)   
        print()
        settings()
    elif option1 == 2:
        os.system("cls")
        menu()
if option == 3:
    shopping()
if option == 4:
    exit()



print( "©  Khachatur Kurghinyan" )