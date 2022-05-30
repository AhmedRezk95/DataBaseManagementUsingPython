
import os
import pandas as pd


def DropProject(mail):
    os.system('clear')
    df = pd.read_csv("projects.csv",delimiter=",",header=None)
    df.columns=["mail","title","description","total","str","end"]
    exists= df['mail'].str.contains(mail).any()
    if exists:
        print(df.loc[df['mail'] == mail])
        select=input("which project 'Column' do you want to delete?\n")
        while not (select in df.columns):
            print("not existed, try again")
            select=input("select column:\n")
            
        value=input("project column value: \n")
        # Use delete function
        delete(df,mail,select,value)
    else:
        print("No project created by this user")


def delete(df,mail_value,select,columnValue):
    # if target is string
    if not columnValue.isdigit() and select != "total":
        # check if string is existed
        exists= df[select].str.contains(columnValue).any()
        if exists:
            # drop these records
            df.drop(df[df[select] == columnValue].index, inplace=True)
            df.to_csv("projects.csv",header=None,index=None)
            print(df.loc[df['mail'] == mail_value])
        else:
            print("Not existed")
    # in case if user choose total and set string value
    elif not columnValue.isdigit() and select == "total":
        print("Invalid Parameter(string)")
    else:
        exists= int(columnValue) in df[select]
        if exists:
            df.drop(df[df[select] == int(columnValue)].index, inplace=True)
            df.to_csv("projects.csv",header=None,index=None)
            print(df.loc[df['mail'] == mail_value])
        else:
            print("Not existed, number")
