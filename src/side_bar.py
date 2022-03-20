import streamlit as st
import pandas as pd

def user_input_features():

    uploaded_file = st.sidebar.file_uploader("Choose a file")

    test = st.sidebar.slider('Test index', 4.3, 7.9, 5.4)

    column_dummy = ['ddd', 'ggg', 'kkk']

    data = {'data_type': 'data', 'data': uploaded_file, 'column_name': column_dummy}
    # features = pd.DataFrame(data, index=[0])
    return data