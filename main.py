import streamlit as st


# Define CSS styles
def load_css():
   st.markdown("""
   <style>
   body {
       color: #555;
       background-color: #f4f4f8;
       font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
   }
   .stMarkdown, .stButton, .stTextInput {
       border-radius: 8px;
       box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
   }
   .sidebar .sidebar-content {
       background-color: #f0f0f5;
       padding: 10px;
   }
   h1 {
       text-align: center;
       font-size: 2em;
       text-shadow: 0 0 10px rgba(0,0,0,0.2);
       color: #4ABDAC; /* relaxing teal color */
   }
   h2, h3 {
       color: #3e4b5b;
       text-align: center;
   }
   .css-1aumxhk {
       background-color: #f0f0f5;
       border-color: #666;
   }
   .stButton>button {
       color: #fff;
       background-color: #4a69bd;
       border-color: #4a69bd;
       font-size: 1em;
       padding: 8px 24px;
       width: 100%;
       margin: 5px 0;
   }
   .stMarkdown {
       text-align: center;
   }
   </style>
   """, unsafe_allow_html=True)


load_css()


# Main page content
st.markdown("""
   <h1>We are here to Help Lives, One Vet at a Time!</h1>
""", unsafe_allow_html=True)
st.sidebar.markdown("## Welcome to Our Main Page Where Help can be Found")


message = """Welcome to the main page! 🎉\nWelcome to our online haven for veterans, designed to support and enhance your day-to-day life with easy-to-use digital tools. Our platform includes features allowing you to get instant answers to your questions. For those who prefer listening over reading, our Text-to-Speech function converts written content into clear, spoken audio. Additionally, our Audio Transcription service ensures that spoken information is not lost, providing you with written records of conversations and audio materials. Explore our features today and experience how they can assist you in navigating daily challenges with ease and confidence.!"""
st.write(message)


# Navigation links
st.markdown("### Navigation Links")
st.markdown("Click below to navigate to different features of our platform:")
st.page_link("pages/Guidance Page.py", label="Receive Guidance and Support")
st.page_link("pages/Translations.py", label="Translations")
st.page_link("pages/Transcription.py", label="Transcription")
