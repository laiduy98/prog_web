import numpy as np
import streamlit as st
import pandas as pd
from sklearn.preprocessing import normalize
from sklearn.preprocessing import StandardScaler


def data_clean(side_bar_input):
    cleaned_input = side_bar_input

    if cleaned_input['data'] is not None:
        data = cleaned_input['data']
        st.subheader("II. Dataset preprocessing")
        # st.dataframe(data)

        st.write('Choose the number of blank features before the rows is removed')
        data = data.replace('?', np.nan)
        num_col_contain_nan = len(data.columns[data.isna().any()].tolist())
        print(num_col_contain_nan)
        # st.write(num_col_contain_nan)

        missing_num = st.slider('Number of missing features before the row is removed', 0, num_col_contain_nan, 0)

        if missing_num > 0:
            data = data[data.isnull().sum(axis=1) < missing_num]

        data_y = data[cleaned_input['outputs']]
        data_X = data.loc[:, data.columns != cleaned_input['outputs']]
        data_X_column = data_X.columns

        st.write('Do you want to normalize ?')
        normalize_status = st.checkbox('Normalize')
        if normalize_status:
            norm_type = st.radio('Choose the norm', ('l1', 'l2', 'max'))
            data_X = normalize(data_X, norm=norm_type)

        st.write('Do you want apply feature scaling ?')
        scaling_status = st.checkbox('Feature scaling')
        if scaling_status:
            scaler = StandardScaler()
            data_X = scaler.fit_transform(data_X)

        data_X = pd.DataFrame(data_X, columns=data_X_column)


        # print(data_y)

        data_X[cleaned_input['outputs']] = data_y

        cleaned_data = data_X
        st.write(cleaned_data)

        cleaned_input['data'] = cleaned_data
    return cleaned_input
