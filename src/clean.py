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

        data = data.replace('?', np.nan)
        # st.write(data['Age (linear)'].isnull())
        # num_col_contain_nan = len(data.columns[data.isna().any()].tolist())
        # print(num_col_contain_nan)
        # st.write(num_col_contain_nan)
        nan_resolve_problem = st.radio('Choose way to solve NaN', ('Remove Nan', 'Replace with mean of column'))
        # st.write(nan_resolve_problem)
        # st.write(type(nan_resolve_problem))

        if nan_resolve_problem == 'Remove Nan':
            st.write('Choose the number of blank features before the rows is removed')
            num_col_contain_nan = len(data.columns[data.isna().any()].tolist())
            missing_num = st.slider('Number of missing features before the row is removed', 0, num_col_contain_nan, 0)

            if missing_num > 0:
                data_new = data[data.isnull().sum(axis=1) < missing_num]
            elif missing_num == 0:
                data_new = data

        elif nan_resolve_problem == 'Replace with mean of column':
            data_new = data.fillna(data.mean())

        data_y = data_new[cleaned_input['outputs']]
        data_X = data_new.loc[:, data.columns != cleaned_input['outputs']]
        st.write(data_X)
        data_X_column = data_X.columns

        st.write('Do you want to normalize ?')
        normalize_status = st.checkbox('Normalize')
        if normalize_status:
            norm_type = st.radio('Choose the norm', ('l1', 'l2', 'max'))
            data_X = normalize(data_X, norm=norm_type)

        st.write('Do you want apply feature scaling (StandardScaler) ?')
        scaling_status = st.checkbox('Feature scaling')
        if scaling_status:
            scaler = StandardScaler()
            data_X = scaler.fit_transform(data_X)

        data_X = pd.DataFrame(data_X, columns=data_X_column)

        # print(data_y)
        # st.write(data_X)
        data_y.reset_index(inplace=True, drop=True)
        data_X.reset_index(inplace=True)

        data_X[cleaned_input['outputs']] = data_y
        # st.write(data_y)
        # st.write(data_X)
        cleaned_data = data_X
        # cleaned_data.dropna(inplace=True)
        cleaned_data[cleaned_input['outputs']].astype(int)
        st.write('### Data preview')
        st.write(cleaned_data)

        cleaned_input['data'] = cleaned_data
    return cleaned_input
