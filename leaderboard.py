# Imports
import pandas as pd

def set_df(id, name):
    url = f'https://docs.google.com/spreadsheets/d/{id}/gviz/tq?tqx=out:csv&sheet={name}'
    df = pd.read_csv(url)
    df = df.iloc[1:11 , 1:9]

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

def get_games_played(df):
    num = max(df['Games Played'].values)
    return num

# =====================================================

def set_leaderboard_page(df):
    leaderboard_md = """---
layout: default
---

[< Home](https://kanziebub.github.io/SurvivalProtocol/)

# **Leaderboard**

"""
    leaderboard_md = leaderboard_md + "### Games Played = " + str(int(get_games_played(df))) + "\n"
    
    # ---------------------------------

    rank1team = get_by_rank(df, 1, "Name")
    rank2team = get_by_rank(df, 2, "Name")
    rank3team = get_by_rank(df, 3, "Name")
    rank4team = get_by_rank(df, 4, "Name")
    rank5team = get_by_rank(df, 5, "Name")
    rank6team = get_by_rank(df, 6, "Name")
    rank7team = get_by_rank(df, 7, "Name")
    rank8team = get_by_rank(df, 8, "Name")
    rank9team = get_by_rank(df, 9, "Name")
    rank10team = get_by_rank(df, 10, "Name")

    rank1kill = get_by_rank(df, 1, "Total TK")
    rank2kill = get_by_rank(df, 2, "Total TK")
    rank3kill = get_by_rank(df, 3, "Total TK")
    rank4kill = get_by_rank(df, 4, "Total TK")
    rank5kill = get_by_rank(df, 5, "Total TK")
    rank6kill = get_by_rank(df, 6, "Total TK")
    rank7kill = get_by_rank(df, 7, "Total TK")
    rank8kill = get_by_rank(df, 8, "Total TK")
    rank9kill = get_by_rank(df, 9, "Total TK")
    rank10kill = get_by_rank(df, 10, "Total TK")

    rank1poin = get_by_rank(df, 1, "Total Point")
    rank2poin = get_by_rank(df, 2, "Total Point")
    rank3poin = get_by_rank(df, 3, "Total Point")
    rank4poin = get_by_rank(df, 4, "Total Point")
    rank5poin = get_by_rank(df, 5, "Total Point")
    rank6poin = get_by_rank(df, 6, "Total Point")
    rank7poin = get_by_rank(df, 7, "Total Point")
    rank8poin = get_by_rank(df, 8, "Total Point")
    rank9poin = get_by_rank(df, 9, "Total Point")
    rank10poin = get_by_rank(df, 10, "Total Point")

    lbtable = """
|  Rank  | Team Name             | Total Kill | **Points** |
|:-------|:----------------------|:-----------|:-----------|
"""
    rank1 = "| #**1** | **" +str(rank1team)+ "** | " +str(int(rank1kill))+ " | **" +str(int(rank1poin))+ "** | \n"
    rank2 = "| #**2** | **" +str(rank2team)+ "** | " +str(int(rank2kill))+ " | **" +str(int(rank2poin))+ "** | \n"
    rank3 = "| #**3** | **" +str(rank3team)+ "** | " +str(int(rank3kill))+ " | **" +str(int(rank3poin))+ "** | \n"
    rank4 = "| #**4** | " +str(rank4team)+ " | " +str(int(rank4kill))+ " | " +str(int(rank4poin))+ " | \n"
    rank5 = "| #**5** | " +str(rank5team)+ " | " +str(int(rank5kill))+ " | " +str(int(rank5poin))+ " | \n"
    rank6 = "| #**6** | " +str(rank6team)+ " | " +str(int(rank6kill))+ " | " +str(int(rank6poin))+ " | \n"
    rank7 = "| #**7** | " +str(rank7team)+ " | " +str(int(rank7kill))+ " | " +str(int(rank7poin))+ " | \n"
    rank8 = "| #**8** | " +str(rank8team)+ " | " +str(int(rank8kill))+ " | " +str(int(rank8poin))+ " | \n"
    rank9 = "| #**9** | " +str(rank9team)+ " | " +str(int(rank9kill))+ " | " +str(int(rank9poin))+ " | \n"
    rank10 = "| #**10** | " +str(rank10team)+ " | " +str(int(rank10kill))+ " | " +str(int(rank10poin))+ " | \n"

    lbtable = lbtable + rank1 + rank2 + rank3 + rank4 + rank5 + rank6 + rank7 + rank8 + rank9 + rank10
    leaderboard_md = leaderboard_md + lbtable

    # ---------------------------------

    penalty = """
## Penalty Log

|  Game  | Team Name | Penalty | Reason                |
|:-------|:----------|:--------|:----------------------|
|        |           |         |                       |
    """

    home = """
[< Home](https://kanziebub.github.io/SurvivalProtocol/)
    """

    leaderboard_md = leaderboard_md + penalty + home
    return leaderboard_md

    # ---------------------------------

# =====================================================

def write_page(target, page_md):
    with open(target, 'w') as f:
        f.write(page_md)

def refresh_page(sheetID, target):
    sheetName = "ERCT"

    df = set_df(sheetID, sheetName)

    page_md = set_leaderboard_page(df)
    write_page(target, page_md)

# refresh_page()

# Tourney 12 Aug 2023
# https://docs.google.com/spreadsheets/d/1hLUR46LwreWo-B3oi1AsYvSiF_qvRxVAcUIpcUZcj9s/edit#gid=1885268704
# sheetID = "1hLUR46LwreWo-B3oi1AsYvSiF_qvRxVAcUIpcUZcj9s"
# target = "leaderboard.md"

# Tourney 19 Aug 2023
# https://docs.google.com/spreadsheets/d/1-oU56f4sAR4JJasuqFoxIqoH7humhXVhJuBwAMH5ZG0/edit#gid=1885268704

# Newbie Tourney 16 Sep 2023
# https://docs.google.com/spreadsheets/d/1Xos9Iojq58I-wSbZfjx4hX8QiWGCLupcLuZxerTebSs/edit?usp=sharing

# EPIC Invitational 30 Sep 2023
# https://docs.google.com/spreadsheets/d/1bb3O4pUtXvQ6jCWKcpB9-wCUlwL_jMRML8fYYN0PDs4/edit#gid=1885268704
# sheetID = "1bb3O4pUtXvQ6jCWKcpB9-wCUlwL_jMRML8fYYN0PDs4"
# target = "./Invitational/01/leaderboard.md"
# refresh_page(sheetID, target)
