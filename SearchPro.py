
import os
import pandas as pd


def SearchProject():
    os.system('clear')
    df = pd.read_csv("projects.csv",delimiter=",",header=None)
    df.columns=["mail","title","description","total","str","end"]

    # set date filter on start date
    filter=input("\n----------------------------------------------------------------------\nSet starting date as DD/MM/YYYY format: \n")
    os.system('clear')
    searching= df[["title","description","total","str","end"]].loc[df['str'] == filter]
    if searching.empty:
        print('No Data Found!')
    else:
        print(searching)