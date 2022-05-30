import os
from dateFunctions import *
import pandas as pd

df = pd.read_csv("projects.csv",delimiter=",",header=None)
df.columns=["mail","title","description","total","str","end"]

def AddProjects(email):
    os.system('clear')

    titleAdd=input("Enter Project title: ")
    # check if input is unique
    unique= df["title"].str.contains(titleAdd).any()
    while titleAdd.isdigit() or unique:
        os.system('clear')
        print("Duplicate/Integer Found!, Try Again")
        # Check again
        titleAdd=input("Enter Project title: ")
        unique= df["title"].str.contains(titleAdd).any()

    os.system('clear')
    detailAdd=input("Enter Project Details: ")
    while detailAdd.isdigit():
        print("Please set a string")
        detailAdd=input("Enter Project Details: ")

    os.system('clear')
    totalAdd=input("Enter project total target: ")
    while not totalAdd.isdigit():
        print("Please set a number")
        totalAdd=input("Enter Project total target: ")

    os.system('clear')
    strAdd=input("Enter project start date as DD/MM/YYYY: ")
    while not validate(strAdd):
        os.system('clear')
        print("Not a date,Please try again")
        strAdd=input("Enter project start date as DD/MM/YYYY: ")

    os.system('clear')
    endAdd=input("Enter project end date as DD/MM/YYYY: ")
    while not validate(endAdd):
        print("Not a date, Please try again!")
        endAdd=input("Enter project end date as DD/MM/YYYY: ")
    
    # check if start date is earlier than
    while not earlier(strAdd,endAdd):
        endAdd=input("Enter project end date as DD/MM/YYYY: ")

    # collect data
    data = f"{email},{titleAdd},{detailAdd},{totalAdd},{strAdd},{endAdd}\n"
    os.system('clear')
    print("Project Added")
    #open data base and get ready to append: write from last line
    ProjectFile= open("projects.csv","a")
    # append data to your database
    ProjectFile.write(data)
    # close file
    ProjectFile.close()
