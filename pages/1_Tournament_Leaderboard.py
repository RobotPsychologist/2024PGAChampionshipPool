'''This is the players leaderboard, the data displayed here is used to calculate the pool scores. 
'''

import streamlit as st
from utils.background_images import set_bg_hack
import pandas as pd

st.set_page_config(
    page_title="Player Leaderboard",
    page_icon=":golf:",
    layout='wide',
)

TOURNAMENT_NAME_LOOKUP = 'us_open'
TOURNAMENT_NAME_LABEL = 'US Open'
YEAR_LABEL = '2024'

st.write(f"# {YEAR_LABEL} {TOURNAMENT_NAME_LABEL} Pool Live Results :man-golfing:")

LOGO_IMAGE_PATH = f'images/{TOURNAMENT_NAME_LOOKUP}/TournamentLogo.png'
st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)

#set_bg_hack("images/augusta_13th_hole.png")

# Load the data from ESPN
url = 'https://www.espn.com/golf/leaderboard'

# Read the HTML tables into a list of DataFrame objects
dfs = pd.read_html(url)

# The first table
df = dfs[0]

# Display the DataFrame
st.dataframe(df[['POS','PLAYER','SCORE','TODAY','THRU','R1','R2','R3','R4','TOT']],hide_index=True, use_container_width=True, height=800)

# Read the CSV file
#df = pd.read_csv('tables/masters_players.csv')

