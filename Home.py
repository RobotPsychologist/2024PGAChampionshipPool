'''This is the entrypoint file for the pool dashboard. 
'''

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Home",
    page_icon=":golf:",
    layout='wide',
)

TOURNAMENT_NAME_LOOKUP = 'pga_championship'
TOURNAMENT_NAME_LABEL = 'PGA Championship'
YEAR_LABEL = '2024'
LOGO_IMAGE_PATH = f'images/{TOURNAMENT_NAME_LOOKUP}/TournamentLogo.png'

st.write(f"# {YEAR_LABEL} {TOURNAMENT_NAME_LABEL} Pool :man-golfing:")



st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)

st.markdown('''
            ## Details & Rules
            We’re once again offering a team selection twist for everyone.

            Given his dominance, we’ve decide to make Scheffler the inflection point in this pool – so you have a simple choice:

                1. Choose Scottie Scheffler and forego any Group 1 picks – then choose 1 player from the remaining 9 slots for a total of 10 players.
                2. Neglect Scottie Scheffler but instead choose two players from Group 1 and one player from the remaining 9 slots for a total of 11 players.           

            Hopefully that is straightforward enough?

            Looking forward to seeing where the picks fall.

            Be sure to take a close look at future 15X Major Winner Talor Gooch who is a bargain in Group 5!    
            
            ### Scoring System
            No matter which path you choose, only your Top 5 players will count towards your team's score (with the Field Approach you simply have one more player to draw from).
            
            The winner of the pool will be the team with the lowest combined score to par from their top 5 players.
            A 3-shot bonus (-3) will be applied if you select the winner.
            Teams must have a minimum of 5 players make the cut to qualify for prizing.
            
            ### Post Picks Update
            Looks like the conditions are going to be soft and wet, which should bring the field closer together.
            We have 23 teams participating and it seems the cost of a tired new father Scheffler was too much for most of the pool - only 4 Teams are rolling the dice on the World #1.

            With our field now set, we’ll payout the winnings as follows:

            First Place     \$300
            Second Place    \$150
            Third Place     \$125
            ''')



course_table = {
    "Hole": [1, 2, 3, 4, 5, 6, 7, 8, 9, "Out", 10, 11, 12, 13, 14, 15, 16, 17, 18, "In", "Total"],
    "Name": ["Cut the Corner", "The Ridge", "Floyds Fork", "Short 'n Sweet", "Fade Away", "The Bear", "Players Pick", "Thor's Hammer", "The Rise", "", "Turns", "On the Edge", "Odin's Revenge", "The Island", "Two Tears", "On the Rocks", "Down the Stretch", "No Mercy", "Gahm Over", "", ""],
    "Yards": [484, 500, 208, 372, 463, 495, 597, 190, 415, 3724, 590, 211, 494, 351, 254, 435, 508, 472, 570, 3885, 7609],
    "Par": [4, 4, 3, 4, 4, 4, 5, 3, 4, 35, 5, 3, 4, 4, 3, 4, 4, 4, 5, 36, 71]
}

df_course_table = pd.DataFrame(course_table)

st.table(df_course_table)