import os
import re
import pandas as pd

from dateFunctions import validate

'''mobile=input("Mobile(Egyptian): ")
regex = re.search('01[0125]+[0-9]{8}',mobile)
print(regex)'''


'''def validate_eg_mob_num():
    os.system('clear')
    import re
    regex = r'01[0125]+[0-9]{8}'
    while True:
        mobile_number = input("input mobile: ")
        if(re.fullmatch(regex, mobile_number)):
            return mobile_number

validate_eg_mob_num()
'''
'''p=input("set: ")
while not validate(p):
    print("This is not date format!")
    p=input("Enter a valid date DD/MM/YYYY: ")'''

pd.options.mode.chained_assignment = None  # default='warn'

'''
os.system('clear')
df = pd.read_csv("projects.csv",delimiter=",",header=None)
df.columns=["mail","title","description","total","str","end"]
mail="ar@g.com"
print(df)
print("------------------------------------------\n")

# create dataframe for specific mail
df_mail= df.loc[df['mail'] == mail]
print(df_mail)
# initialize parameters, title must be unique
t=input("title\n")'''
'''select=input("enter column\n")
p=input("replace\n")'''
'''# replace value of selected column name based on title
df_mail.loc[df_mail["title"] == t, select ] = p
# update it to the main dataframe
df.update(df_mail)'''
'''# condition select = str
print(type())'''

def duplicate(placement,dataframe):
    unique= dataframe["title"].str.contains(placement).any()
    while placement.isdigit() or unique:
        os.system('clear')
        print("Error, Try Again")
        # Check again
        placement=input("Enter Project title: ")
        unique= dataframe["title"].str.contains(placement).any()


