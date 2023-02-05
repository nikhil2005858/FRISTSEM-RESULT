import streamlit as st
st.header(" WELCOME TO POLYTECHNIC  GOVERNMENT CHAMARAJANAGAR ")
st.image("govtpolychamraj01.jpg")
st.container()
st.write("[SECOND SEM RESULTS](https://nikhil2005858-result130-hello23-6mu7lh.streamlit.app/)")
st.write("FRIST SEM RESULTS")
button=st.button("GET RESULT")
data=open("html1.html","r")
x=data.read()
if button==True:
   st.markdown(x,unsafe_allow_html=True)