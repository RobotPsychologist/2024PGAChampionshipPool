'''This is the player selections from the pool participants. 
'''

import streamlit as st
import pandas as pd
from utils.background_images import set_bg_hack

st.set_page_config(
    page_title="Team Selections",
    page_icon=":golf:",
    layout='wide',
)

st.write("# Team Selections :abacus:")
set_bg_hack("images/clubhouse.png")
LOGO_IMAGE_PATH = 'images/MastersTournamentLogo.png'
st.sidebar.image(LOGO_IMAGE_PATH, use_column_width=True)

group1, group2 = st.columns([0.5 , 0.5]) #group2 [0.2 , 0.2, 0.2, 0.2, 0.2]

grp1Table =  pd.DataFrame({
                    'Player': ['Scottie Scheffler', 'Rory McIlroy', 'Jon Rahm', 'Brooks Koepka', 'Jordan Spieth', 'Dustin Johnson', 'Viktor Hovland', 'Xander Schauffele', 'Patrick Cantlay', 'Cameron Smith'],
                    'Masters': ['🟩', '', '🟩', '', '🟩','🟩', '', '', '', ''],
                    'Country': ['🇺🇸', '🇬🇧', '🇪🇸', '🇺🇸', '🇺🇸', '🇺🇸', '🇳🇴', '🇺🇸', '🇺🇸', '🇦🇺'],
                    'Picked': [18,4,4,6,1,1,2,4,1,0]
                    })

grp2Table = pd.DataFrame({
                    'Player': ['Will Zalatoris', 'Hideki Matsuyama', 'Ludvig Aberg', 'Tony Finau', 'Bryson DeChambeau','Collin Morikawa','Matt Fitzpatrick', 'Joaquin Niemann', 'Wyndham Clark', 'Brain Harman' ],
                    'Masters': ['','🟩','','','','','','','','',],
                    'Country': ['🇺🇸','🇯🇵','🇸🇪','🇺🇸','🇺🇸','🇺🇸','🏴󠁧󠁢󠁥󠁮󠁧󠁿','🇨🇱','🇺🇸','🇺🇸'],
                    'Picked': [5,10,3,7,0,5,5,4,11,5]
                    })

grp3Table = pd.DataFrame({
                    'Player': ['Justin Thomas', 'Tommy Fleetwood', 'Max Homa', 'Cameron Young', 'Shane Lowry', 'Jason Day', 'Patrick Reed', 'Sahith Theegala', 'Sam Burns', 'Min Woo Lee', 'Sung-Jae Im', 'Tom Kim', 'Tyrrell Hatton', 'Rickie Fowler', 'Justin Rose', 'Phil Mickelson', 'Tiger Woods', 'Sergio Garcia', 'Adam Scott', 'Corey Conners'],
                    'Masters': ['','','','','','','🟩','','','','','','','','','🟩🟩🟩','🟩🟩🟩🟩🟩','🟩','🟩',''],
                    'Country': ['🇺🇸','🏴󠁧󠁢󠁥󠁮󠁧󠁿','🇺🇸','🇺🇸','🇮🇪','🇦🇺','🇺🇸','🇺🇸','🇺🇸','🇦🇺','🇰🇷','🇰🇷','🏴󠁧󠁢󠁥󠁮󠁧󠁿','🇺🇸','🏴󠁧󠁢󠁥󠁮󠁧󠁿','🇺🇸','🇺🇸','🇪🇸','🇦🇺','🇨🇦'],
                    'Picked': [6,5,6,5,9,1,0,4,1,1,1,1,0,3,1,2,1,0,0,5]
                    })

grp4Table = pd.DataFrame({
                    'Player': ['Si Woo Kim', 'Chris Kirk', 'Nick Taylor', 'J.T. Poston', 'Nick Dunlap', 'Keegan Bradley', 'Jake Knapp', 'Harris English', 'Cameron Davis', 'Thorbjorn Olesen', 'Mattieu Pavon', 'Sepp Straka', 'Eric Cole', 'Russell Henley', 'Gary Woodland', 'Emiliano Grillo', 'Nicolai Holgaard', 'Adam Hadwin', 'Luke List', 'Stephan Jaeger'],
                    'Masters': ['','','','','','','','','','','','','','','','','','','',''],
                    'Country': ['🇰🇷','🇺🇸','🇨🇦','🇺🇸','🇺🇸','🇺🇸','🇺🇸','🇺🇸','🇦🇺','🇩🇰','🇫🇷','🇦🇹','🇺🇸','🇺🇸','🇺🇸','🇦🇷','🇩🇰','🇨🇦','🇺🇸','🇩🇪'],
                    'Picked': [7,3,17,0,2,3,1,0,1,0,1,0,0,4,1,0,1,6,1,0]
                    })

grp5Table = pd.DataFrame({
                    'Player': ['Charl Schwartzel', 'Ryan Fox', 'Kurt Kitayama', 'Adrian Meronk', 'Bubba Watson', 'Danny Willett', 'Grayson Murray', 'Denny McCarthy', 'Ryo Hisatsune', 'Lucas Glover', 'Taylor Moore', 'Peter Malnati', 'Eric van Rooyen', 'Zach Johnson', 'Mike Weir', 'Jose Maria Olazabal', 'Fred Couples', 'Vijay Singh', 'Christo Lamprecht', 'Adam Schenk'],
                    'Masters': ['🟩','','','','🟩🟩','🟩','','','','','','','','🟩','🟩','🟩','🟩','🟩','',''],
                    'Country': ['🇿🇦','🇦🇺','🇺🇸','🇵🇱','🇺🇸','🏴󠁧󠁢󠁥󠁮󠁧󠁿','🇺🇸','🇺🇸','🇯🇵','🇺🇸','🇺🇸','🇺🇸','🇿🇦','🇺🇸','🇨🇦','🇪🇸','🇺🇸','🇫🇯','🇿🇦','🇺🇸'],
                    'Picked': [1,4,0,2,1,5,2,8,0,3,6,2,7,2,0,0,0,1,0,2]
                    })
with group1:
    st.write("### Group 1")
    st.dataframe(grp1Table[['Player', 'Masters', 'Country', 'Picked']], hide_index=True, use_container_width=True)
    st.write("### Group 3")
    st.dataframe(grp3Table, hide_index=True, use_container_width=True)
    st.write("### Group 5")
    st.dataframe(grp5Table, hide_index=True, use_container_width=True)

with group2:
    st.write("### Group 2")
    st.dataframe(grp2Table, hide_index=True, use_container_width=True)
    st.write("### Group 4")
    st.dataframe(grp4Table, hide_index=True, use_container_width=True)