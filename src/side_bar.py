import streamlit as st
import pandas as pd
import warnings
from io import StringIO

input_dict = {}


def user_input_features():
    warnings.filterwarnings("ignore")

    # 1st upload the file:

    data_file = st.sidebar.file_uploader("Upload a data file: ")
    empty = True

    try:
        # csv
        data_df = pd.read_csv(data_file, sep=",", header=None)
        # st.write(df)
        if data_df is not None:

            column_input_type = st.sidebar.radio('Choose input column name by file or type directly:',
                                                 ('By file', 'By input in the text field'))

            if column_input_type == 'By file':
                column_file = st.sidebar.file_uploader("Upload a column file: ")
                # print('-----====' +column_file)

                if column_file is not None:
                    column_file = StringIO(column_file.getvalue().decode("utf-8"))
                    column_file = column_file.read()
                    column_name = column_file.split(',')
                    empty = False
                else:
                    column_name = []
                    for i in range(data_df.shape[1]):
                        column_name.append(f'default {str(i)}')
                    empty = False
                    st.sidebar.write("No file was assigned")

            elif column_input_type == 'By input in the text field':
                num_column = data_df.shape[1]
                st.write("The number of columns is : ", num_column)
                st.write("Please name each column on the left, or you can use the default name")
                column_name = []
                i = 1

                while i <= num_column:
                    name = st.sidebar.text_input(f"Enter the name of column {i}", f"default {i}")
                    if name is not None:
                        column_name.append(name)
                        empty = False
                    i = i + 1

            if not empty:
                doneBT = st.sidebar.checkbox("Done!")

            st.markdown("<hr/>", unsafe_allow_html=True)
            st.sidebar.markdown(f"<h5 style='text-align: center; color: #0556FD;'>Your columns: </h5>",
                                unsafe_allow_html=True)
            st.sidebar.text(column_name)
            data_df = data_df.set_axis(column_name, axis=1)
            input_dict["data"] = data_df

        if doneBT:
            """
            try:
                st.write(df)
            except:
                if empty == False:
                    st.error("Error: you didn't name your columns!")
                else:
                    st.error("Error: You gave the same name for two columns!")
            """
            st.sidebar.markdown(f"<h4 style='text-align: center; color: #0556FD;'>Select the model(s)</h4>",
                                unsafe_allow_html=True)
            LR = st.sidebar.checkbox("Logistic regression")
            SVM = st.sidebar.checkbox("SVM")
            DT = st.sidebar.checkbox("Decision Tree")

            if LR:
                input_dict['logistic_regression'] = True
            else:
                input_dict['logistic_regression'] = False

            if SVM:
                input_dict['svm'] = True
            else:
                input_dict['svm'] = False

            if DT:
                input_dict['decision_tree'] = True
            else:
                input_dict['decision_tree'] = False

            # choose input
            st.sidebar.markdown(f"<h4 style='text-align: center; color: #0556FD;'>Select your feature(s)</h4>",
                                unsafe_allow_html=True)

            features = st.sidebar.multiselect("Select your Inputs", column_name)
            input_dict['features'] = features

            # choose output
            st.sidebar.markdown(f"<h4 style='text-align: center; color: #0556FD;'>Select your output</h4>",
                                unsafe_allow_html=True)

            outputs = st.sidebar.selectbox("Select your output", column_name)
            # st.sidebar.write(value)
            # print(type(outputs))
            input_dict['outputs'] = outputs

            # qualitative variables
            st.sidebar.markdown(
                f"<h4 style='text-align: center; color: #0556FD;'>Select qualitative variables</h4>",
                unsafe_allow_html=True)

            qualitative_var = st.sidebar.multiselect("Select qualitative variables", column_name)
            input_dict["qualitative_variables"] = qualitative_var

            # quantitive vars
            st.sidebar.markdown(
                f"<h4 style='text-align: center; color: #0556FD;'>Select quantitative variables</h4>",
                unsafe_allow_html=True)
            quantitative_var = st.sidebar.multiselect("Select quantitative variables", column_name)
            input_dict["quantitative_variables"] = quantitative_var

            # if st.sidebar.button("show me the result!"):
            return input_dict

    except ValueError:
        st.write("no file was assigned")
