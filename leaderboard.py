# Imports
import pandas as pd
import markdown

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

rank1team = get_by_rank(df, 1, "Name")
rank2team = get_by_rank(df, 2, "Name")
rank3team = get_by_rank(df, 3, "Name")
rank4team = get_by_rank(df, 4, "Name")
rank5team = get_by_rank(df, 5, "Name")
rank6team = get_by_rank(df, 6, "Name")
rank7team = get_by_rank(df, 7, "Name")
rank8team = get_by_rank(df, 8, "Name")

rank1poin = get_by_rank(df, 1, "Total Point")
rank2poin = get_by_rank(df, 2, "Total Point")
rank3poin = get_by_rank(df, 3, "Total Point")
rank4poin = get_by_rank(df, 4, "Total Point")
rank5poin = get_by_rank(df, 5, "Total Point")
rank6poin = get_by_rank(df, 6, "Total Point")
rank7poin = get_by_rank(df, 7, "Total Point")
rank8poin = get_by_rank(df, 8, "Total Point")
