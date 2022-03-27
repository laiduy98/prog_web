import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
import side_bar


def models_select(cleaned_data):
    st.subheader("III. Training")
    # Definition of X,y columns
    result_models = {}
    data = cleaned_data["data"]
    #data = data.reset_index()
    X = data[cleaned_data['features']]
    y = data[cleaned_data['outputs']]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    result_models['y_test']=y_test
    if cleaned_data['logistic_regression'] == True:
        # defining the model
        regression = LogisticRegression(multi_class='ovr')
        # Fit the model
        regression.fit(X_train, y_train)
        # The prediction output
        y_pred_log = regression.predict(X_test)
    
        result_models['y'] = y
        result_models['y_pred_logistic']=y_pred_log

    if cleaned_data['svm'] == True:
        svc=SVC() 
        # fit classifier to training set
        svc.fit(X_train,y_train)
        # make predictions on test set
        y_pred_svm=svc.predict(X_test)

        result_models['y_pred_svm']=y_pred_svm

    if cleaned_data['decision_tree'] == True:
        clf = DecisionTreeClassifier()
        clf.fit(X_train, y_train)
        y_pred_clf = clf.predict(X_test)
        result_models['y_pred_tree'] = y_pred_clf
    
    st.write(result_models)
    return result_models
    


