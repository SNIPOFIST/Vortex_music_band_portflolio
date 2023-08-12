import streamlit as st
from PIL import Image
import time 


st.set_page_config(
    page_title="VORTEX - Get High On Music",
    layout="wide",
    page_icon=":tornado:",
    
)
# CSS code snippet for background image properties
pg_bg =  """
<style>
[data-testid="stAppViewContainer"]{
background-image: url('https://c1.wallpaperflare.com/preview/373/217/83/guitarist-guitar-player-wallpaper-music-wallpapers.jpg');
background-size: cover;
}
</style>"""
# CSS code snippet for side bar image properties
side_bg = """
<style>
[data-testid="stSidebar"]{
  width: 200px;
  background-image: url('https://w0.peakpx.com/wallpaper/587/281/HD-wallpaper-stars-night-sky-amoled-black-dark-minimal-night-night-sky-sky-star-stars-steamroom.jpg');
}
</style>
"""
header = """
[data-testid="stHeader"]{
<p>GET HIGH ON MUSIC</p>
}
"""
st.markdown(pg_bg,unsafe_allow_html=True)
st.markdown(side_bg,unsafe_allow_html=True)

# Define HTML/CSS for center alignment
custom_style = """
    <style>
    .center-text {
        text-align: center;
        font-size: 80px;
        font-family: sans-serif:
    }
    </style>
"""

dummy_1 , dummy_2 ,dummy_3 = st.columns(3)
# header section for Logo 
with dummy_1:
    # dummy column to center the image 
    st.write("")

with dummy_2:
    vortex_logo = Image.open("vortex-logo.jpg")

    st.image(vortex_logo,width=380)
with dummy_3:
    # dummy column 3 to center the image 
    st.write("")
# Apply the custom style and display centered text
st.markdown(custom_style, unsafe_allow_html=True)
st.markdown('<h1 class="center-text">VORTEX</h1>', unsafe_allow_html=True)

# Use the custom CSS class to style text
name_style = """
    <style>
    .name_style{
        font-size: 24px;
        font-family: sans-serif:
    }
    </style>
    """
st.write("")
st.write("")
st.write("")
st.write("")
st.title("About the band!")

st.write("")
with st.container():
        markdown_text = """
        <p style="font-size: 24px;font-family:monospace">Vortex is a 6 piece rock n roll speculative band based in Bangalore, India 🇮🇳. 
            We as a team enjoys and loves to express the music and talent we have in us and spread it across, 
            we have won multiple battle of bands events across Bangalore and also played an opening act for band Mysore Xpress for 
            Tantra'23 which comprised of a 60 minute set.<br>
        <br>
         We as a team is diverse with a sole purpose of following our passions and to Rock 'N' Roll 
            for every opportunity we get. Be it Rock, Pop, Funky groovy music or any genre put forward to us we give it out in our own speculated style 
            such that we'll entertain you with some quality music and love.<br>
        <br>
        Every time we perform we look to bring down the roof and get you all hooked up to the 
            best quality of music with tons of fun. See you all<</p>
        """
        st.markdown(markdown_text,unsafe_allow_html = True) 

st.write("------------")
st.title("THE TEAM!")
st.write("")
the_team = Image.open("vortex-team.jpg")
st.image(the_team)
st.write("------------")
st.title("ON THE DRUMS!")
st.write("")
st.write("")
st.subheader("VISHNU NAIR")

drum_container , drum_picture = st.columns(2)
with drum_container:
    with st.container():
        st.write("")
        st.write("")
        markdown_text = """

        <p style="font-size: 22px;font-family:courier new">The heart and rhythm of our band, a drummer by passion and talent. He's been playing drums for 11 years now and he picks up beats instantaneously and that's going to be your first impressions about him.<br>
        <br>
        He prefers hard rock, jazz, pop and R&B as the genres of music he listens to. He is inspired by the work of artists like Matt McGuire, Casey Cooper, Aric Improta and Ed sheeran.<br>
        <br>
        To name a few, his favourite bands are Twenty one pilots, Metallica, Imagine dragons and our very own Kerala based Thaikkudam Bridge. Turning benches into drums and pens to drumsticks, he's got you hooked onto the best beats from our side.</p>
        """
        st.markdown(markdown_text,unsafe_allow_html = True)

