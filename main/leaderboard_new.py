# -*- coding: utf-8 -*-
# Imports
from helper import helper_page as page


def write_page(target, page_md):
    with open(target, 'w') as f:
        f.write(page_md)

def refresh_page(sheetID, target):
    sheetName = "ERCT"

    df = page.set_df(sheetID, sheetName)

    page_md = page.set_leaderboard_page(df)
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
sheetID = "1bb3O4pUtXvQ6jCWKcpB9-wCUlwL_jMRML8fYYN0PDs4"
target = "./main/view/leaderboard.md"
refresh_page(sheetID, target)
