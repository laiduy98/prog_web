from sklearn import preprocessing
import streamlit as st
import numpy as np
import pandas as pd

from side_bar import user_input_features
from data_visulization import ziu_pretty
from clean import data_clean

# st.image('')

st.write('''
# Programmation web project
## Project
''')

side_bar_input = user_input_features()

st.write(side_bar_input)

zilu_output = ziu_pretty(side_bar_input)

# duy_output = duy_fuction(zilu_output)
#
# masha_out

# if side_bar_input['data_type'] == 'data':
#      processed_data = data_clean(side_bar_input=side_bar_input)
# else:
#      processed_data = data_clean(side_bar_input=side_bar_input)

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)