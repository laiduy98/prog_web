from sklearn import preprocessing
import streamlit as st
import numpy as np
import pandas as pd

from side_bar import user_input_features
from data_visualization import data_visualization
from clean import data_clean
from models import models_select

# st.image('')

st.write('''
# Programmation web project
##### This is a web application for visualising existing datasets, 
exploratory data analysis and training of different models.
''')

side_bar_input = user_input_features()

#st.write(side_bar_input)
if side_bar_input is not None:
    data_visualization(side_bar_input)

cleaned_data = data_clean(side_bar_input)

result = models_select(cleaned_data)



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