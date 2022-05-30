import os
from dateFunctions import earlier, validate
import pandas as pd

# turn off pandas warning
pd.options.mode.chained_assignment = None  # default='warn'


def EditProject(mail):
    os.system('clear')
    df = pd.read_csv("projects.csv",delimiter=",",header=None)
    df.columns=["mail","title","description","total","str","end"]

    # Check email existence
    exists= df['mail'].str.contains(mail).any()

    # create dataframe for specific mail
    df_mail= df.loc[df['mail'] == mail]
    if exists:
        # display mail dataframe
        print(df_mail)

        t=input("What is your project title?\n%? ")
        # check if input is unique
        exist= df_mail["title"].str.contains(t).any()
        while t.isdigit() or (not exist) or t=="":
            os.system('clear')
            print(df_mail)
            print("Not Existed, Try again!")
            # Check again
            t=input("Enter Project title: ")
            exist= df_mail["title"].str.contains(t).any()

        select=input("which column do you want to change?\n")
        while not (select in df.columns):
            os.system('clear')
            print(df_mail)
            print("not existed, try again")
            select=input("select column again:\n")
        # in case it is not date type
        if select != "str" and select != "end":
            p=input("Set the new value\n")
            # Incase you want to change title you have to make sure that is unique value
            unique= df_mail["title"].str.contains(p).any()
            if select != "total":
                # unlike total column all parameter are string type
                while p.isdigit() or unique:
                    os.system('clear')
                    print(df_mail)
                    print("Invalid Type(Integer), Try Again")
                    # Check again
                    p=input("Enter New value again!: ")
                    unique= df_mail["title"].str.contains(p).any()
            else:
                # in case of total it must be integer
                while not p.isdigit():
                    os.system('clear')
                    print(df_mail)
                    print("Invalid Type(string), Try Again")
                    # Check again
                    p=input("Enter New value again!: ")
            # replace value of selected column name based on title
            df_mail.loc[df_mail["title"] == t, select ] = p
            # update it to the main dataframe
            df.update(df_mail)
            df.to_csv(r'projects.csv', header=False, index=False)
            print(df_mail)
        elif select == "str":
            # get end date for the same row
            end= df_mail["end"].loc[df_mail["title"]==t].item()
            p=input("Set the new value\n")
            # replace value of selected column name based on title
            while not validate(p):
                os.system('clear')
                print(df_mail)
                print("This is not date format!")
                p=input("Enter a valid date DD/MM/YYYY: ")
            # Check str date < end date
            while not earlier(p,end):
                os.system('clear')
                print(df_mail)
                
                p=input("Enter a valid date DD/MM/YYYY:\n")
            # replace
            df_mail.loc[df_mail["title"] == t, select ] = p
            # update it to the main dataframe
            df.update(df_mail)
            df.to_csv(r'projects.csv', header=False, index=False)
            print(df_mail)
        elif select == "end":
            # get end date for the same row
            str= df_mail["str"].loc[df_mail["title"]==t].item()
            p=input("Set the new value\n")
            # replace value of selected column name based on title
            while not validate(p):
                os.system('clear')
                print(df_mail)
                print("This is not date format!")
                p=input("Enter a valid date DD/MM/YYYY: ")
            # Check str date < end date
            while not earlier(str,p):
                os.system('clear')
                print(df_mail)
                p=input("Enter a valid date DD/MM/YYYY:\n")
            # replace
            df_mail.loc[df_mail["title"] == t, select ] = p
            # update it to the main dataframe
            df.update(df_mail)
            df.to_csv(r'projects.csv', header=False, index=False)
            print(df_mail)
        else:
            print("Something is wrong,please check your inputs again")
    else:
        print("No project created by this user")

