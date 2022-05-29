import os
import pandas as pd
def ViewProjects():
    os.system('clear')
    df = pd.read_csv("projects.csv",delimiter=",",header=None)
    df.columns=["mail","title","description","total","str","end"]
    df2 = df.to_string(index=False)
    print(df2)