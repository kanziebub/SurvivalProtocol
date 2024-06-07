# Imports
import pandas as pd

def set_df(id, name):
    url = f'https://docs.google.com/spreadsheets/d/{id}/gviz/tq?tqx=out:csv&sheet={name}'
    df = pd.read_csv(url, encoding='latin')
    df = df.iloc[1:19 , 1:9]

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

def get_header():
    head = """---
layout: default
---

[< Home](https://kanziebub.github.io/SurvivalProtocol/)

"""
    return head
    
def get_footer():
    home = """
[< Home](https://kanziebub.github.io/SurvivalProtocol/)
    """
    return home

def get_penalty_table():
    
    penalty = """
### Penalty Log

|  Game  | Team Name | Penalty | Reason                |
|:-------|:----------|:--------|:----------------------|
"""
    return penalty

# =====================================================
def set_penalty(game, team, penalty, reason):
    row = "| " + game + " | " + team + " | " + penalty + " | " + reason + " | \n"
    return row

def set_leaderboard(df, teams):
    leaderboard_md = "### Games Played = " + str(int(get_games_played(df))) + "\n"
    
    # ---------------------------------
    lbtable = """
|  Rank  | Team Name             | Total Kill | **Points** |
|:-------|:----------------------|:-----------|:-----------|
"""
    rows = ""
    for i in range (teams):
        rank = i+1
        rows+= get_data_by_rank(df, rank)

    lbtable = lbtable + rows
    page_md  = leaderboard_md + lbtable

    return page_md

    # ---------------------------------

def get_data_by_rank(df, rank):
    team = get_by_rank(df, rank, "Name")
    kill = get_by_rank(df, rank, "Total TK")
    poin = get_by_rank(df, rank, "Total Point")
    row = ""
    if (rank==1 or rank==2 or rank==3):
        row += "| #**"+str(rank)+"** | **" +str(team)+ "** | " +str(int(kill))+ " | **" +str(int(poin))+ "** | \n"
    else:
        row += "| #**"+str(rank)+"** | " +str(team)+ " | " +str(int(kill))+ " | " +str(int(poin))+ " | \n"
    return row

def get_custom_information():
    return (
"""
\n
### Bracket
- Group A
  - NANYA
  - Melon
  - Eclair
  - HnS
- Group B
  - Ijat
  - SIAPA
  - EzWins
  - GG
- Group C
  - BlmTau
  - YOLO
  - 66%ptk
  - NTR185
\n
### Match-up
```
Round 1: BC 
Round 2: AB 
Round 3: AC 
Round 4: BC 
Round 5: AB 
Round 6: AC
```
\n
""")
# =====================================================

def write_page(target, page_md):
    with open(target, 'w') as f:
        f.write(page_md)

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

# EPIC S2 Open 21-22 Oct 2023
    # Qualifiers
        # https://docs.google.com/spreadsheets/d/10RBhnE8PJ9X_UExNlVg1IV6HYb16Nqs36p5g-IN3RAc/edit#gid=1881109526
        # https://docs.google.com/spreadsheets/d/1OTA3LYuiDxJ47vyKfvIR5jFOT6fT7IapwQFE2fKfWHI/edit#gid=1881109526
    # Finals
        # https://docs.google.com/spreadsheets/d/1hCN56fy0dOZrc9UxU5WaiqpW5sjfiXSH9P2W_bPCaZE/edit#gid=1885268704 

# EPIC S3 Open 25 Nov & 2 Dec 2023
    # Qualifiers
        # https://docs.google.com/spreadsheets/d/1SSutJKrwf2y9mgj8sUqXzdvLkA0P-SSbA_RbyH5N4-o/edit?usp=sharing
        # https://docs.google.com/spreadsheets/d/1rgwbKUNxfOgDte29NnJ9Rmfg2Umz6qzpO1Qk2-D1l4o/edit?usp=sharing
    # Finals
        # https://docs.google.com/spreadsheets/d/1-xXH_T36FAajsApcl4k_Ha1aT-5VR2hhLfNJLVI7rys/edit#gid=1885268704

# Newbie Tournament 2.0 20 Jan 2024
    # https://docs.google.com/spreadsheets/d/1_74atS-on-fS4X7jvD9HxBlikC4y0ZtSPeW-rHke8G8/edit#gid=1885268704  

# EPIC S4 Open 8 Jun
    # Qualifiers
        # https://docs.google.com/spreadsheets/d/19vkPDGKtBVXdP0xaxhVR9pVelrj1FDEQr5hrpQZ6Ji4/edit?gid=1885268704#gid=1885268704
    # Finals  
        # 
        
def single():
    target = "./EPIC/04/qualifiers.md"
    sheetID = "19vkPDGKtBVXdP0xaxhVR9pVelrj1FDEQr5hrpQZ6Ji4"
    sheetName = "ERCT"
    penalty_placeholder = "|        |           |         |                       | \n"

    df = set_df(sheetID, sheetName)
    leaderboard = ("""
# **Leaderboard**

""" + set_leaderboard(df, 12) 
    + get_penalty_table() 
    + penalty_placeholder
    # + set_penalty("a", "a", "aa", "otp") 
    + " \n \n")

    page_md = (  get_header() 
               + leaderboard
               + get_custom_information()
               + get_footer()
               )
    write_page(target, page_md)
    
def double():
    target = "./EPIC/03/qualifiers.md"
    sheetA = "1SSutJKrwf2y9mgj8sUqXzdvLkA0P-SSbA_RbyH5N4-o"
    sheetB = "1rgwbKUNxfOgDte29NnJ9Rmfg2Umz6qzpO1Qk2-D1l4o"
    sheetName = "ERCT"
    penalty_placeholder = "|        |           |         |                       | \n"

    df_A = set_df(sheetA, sheetName)
    df_B = set_df(sheetB, sheetName)

    leaderboard_A = ("""
# **Lobby A Leaderboard**

""" + set_leaderboard(df_A, 7) 
    + get_penalty_table() 
    + penalty_placeholder
    # + set_penalty("", "", "", "") 
    + " \n \n")
    leaderboard_B = ("""
# **Lobby B Leaderboard**

""" + set_leaderboard(df_B, 7) 
    + get_penalty_table() 
    # + penalty_placeholder
    # + set_penalty("B04", "TILT", "-2", "Non-Player Death") 
    + " \n \n")

    page_md = (get_header() 
               + leaderboard_A
               + leaderboard_B
               + get_footer())
    write_page(target, page_md)

def main():
    single()

main()
