'''This is the entrypoint file for the 2024 Masters Pool dashboard. 
'''

import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":golf:",
    layout='wide',
)

st.write("# 2024 Masters Pool :man-golfing:")

LOGO_IMAGE_PATH = 'images/MastersTournamentLogo.png'
st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)

st.markdown('''
            ## Details & Rules
            Welcome to the 2024 Masters Pool!
            This year's pool will be just as easy as years past, but with a new choose-your-own-adventure team selection process.
            
            ### New Selection Format: Favourites or Field
            This year, you will have the option to play build a team of 10 or 11, depending on how your want to hedge your bets!
            
            | Bet the Favourites      | Bet the Field |
            | ----------- | ----------- |
            | Select 2 players from each group for a total of 10 players (the regular selection process)      | Select only 1 player from Group 1 but then select a third player twice in any remaining group (total of 11 players)      |.

            
            ### Scoring System
            No matter which path you choose, only your Top 5 players will count towards your team's score (with the Field Approach you simply have one more player to draw from).
            
            The winner of the pool will be the team with the lowest combined score to par from their top 5 players.
            A 3-shot bonus (-3) will be applied if you select the winner.
            Teams must have a minimum of 5 players make the cut to qualify for prizing.
            
            ### Entry Details
            Team Entry Cost $25 (hold until post tournament).
            Theams must be submitted on or before Tuesday April 9th at 9:00pm EST to <morrison.kylejames@gmail.com>.
            ''')

