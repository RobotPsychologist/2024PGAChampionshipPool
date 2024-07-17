'''This is the entrypoint file for the pool dashboard. 
'''

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Home",
    page_icon=":golf:",
    layout='wide',
)

TOURNAMENT_NAME_LOOKUP = 'the_open'
TOURNAMENT_NAME_LABEL = 'THE 152ND OPEN AT ROYAL TROON'
YEAR_LABEL = '2024'
LOGO_IMAGE_PATH = f'images/{TOURNAMENT_NAME_LOOKUP}/TournamentLogo.png'

st.write(f"# {TOURNAMENT_NAME_LABEL} ")
st.write(f"## {YEAR_LABEL} Pool :golf: ")



st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)

st.markdown('''
        Royal Troon’s Old Course was founded in 1878, expanded to 18 holes 10 years later and re-designed by five-time Champion Golfer James Braid ahead of its first Open in 1923. It is now gearing up to host The Open for a tenth time.
            ''')



st.image('images/the_open/the_open_at_royal_troon.png', use_column_width=True)  # Image from the royal troon website