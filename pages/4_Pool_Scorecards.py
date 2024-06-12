
import streamlit as st
from utils.background_images import set_bg_hack
import pandas as pd
from math import floor

st.set_page_config(
    page_title="Pool Scorecards",
    page_icon=":golf:",
    layout='wide',
)

# GLOBAL CONSTANTS
TOURNAMENT_NAME_LOOKUP = 'us_open'
TOURNAMENT_NAME_LABEL = 'US Open'
YEAR_LABEL = '2024'

LOGO_IMAGE_PATH = f'images/{TOURNAMENT_NAME_LOOKUP}/TournamentLogo.png'
st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)


st.write(f"# {YEAR_LABEL} {TOURNAMENT_NAME_LABEL} Pool Scorecards :1234:")
#set_bg_hack('images/augusta_6th_hole.png')

# DATA PREPARATION
team_selections_path = f'tables/{TOURNAMENT_NAME_LOOKUP}/pool_picks.csv'
df_player_picks = pd.read_csv(f'tables/{TOURNAMENT_NAME_LOOKUP}/pool_picks.csv')
player_list = df_player_picks['player'].unique().tolist()
st.dataframe(player_list)
team_count = len(player_list)
column_count = floor(team_count / 4)
column_4_count = column_count - (team_count % 4)

# FUNCTION DEFINITIONS
def pull_scores(url='https://www.espn.com/golf/leaderboard'):
    '''Pulls the current scores from the ESPN leaderboard and returns a dataframe with the scores'''
    dfs = pd.read_html(url)
    return dfs[0]

def team_selection_table(team, pool_team_selections_df, pool_player_names_df=player_list):
    '''Displays the team selection table with populated scores for a given team'''
    pool_player_name = pool_player_names_df[team]
    st.write(f"### {pool_player_name}")
    try:
        col_select = ['group_number','POS', 'golfer','SCORE','TODAY','THRU','TOT']
        st.dataframe(pool_team_selections_df.loc[pool_team_selections_df['player'] == pool_player_name,
                                                col_select],
                    hide_index=True,
                    use_container_width=True,
                    column_config={
                            "group_number": st.column_config.NumberColumn("G#"),
                            "golfer": st.column_config.TextColumn("GOLFER", width="medium"),
                            "TOT": st.column_config.NumberColumn(
                                "Total",
                                width="small",
                                min_value=-100,
                                max_value=1500,
                                step=1,
                            )
                        }
                    )
    except:
        st.write("Wating for tournament to start or data loading erorr...")
        col_select = ['group_number', 'golfer','TEE TIME']
        st.dataframe(pool_team_selections_df.loc[pool_team_selections_df['player'] == pool_player_name,
                                        col_select],
            hide_index=True,
            use_container_width=True,
            column_config={
                    "group_number": st.column_config.NumberColumn("G#"),
                    "golfer": st.column_config.TextColumn("GOLFER", width="medium"),
                    "TEE TIME": st.column_config.TextColumn("Tee Time", width="small"),
                    
                }
            )
 
df_golfers = pull_scores()
score_cards = pd.merge(df_player_picks, df_golfers, how='left', left_on='golfer', right_on='PLAYER') 

team_row1, team_row2, team_row3, team_row4 = st.columns([0.25 , 0.25, 0.25, 0.25])

split_count = team_count // 4
split_count += 1
remainder = team_count - split_count


with team_row1:
    for team1 in range(0, split_count):
        team_selection_table(team=team1, pool_team_selections_df=score_cards)
with team_row2:
    for team2 in range(split_count, 2*split_count):
        team_selection_table(team=team2, pool_team_selections_df=score_cards)
        
with team_row3:
    for team3 in range(2*split_count, 3*split_count):
        team_selection_table(team=team3, pool_team_selections_df=score_cards)
        
with team_row4:
    for team4 in range(3*split_count, 3*split_count+remainder):
        team_selection_table(team=team4, pool_team_selections_df=score_cards)