import streamlit as st
import time

from main import counter


st.header(':zap: Monty Hall Game Simulaton')

num_games = st.number_input('num of game to simulate', min_value=1, value=100)

col1, col2 = st.columns(2)
col1.subheader('Win Percentage with Switching')
col2.subheader('Win Perectage without Switching')

chart1 = col1.line_chart(height=400)
chart2 = col2.line_chart(height=400)

wins_switching = 0
wins_no_switching = 0
for i in range(num_games):
    num_wins_switching, num_wins_no_switching = counter(1)

    wins_switching += num_wins_switching
    wins_no_switching += num_wins_no_switching

    chart1.add_rows([wins_switching / (i + 1)])
    chart2.add_rows([wins_no_switching / (i + 1)])

    time.sleep(0.01)
