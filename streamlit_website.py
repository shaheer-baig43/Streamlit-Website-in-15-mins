import random
import streamlit as st
import pandas as pd
import time



st.title('Streamlit Website in 15 Minutes!')

st.write('### This is a countdown timer ###')


seconds_input = st.text_input("Enter the countdown time in seconds:", key="countdown_input")


if st.button("Start Timer"):
    if seconds_input.isdigit():  
        seconds = int(seconds_input)
        
        countdown_placeholder = st.empty()  

        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = f'{mins:02}:{secs:02}'
            countdown_placeholder.markdown(f"### {timer}")  
            time.sleep(1)
            seconds -= 1

        countdown_placeholder.markdown("##  Time's up!")
    else:
        st.error("Please enter a valid number!")


st.write('Made by Shaheer Baig')




