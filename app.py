import streamlit as st

view = [100, 150, 30, 400]
st.write('# Title: Number of Students')
st.write('## raw')
view

st.write('## bar chart')
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview