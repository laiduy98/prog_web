import streamlit as st
import pandas as pd
import warnings

dict = {}

def user_input_features():
    warnings.filterwarnings("ignore")

    # 1st upload the file:

    file = st.sidebar.file_uploader("Upload a data file: ")
    empty = True

    try:
        # csv
        df = pd.read_csv(file, sep=",", header=None)
        #st.write(df)
        if df is not None:
            num_Column = df.shape[1]
            st.write("The number of columns is : ", num_Column)
            st.write("Please name each column on the left, or you can use the default name")
            column_name = []
            i = 1

            while i <= num_Column:
                name = st.sidebar.text_input(f"Enter the name of column {i}", f"default {i}")
                if name is not None:
                    column_name.append(name)
                    empty = False
                i = i + 1
            if empty == False:
                doneBT = st.sidebar.checkbox("Done!")

            st.markdown("<hr/>", unsafe_allow_html=True)
            st.sidebar.markdown(f"<h5 style='text-align: center; color: #0556FD;'>Your columns: </h5>",
                                unsafe_allow_html=True)
            st.sidebar.text(column_name)
            df = df.set_axis(column_name, axis=1)
            dict["data"] = df


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
                dict['logistic_regression'] = True
            else:
                dict['logistic_regression'] = False

            if SVM:
                dict['svm'] = True
            else:
                dict['svm'] = False

            if DT:
                dict['decision_tree'] = True
            else:
                dict['decision_tree'] = False

            # choose input
            st.sidebar.markdown(f"<h4 style='text-align: center; color: #0556FD;'>Select your feature(s)</h4>",
                                unsafe_allow_html=True)

            features = st.sidebar.multiselect("Select your Inputs", column_name)
            dict['features'] = features

            # choose output
            st.sidebar.markdown(f"<h4 style='text-align: center; color: #0556FD;'>select your Output</h4>",
                                unsafe_allow_html=True)

            outputs = st.sidebar.selectbox("Select your output", column_name)
            # st.sidebar.write(value)
            dict['outputs'] = outputs

            # qualitative variables
            st.sidebar.markdown(
                f"<h4 style='text-align: center; color: #0556FD;'>Select qualitative variables</h4>",
                unsafe_allow_html=True)

            qualitative_var = st.sidebar.multiselect("Select qualitative variables", column_name)
            dict["qualitative_variables"] = qualitative_var

            # quantitive vars
            st.sidebar.markdown(
                f"<h4 style='text-align: center; color: #0556FD;'>Select quantitative variables</h4>",
                unsafe_allow_html=True)
            quantitative_var = st.sidebar.multiselect("Select quantitative variables", column_name)
            dict["quantitative_variables"] = quantitative_var

            #if st.sidebar.button("show me the result!"):
            return dict

    except ValueError:
        st.write("no file was assigned")


