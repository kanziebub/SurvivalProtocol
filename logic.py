
def set_df(id, name):
    url = f'https://docs.google.com/spreadsheets/d/{id}/gviz/tq?tqx=out:csv&sheet={name}'
    df = pd.read_csv(url)
    df = df.iloc[1:9 , 1:9]

    df.rename(
    columns = {
        'Unnamed: 1':'Rank',
        'Unnamed: 2':'Name',
        'Unnamed: 3':'Total Point',
        'Unnamed: 4':'Total TK',
        'Unnamed: 5':'Avg TK',
        'Unnamed: 6':'Avg Placement',
        'Unnamed: 7':'Avg Placement Point',
        'Unnamed: 8':'Games Played',
        }, 
    inplace = True)

    return df

# def get_TK(df, team):
#     return 0

# =====================================================

# Imports
import pandas as pd

# Tourney 12 Aug 2023
# https://docs.google.com/spreadsheets/d/1hLUR46LwreWo-B3oi1AsYvSiF_qvRxVAcUIpcUZcj9s/edit?usp=sharing

ID_squads_12aug2023 = "https://docs.google.com/spreadsheets/d/1hLUR46LwreWo-B3oi1AsYvSiF_qvRxVAcUIpcUZcj9s/edit#gid=1885268704"
sheetID = "1hLUR46LwreWo-B3oi1AsYvSiF_qvRxVAcUIpcUZcj9s"
sheetName = "ERCT"

df = set_df(sheetID, sheetName)
print(df)



