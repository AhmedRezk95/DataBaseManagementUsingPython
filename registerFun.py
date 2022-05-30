
import os
import pandas as pd
import re

def registeration():
    os.system('clear')
    # Set checks for parameters
    first=input("First name: ")
    # if it is not integer
    while (not (first.isalpha())):
        print("Integer/empty Found in first name, please try again")
        first=input("First name: ")
    # Set checks for parameters
    os.system('clear')
    last=input("Last name: ")
    while (not last.isalpha()):
        print("Integer/empty Found in last name, please try again")
        last=input("Last name: ")
    
    # Set checks for parameters
    os.system('clear')
    mail=input("Mail: ").lower()
    # base on what i found online for mail validation
    while not (re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',mail)):
        print("invalid mail,please try again")
        mail=input("Mail: ").lower()

    # Open database to compare
    df = pd.read_csv("DataBase.csv",delimiter=",",header=None)
    df.columns=["first","last","mail","password","mobile"]
    for i in df["mail"]:
        if i == mail:
            print("Mail is already created, please sign in with it")
            return False
    # Set checks for parameters
    
    paswd=input("Password: ")
    os.system('clear')
    Cpasswd=input("Confirm Password: ")
    while (paswd!=Cpasswd):
        os.system('clear')
        print("Not matched, try again")
        Cpasswd=input("Confirm Password: ")
    
    # Set checks for parameter mobile 1
    os.system('clear')
    mobile=input("Mobile(Egyptian): ").lower()
    # regex expression 01[digit contains 0 or 1 or 2 or 5] + 8 digits of any digit [0-9]
    regex = r'01[0125]+[0-9]{8}'
    while (not re.search(regex, mobile)):
        mobile=input("Not a Valid phone number\nEnter a valid Mobile(Egyptian): ").lower()
        
    # add egyptian code
    mobile="+2"+mobile
    # collect data
    data = f"{first},{last},{mail},{paswd},{mobile}\n"
    #open data base and get ready to append
    DataBaseFile= open("DataBase.csv","a")
    # append data to your database
    DataBaseFile.write(data)
    # close file
    DataBaseFile.close()
    return True


