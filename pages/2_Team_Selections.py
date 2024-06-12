'''This is the player selections from the pool participants. 
'''

import streamlit as st
import pandas as pd
from utils.background_images import set_bg_hack

TOURNAMENT_NAME_LOOKUP = 'us_open'
TOURNAMENT_NAME_LABEL = 'US Open'
YEAR_LABEL = '2024'

st.set_page_config(
    page_title=f"{YEAR_LABEL} {TOURNAMENT_NAME_LABEL} Team Selections",
    page_icon=":golf:",
    layout='wide',
)

# ESPN DATA LOAD FOR GROUP DISPLAY
## Load the data from ESPN
url = 'https://www.espn.com/golf/leaderboard'

## Read the HTML tables into a list of DataFrame objects
web_leaderboard_dfs = pd.read_html(url)

## The first table
web_leaderboard_df = web_leaderboard_dfs[0]

st.write("# Team Selections :abacus:")
#set_bg_hack("images/clubhouse.png")
LOGO_IMAGE_PATH = f'images/{TOURNAMENT_NAME_LOOKUP}/TournamentLogo.png'
st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)

group1, group2 = st.columns([0.5 , 0.5]) #group2 [0.2 , 0.2, 0.2, 0.2, 0.2]

df = pd.read_csv(f'tables/{TOURNAMENT_NAME_LOOKUP}/group_counts.csv')
df.drop(columns=['espn_check'], inplace=True)

df = pd.merge(df,
            web_leaderboard_df,
            how='left',
            left_on='golfer',
            right_on='PLAYER')

total_groups = df['group_number'].nunique()
split_num = total_groups // 2

COLUMN_CONFIG_CLEAN={'golfer': st.column_config.TextColumn('Golfer', width='medium'),      
                'pick_count': st.column_config.NumberColumn('Pick Count', width='small'),
                'TOT': st.column_config.NumberColumn('Total', width='small'),
                "THRU": st.column_config.TextColumn("THRU")
                    }

COLUMN_CONFIG_ERROR={'golfer': st.column_config.TextColumn('Golfer', width='medium'),      
                'pick_count': st.column_config.NumberColumn('Pick Count', width='small'),
                'group_number': st.column_config.NumberColumn('Group', width='small'),
                'TEE TIME': st.column_config.TextColumn('Tee Time', width='small'),
                    }

try:
    with group1:
        for i in range(1, total_groups+1):
            st.write(f"### Group {i}")
            st.dataframe(df[df['group_number'] == i][['golfer', 'pick_count','THRU','SCORE', 'TODAY','R1','R2','R3','R4','TOT']], hide_index=True, use_container_width=True, column_config=COLUMN_CONFIG_ERROR)
            if split_num == i:
                break

    with group2:
        for i in range(split_num+1, total_groups+1):
            if i != 6:
                st.write(f"### Group {i}")
            else:
                st.write(f"### Group Q")
            st.write(f"### Group {i}")
            st.dataframe(df[df['group_number'] == i][['golfer', 'pick_count','THRU','SCORE', 'TODAY','R1','R2','R3','R4','TOT']], hide_index=True, use_container_width=True, column_config=COLUMN_CONFIG_ERROR)

except:
    st.write('If you see this message the tournament hasn\'t started or there was an error loading the data, please contact Christopher or try again later. Thank you!')


    with group1:
        for i in range(1, total_groups+1):
            if i != 1:
                st.write(f"### Group {i}")
            st.dataframe(df[df['group_number'] == i][['golfer', 'pick_count', 'TEE TIME']], hide_index=True, use_container_width=True, column_config=COLUMN_CONFIG_ERROR)
            if split_num == i:
                break

    with group2:
        for i in range(split_num+1, total_groups+1):
            if i != 6:
                st.write(f"### Group {i}")
            else:
                st.write(f"### Group Q")
            st.dataframe(df[df['group_number'] == i][['golfer', 'pick_count', 'TEE TIME']], hide_index=True, use_container_width=True, column_config=COLUMN_CONFIG_ERROR)