'''This is the pool leaderboards. 
'''

import streamlit as st
from utils.background_images import set_bg_hack
import pandas as pd

st.set_page_config(
    page_title="Pool Leaderboard",
    page_icon=":golf:",
    layout='wide',
)

st.write("# Pool Leaderboard :trophy:")

LOGO_IMAGE_PATH = 'images/MastersTournamentLogo.png'
st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)

set_bg_hack('images/augusta_6th_hole.png')

TEAM_SELECTIONS_PATH = 'tables/pool_team_selections.csv'

# FUNCTION DEFINITIONS
def pull_scores(url='https://www.espn.com/golf/leaderboard'):
    '''Pulls the current scores from the ESPN leaderboard and returns a dataframe with the scores'''
    dfs = pd.read_html(url)
    return dfs[0]

def keep_top_5_scores(df):
    '''Returns the top 5 scores for each group.'''
    return df.nsmallest(5, 'SCORE')

def convert_golf_scores(df):
    '''Converts the golf scores to integers.'''
    df['SCORE'] = df['SCORE'].apply(lambda x: int(x) if x != 'E' else 0)
    df['TODAY'] = df['TODAY'].apply(lambda x: int(x) if x != 'E' and x != '-' else 0)
    df['TOT'] = df['TOT'].apply(lambda x: int(x) if x != 'E' and x != '--'else 0) 
    return df

# LOAD DATA TABLES
df_masters = convert_golf_scores(df=pull_scores())
team_selections_df = pd.read_csv(TEAM_SELECTIONS_PATH)   
score_cards = pd.merge(team_selections_df, 
                       df_masters, 
                       how='left', 
                       left_on='mst_player', 
                       right_on='PLAYER') 
top_5_df = score_cards.groupby('pool_player_name').apply(keep_top_5_scores).reset_index(drop=True)

#st.table(top_5_df)
# Group by 'pool_player_name' again and sum the 'total'
result = top_5_df.groupby('pool_player_name')[['SCORE', 'TODAY','TOT']].sum()

# Convert the result to a DataFrame
result_df = result.reset_index()

# Display the DataFrame
st.dataframe(result_df,    
             column_config={
                "TOT": st.column_config.NumberColumn(
                    "TOTAL",
                    width="small",
                    help="The aggregated Total score for the top 5 players.",
                    min_value=-100,
                    max_value=1500,
                    step=1),
                "pool_player_name": st.column_config.TextColumn(
                    "Player", width="medium")
                },
             height=900,use_container_width=True, hide_index=True)
# Display the DataFrame
#st.table(df.groupby('pool_player_name')['total'].nsmallest(5))