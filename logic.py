
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

def get_by_team(df, team, field):
    row = df.loc[df['Name'] == team]
    return row[field].values[0]

def get_by_rank(df, rank, field):
    row = df.iloc[rank-1:rank]
    return row[field].values[0]

# =====================================================

# Imports
import pandas as pd

# Tourney 12 Aug 2023
# https://docs.google.com/spreadsheets/d/1hLUR46LwreWo-B3oi1AsYvSiF_qvRxVAcUIpcUZcj9s/edit#gid=1885268704\
sheetID = "1hLUR46LwreWo-B3oi1AsYvSiF_qvRxVAcUIpcUZcj9s"
sheetName = "ERCT"

df = set_df(sheetID, sheetName)

teams = [
    "SKILLISSUE",
    "LF CHINESE GF",
    "Pecinta Paha Laura",
    "Party Orang Setres ",
    "CalledByGod",
    "B Komachi",
    "Adina and Friends",
    "TUYUL",
]

fields = [
    'Rank',
    'Name',
    'Total Point',
    'Total TK',
    'Avg TK',
    'Avg Placement',
    'Avg Placement Point',
    'Games Played'
]
