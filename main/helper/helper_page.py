# -*- coding: utf-8 -*-
import pandas as pd


def set_df(id, name):
    url = (
        f"https://docs.google.com/spreadsheets/d/{id}/gviz/tq?tqx=out:csv&sheet={name}"
    )
    df = pd.read_csv(url)
    # iloc function: start_row:end_row, start_column:end_column
    df = df.iloc[1:11, 1:9]

    df.rename(
        columns={
            "Unnamed: 1": "Rank",
            "Unnamed: 2": "Name",
            "Unnamed: 3": "Total Point",
            "Unnamed: 4": "Total TK",
            "Unnamed: 5": "Avg TK",
            "Unnamed: 6": "Avg Placement",
            "Unnamed: 7": "Avg Placement Point",
            "Unnamed: 8": "Games Played",
        },
        inplace=True,
    )

    return df


def get_by_team(df, team, field):
    row = df.loc[df["Name"] == team]
    return row[field].values[0]


def get_by_rank(df, rank, field):
    row = df.iloc[rank - 1 : rank]
    return row[field].values[0]


def get_games_played(df):
    num = max(df["Games Played"].values)
    return num


def print_leaderboard_data(df):
    lbtable = """
|  Rank  | Team Name             | Total Kill | **Points** |
|:-------|:----------------------|:-----------|:-----------|
"""

    for count in range(len(df)):
        count = count + 1
        rank_team = get_by_rank(df, count, "Name")
        rank_kill = get_by_rank(df, count, "Total TK")
        rank_poin = get_by_rank(df, count, "Total Point")

        if count <= 3:
            rank = (
                "| #**"
                + str(count)
                + "** | **"
                + str(rank_team)
                + "** | "
                + str(int(rank_kill))
                + " | **"
                + str(int(rank_poin))
                + "** | \n"
            )
        else:
            rank = (
                "| #**"
                + str(count)
                + "** | "
                + str(rank_team)
                + " | "
                + str(int(rank_kill))
                + " | "
                + str(int(rank_poin))
                + " | \n"
            )

        lbtable = lbtable + rank

    return lbtable


def set_leaderboard_page(df):
    leaderboard_md = """---
layout: default
---

[< Home](https://kanziebub.github.io/SurvivalProtocol/)

# **Leaderboard**

"""
    leaderboard_md = (
        leaderboard_md + "### Games Played = " + str(int(get_games_played(df))) + "\n"
    )

    leaderboard_md = leaderboard_md + print_leaderboard_data(df)

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

    #     script = """
    # <script>
    # ```js script
    #   // Define a function to execute the script
    #     function executePythonScript() {
    #         $.ajax({
    #             type:'POST',
    #             url:'leaderboard.py',
    #             success: function(data) {
    #                 console.log(data)
    #             };
    #         });
    #     }

    #     // Run the script when the page is fully loaded
    #     $(document).ready(function() {
    #         executePythonScript();
    #     });
    # ```
    # """

    leaderboard_md = leaderboard_md + penalty + home
    return leaderboard_md

    # ---------------------------------
