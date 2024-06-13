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

# GLOBAL CONSTANTS
TOURNAMENT_NAME_LOOKUP = 'us_open'
TOURNAMENT_NAME_LABEL = 'US Open'
YEAR_LABEL = '2024'
LOGO_IMAGE_PATH = f'images/{TOURNAMENT_NAME_LOOKUP}/TournamentLogo.png' # sidebar image location
TEAM_SELECTIONS_PATH = f'tables/{TOURNAMENT_NAME_LOOKUP}/pool_picks.csv' # data location

st.write(f"# {YEAR_LABEL} {TOURNAMENT_NAME_LABEL} Pool Leaderboard :trophy:")
st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)

# FUNCTION DEFINITIONS
def pull_scores(url='https://www.espn.com/golf/leaderboard'):
    '''Pulls the current scores from the ESPN leaderboard and returns a dataframe with the scores'''
    dfs = pd.read_html(url)
    ldbrd_df = dfs[0]
    ldbrd_df = ldbrd_df.loc[~ldbrd_df.map(lambda x: ('cut' in str(x)) or ('WD' in str(x)) or ('CUT' in str(x))).any(axis=1)]
    ldbrd_df = ldbrd_df.loc[~ldbrd_df.map(lambda x: 'Projected' in str(x)).any(axis=1)]
    return ldbrd_df

def keep_top_5_scores(df):
    '''Returns the lowest 5 scores for each group.'''
    return df.nsmallest(5, 'SCORE')

def convert_golf_scores(df):
    '''Many data sources come in mixed data formats. This function converts the scores to integers.'''
    df['SCORE'] = df['SCORE'].apply(lambda x: int(x) if x != 'E' and x != '-' else 0)
    df['TODAY'] = df['TODAY'].apply(lambda x: int(x) if x != 'E' and x != '-' else 0)
    df['TOT'] = df['TOT'].apply(lambda x: int(x) if x != 'E' and x != '--'else 0) 
    
    # Subtract 3 from the score of the top player (Bonus for picking the tournament leader)
    df.loc[df['POS'] == '1', 'SCORE'] = df.loc[df['POS'] == '1', 'SCORE'] - 3
    return df

# LOAD DATA TABLES
pulled_scores = pull_scores()

try:
    df_golfers = convert_golf_scores(df=pulled_scores)
except:
    st.write('Error: Could not pull the scores from data source. Please try again later.')
    st.stop()


team_selections_df = pd.read_csv(TEAM_SELECTIONS_PATH)
score_cards = pd.merge(team_selections_df,
                       df_golfers,
                       how='left',
                       left_on='golfer',
                       right_on='PLAYER')
top_5_df = score_cards.groupby('player').apply(keep_top_5_scores, include_groups = False)

# Group by 'pool_player_name' again and sum the 'total'
result = top_5_df.groupby('player')[['SCORE', 'TODAY','TOT']].sum()

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
                "player": st.column_config.TextColumn(
                    "Player", width="medium")
                },
             height=900,use_container_width=True, hide_index=True)

st.write('Note: The TODAY column does not include the 3 shot bonus for the tournament leader. The SCORE column does include the 3 shot bonus automatically.')


st.write("## Compare Players :scales:")
compare1, compare2 = st.columns(2)
players = score_cards['player'].unique()
column_configs = {"TOT": st.column_config.NumberColumn("TOTAL"),
                  "group_number": st.column_config.NumberColumn("G#"),
                  "golfer": st.column_config.TextColumn("GOLFER", width="medium"),
                  "SCORE": st.column_config.NumberColumn("SCORE"),
                  "TODAY": st.column_config.NumberColumn("TODAY"),
                  "THRU": st.column_config.TextColumn("THRU")
                  }

with compare1:
    selected_score1 = st.selectbox(
        'Select player:',
        result_df['player'].unique(),
        key='score1'   
    )
    # Filter the DataFrame based on the selected score
    filtered_df1 = score_cards[(score_cards['player'] == selected_score1)]
    # Display the filtered DataFrame
    st.dataframe(filtered_df1[['group_number','POS','golfer','SCORE','TODAY','THRU','R1','R2','R3','R4','TOT']],
                 use_container_width=True, 
                 hide_index=True,
                 column_config=column_configs)
    
with compare2:
    selected_score2 = st.selectbox(
        'Select player:',
        result_df['player'].unique(),
        key='score2'   
    )
    # Filter the DataFrame based on the selected score
    filtered_df2 = score_cards[(score_cards['player'] == selected_score2)]
    # Display the filtered DataFrame
    st.dataframe(filtered_df2[['group_number','POS','golfer','SCORE','TODAY','THRU','R1','R2','R3','R4','TOT']],
                 use_container_width=True, 
                 hide_index=True,
                 column_config=column_configs)