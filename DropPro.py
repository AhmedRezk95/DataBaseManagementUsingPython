
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
        location=input("project column value: \n")
        # if target is string
        if not location.isdigit():
            # check if string is existed
            exists= df[select].str.contains(location).any()
            if exists:
                # drop these records
                df.drop(df[df[select] == location].index, inplace=True)
                df.to_csv("projects.csv",header=None,index=None)
                print(df.loc[df['mail'] == mail])
            else:
                print("Not existed")
        else:
            exists= int(location) in df[select]
            if exists:
                df.drop(df[df[select] == int(location)].index, inplace=True)
                df.to_csv("projects.csv",header=None,index=None)
                print(df.loc[df['mail'] == mail])
            else:
                print("Not existed, number")
    else:
        print("No project created by this user")


def delete(df,select,location):
    df.drop(df[df[select] == int(location)].index, inplace=True)
    df.to_csv("projects.csv",header=None,index=None)
    print(df.loc[df['mail'] == mail])
