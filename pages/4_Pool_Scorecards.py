
import streamlit as st
from utils.background_images import set_bg_hack
import pandas as pd
from math import floor

st.set_page_config(
    page_title="Pool Scorecards",
    page_icon=":golf:",
    layout='wide',
)

LOGO_IMAGE_PATH = 'images/MastersTournamentLogo.png'
st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)


st.write("# Pool Scorecards :1234:")
set_bg_hack('images/augusta_6th_hole.png')

# CONSTANTS
PLAYER_LIST = ['Jeff Cain','Barry Ferguson','Ryan Ferguson','Shaun Ferguson','Duncan Fraser','Jordan Gleed',
              'Dave Hanson','Jason Knight','Jaideep Lal','Tazim Lal','Jamie McCarthy','Troy McCann',
              'Alex Monk','Jim Morrison','Kyle Morrison','Rosemary Morrison','Christopher Readshaw','Patrick Readshaw',
              'Pam Readshaw','Paul Readshaw','Christopher Risi','Frank Risi','Ali Robitaille','Jeff Wand']
TEAM_SELECTIONS_PATH = 'tables/pool_team_selections.csv'
team_count = len(PLAYER_LIST)
column_count = floor(team_count / 4)
column_4_count = column_count - (team_count % 4)

# FUNCTION DEFINITIONS
def pull_scores(url='https://www.espn.com/golf/leaderboard'):
    '''Pulls the current scores from the ESPN leaderboard and returns a dataframe with the scores'''
    dfs = pd.read_html(url)
    return dfs[0]

def team_selection_table(team, pool_team_selections_df, pool_player_names_df=PLAYER_LIST):
    '''Displays the team selection table with populated scores for a given team'''
    pool_player_name = pool_player_names_df[team]
    st.write(f"### {pool_player_name}")
    st.dataframe(pool_team_selections_df.loc[pool_team_selections_df['pool_player_name'] == pool_player_name, ['group_number','POS', 'mst_player','SCORE','TODAY','THRU','TOT']],
                 hide_index=True,
                 use_container_width=True,
                 column_config={
                        "group_number": st.column_config.NumberColumn("G#", width="small"),
                        "mst_player": st.column_config.TextColumn("Golfer", width="small"),
                        "TOT": st.column_config.NumberColumn(
                            "Total",
                            width="small",
                            min_value=-100,
                            max_value=1500,
                            step=1,
                        )
                    }
                )
 
df_masters = pull_scores()
team_selections_df = pd.read_csv(TEAM_SELECTIONS_PATH)   

score_cards = pd.merge(team_selections_df, df_masters, how='left', left_on='mst_player', right_on='PLAYER') 

team_row1, team_row2, team_row3, team_row4 = st.columns([0.25 , 0.25, 0.25, 0.25])

with team_row1:
    for team1 in range(0, column_count):
        team_selection_table(team=team1, pool_team_selections_df=score_cards)
with team_row2:
    for team2 in range(column_count, 2*column_count):
        team_selection_table(team=team2, pool_team_selections_df=score_cards)
        
with team_row3:
    for team3 in range(2*column_count, 3*column_count):
        team_selection_table(team=team3, pool_team_selections_df=score_cards)
        
with team_row4:
    for team4 in range(3*column_count, 3*column_count+column_4_count):
        team_selection_table(team=team4, pool_team_selections_df=score_cards)