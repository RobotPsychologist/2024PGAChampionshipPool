'''This is the entrypoint file for the pool dashboard. 
'''

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Home",
    page_icon=":golf:",
    layout='wide',
)

TOURNAMENT_NAME_LOOKUP = 'us_open'
TOURNAMENT_NAME_LABEL = 'US Open'
YEAR_LABEL = '2024'
LOGO_IMAGE_PATH = f'images/{TOURNAMENT_NAME_LOOKUP}/TournamentLogo.png'

st.write(f"# {YEAR_LABEL} {TOURNAMENT_NAME_LABEL} Pool :man-golfing:")



st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)

st.markdown('''
            ## Details & Rules
            Once again we switched up the format here to keep everyone on their toes.

            This format favors the favourites … we’re going to make the pool top-heavy with “big players” and rely less on the mules in the field.

            Everyone will build a team of 10 players, but with 4 from the marquee first group, two from the second, and one from each of the remaining.

            Your team must also include a player who “Monday qualified” for the tournament this week during Golf's Longest Day (final group) – and there are some relevant names in that mix.

            Don’t toss the qualifier pick away either, in 2005 New Zealand’s Michael Campbell qualified for Pinehurst and defeated runner up Tiger Woods to win his only tournament – the US Open.           

            We’re fully digital in this version of the pool, so please just fill in the link here with your email.
            
            Good luck everyone!
            ''')



st.markdown('''## Course Layout''')
course_table = {
    "Hole": [1, 2, 3, 4, 5, 6, 7, 8, 9, "Out", 10, 11, 12, 13, 14, 15, 16, 17, 18, "In", "Total"],
    "Name": ["Cut the Corner", "The Ridge", "Floyds Fork", "Short 'n Sweet", "Fade Away", "The Bear", "Players Pick", "Thor's Hammer", "The Rise", "", "Turns", "On the Edge", "Odin's Revenge", "The Island", "Two Tears", "On the Rocks", "Down the Stretch", "No Mercy", "Gahm Over", "", ""],
    "Yards": [484, 500, 208, 372, 463, 495, 597, 190, 415, 3724, 590, 211, 494, 351, 254, 435, 508, 472, 570, 3885, 7609],
    "Par": [4, 4, 3, 4, 4, 4, 5, 3, 4, 35, 5, 3, 4, 4, 3, 4, 4, 4, 5, 36, 71]
}

df_course_table = pd.DataFrame(course_table)

st.table(df_course_table)