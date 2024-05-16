'''This is the player selections from the pool participants. 
'''

import streamlit as st
import pandas as pd
from utils.background_images import set_bg_hack

TOURNAMENT_NAME_LOOKUP = 'pga_championship'
TOURNAMENT_NAME_LABEL = 'PGA Championship'
YEAR_LABEL = '2024'

st.set_page_config(
    page_title=f"{YEAR_LABEL} {TOURNAMENT_NAME_LABEL} Team Selections",
    page_icon=":golf:",
    layout='wide',
)

st.write("# Team Selections :abacus:")
#set_bg_hack("images/clubhouse.png")
LOGO_IMAGE_PATH = f'images/{TOURNAMENT_NAME_LOOKUP}/TournamentLogo.png'
st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)

group1, group2 = st.columns([0.5 , 0.5]) #group2 [0.2 , 0.2, 0.2, 0.2, 0.2]

df = pd.read_csv(f'tables/{TOURNAMENT_NAME_LOOKUP}/group_counts.csv')
df.drop(columns=['espn_check'], inplace=True)

total_groups = df['group_number'].nunique()
split_num = total_groups // 2

with group1:
    for i in range(0, total_groups+1):
        st.write(f"### Group {i}")
        st.dataframe(df[df['group_number'] == i], hide_index=True, use_container_width=True)
        if split_num == i:
            break

with group2:
    for i in range(split_num+1, total_groups):
        st.write(f"### Group {i}")
        st.dataframe(df[df['group_number'] == i], hide_index=True, use_container_width=True)
