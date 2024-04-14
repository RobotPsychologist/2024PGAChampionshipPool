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
    ldbrd_df = dfs[0]
    ldbrd_df = ldbrd_df.loc[~ldbrd_df.map(lambda x: ('cut' in str(x)) or ('CUT' in str(x))).any(axis=1)]
    ldbrd_df = ldbrd_df.loc[~ldbrd_df.map(lambda x: 'Projected' in str(x)).any(axis=1)]
    return ldbrd_df

def keep_top_5_scores(df):
    '''Returns the lowest 5 scores for each group.'''
    return df.nsmallest(5, 'SCORE')

def convert_golf_scores(df):
    '''Converts the golf scores to integers.'''
    df['SCORE'] = df['SCORE'].apply(lambda x: int(x) if x != 'E' else 0)
    df['TODAY'] = df['TODAY'].apply(lambda x: int(x) if x != 'E' and x != '-' else 0)
    df['TOT'] = df['TOT'].apply(lambda x: int(x) if x != 'E' and x != '--'else 0) 
    
    # Subtract 3 from the score of the top player
    df.loc[df['POS'] == '1', 'SCORE'] = df.loc[df['POS'] == '1', 'SCORE'] - 3
    return df

# LOAD DATA TABLES
pulled_scores = pull_scores()
#st.dataframe(pulled_scores)
df_masters = convert_golf_scores(df=pulled_scores)
#st.dataframe(df_masters)
team_selections_df = pd.read_csv(TEAM_SELECTIONS_PATH)
score_cards = pd.merge(team_selections_df,
                       df_masters,
                       how='left',
                       left_on='mst_player',
                       right_on='PLAYER')
top_5_df = score_cards.groupby('pool_player_name').apply(keep_top_5_scores, include_groups = False)
#.reset_index(drop=True)
#top_5_df = score_cards.groupby('pool_player_name')['SCORE'].nsmallest(5)
#top_5_df = score_cards.groupby('pool_player_name', group_keys=False).apply(keep_top_5_scores)
#top_5_df=score_cards.groupby('pool_player_name',group_keys=False).apply(lambda grp:grp.nsmallest(n=5,columns='SCORE').sort_index())
#st.dataframe(top_5_df)
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

st.write("## Compare Players :scales:")
compare1, compare2 = st.columns(2)
players = score_cards['pool_player_name'].unique()
column_configs = {"TOT": st.column_config.NumberColumn("TOTAL"),
                  "group_number": st.column_config.NumberColumn("G#"),
                  "mst_player": st.column_config.TextColumn("GOLFER", width="medium"),
                  "SCORE": st.column_config.NumberColumn("SCORE"),
                  "TODAY": st.column_config.NumberColumn("TODAY"),
                  "THRU": st.column_config.TextColumn("THRU")
                  }

with compare1:
    selected_score1 = st.selectbox(
        'Select player:',
        result_df['pool_player_name'].unique(),
        key='score1'   
    )
    # Filter the DataFrame based on the selected score
    filtered_df1 = score_cards[(score_cards['pool_player_name'] == selected_score1)]
    # Display the filtered DataFrame
    st.dataframe(filtered_df1[['group_number','POS','mst_player','SCORE','TODAY','THRU','R1','R2','R3','R4','TOT']],
                 use_container_width=True, 
                 hide_index=True,
                 column_config=column_configs)
    
with compare2:
    selected_score2 = st.selectbox(
        'Select player:',
        result_df['pool_player_name'].unique(),
        key='score2'   
    )
    # Filter the DataFrame based on the selected score
    filtered_df2 = score_cards[(score_cards['pool_player_name'] == selected_score2)]
    # Display the filtered DataFrame
    st.dataframe(filtered_df2[['group_number','POS','mst_player','SCORE','TODAY','THRU','R1','R2','R3','R4','TOT']],
                 use_container_width=True, 
                 hide_index=True,
                 column_config=column_configs)