with drum_picture:
    drummer = Image.open("vortex-vishnu.jpg")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.image(drummer,width=450,use_column_width = True)
st.write("------------")
st.title("ON THE VOCALS!")
st.write("")
st.write("")
st.subheader("SPANDAN DAS")

vocal_content , vocal_picture = st.columns(2)
with vocal_content:
    with st.container():
        st.write("")
        st.write("")
        markdown_text = """
        <p style="font-size: 22px;font-family:courier new">The voice of our band, A vocalist, pianist and guitarist who first picked up an instrument at the age of three. He has performed in various stage shows all around India and hopes to touch more hearts with his voice.<br>
        <br>
        He prefers pop, classic rock and Bollywood style of music. He idolizes Kishore Kumar, Arijit Singh and Chester Bennigton , quite a versatile combo, just like his way of singing. His favourite bands are Linkin Park, Maroon 5, Iron Maiden and Simple Plan.<br>
        <br>
        Could sing his heart out even when he has the soarest of throats and will definitely win your hearts, here's our newest vocalist.</p>
        """
        st.markdown(markdown_text,unsafe_allow_html = True)   

with vocal_picture:
    vocal = Image.open("vortex-spandan.jpg")
    st.write("")
    st.write("")
    st.write("")
    st.image(vocal,width=420,use_column_width=False)
st.write("------------")
st.title("BASSIST!")
st.write("")
st.write("")
st.subheader("SEHAJ TALWAR")

bassist_content , bassist_picture = st.columns(2)
with bassist_content:
    with st.container():
        st.write("")
        st.write("")
        markdown_text = """

        <p style="font-size: 22px;font-family:courier new">He's our bassist and he has an experience with the guitar for about 4 years now. He was very affectionate towards stringed instruments right from the start and that's when he mastered with fingerstyle guitar play.<br>
        <br>
        He enjoys and prefers some genres like Metal, Pop, Country music and some R&B. He is inspired by the works of some artists like Tommy Emmanuel, Chet Atkins and Led Zeppelin. Some of his favourite bands are Queen, Megadeth, The Beatles and System Of A Down.<br>
        <br>
        Even though he is new to bass and the band, all he needs is some time and he's got us all hooked on to the song.</p>
        """
        st.markdown(markdown_text,unsafe_allow_html = True)
 
with bassist_picture:
    bassist = Image.open("vortex-sehaj.jpg")
    st.write("")
    st.write("")
    st.write("")

    st.image(bassist,width=420,)

st.write("------------")
st.write("")
st.write("")
st.write("")

st.subheader('''For Enquiries''')
st.write("")
st.write("")

col1 , col2 = st.columns(2)
with col1:
    st.markdown("*Instagram* ➞ [Vortex](https://www.instagram.com/vortex__blr/?igshid=MzRlODBiNWFIZA==)")
    st.markdown("*Contact*  ➞ [+91 81974 74510](https://www.google.com)")
    st.markdown("*Mail* ➞ [vishnu.s.nair@gmail.com](mailto:vishnu.s.nair1818@gmail.com)")

with col2:
    st.markdown("**Visit our gallery** ➞ [Google-Drive](https://drive.google.com/drive/folders/1-8pi6t-MbtMpiThPmfTJie9jUriVGjuP)")
st.sidebar.header("Jump to")
st.sidebar.markdown("- [About the band](#about-the-band)")
st.sidebar.markdown("- [On the Drums!](#on-the-drums)")
st.sidebar.markdown("- [On The Vocals!](#on-the-vocals)")
st.sidebar.markdown("- [Bassist!](#bassist)")
st.sidebar.markdown("- [For Enquiries](#for-enquiries)")
st.write("")

st.write("------------")
st.caption("GET HIGH ON MUSIC ")
