import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import side_bar


def models_select(cleaned_data):
    st.subheader("III. Training")
    # Definition of X,y columns
    result_models = {}
    data = cleaned_data["data"].reset_index()
    #data = data.reset_index()
    X = data[cleaned_data['features']]
    y = data[cleaned_data['outputs']]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    print(type(X_train))
    if cleaned_data['logistic_regression'] == True:
        #st.write(X_train, y_train)
        # defining the model
        regression = LogisticRegression()
        # Fit the model
        st.write(X_train)
        st.write(y_train)
        regression.fit(X_train, y_train)
        # The prediction output
        y_pred_log = regression.predict(X_test)
        st.write(y, y_pred_log)
        #st.write('test')
        result_models['y'] = y
        result_models['y_pred_logistic'] = y_pred_log
        result_models['y_test_logistic'] = y_test
        st.write(result_models)
        return result_models


