import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import side_bar

def models_select(side_bar_input):
    st.subheader("III. Training")
    #Definition of X,y columns
    data = side_bar_input["data"]
    data = data.reset_index()
    X = data[side_bar_input['features']]
    y = data[side_bar_input['outputs']]
    y.replace((2,4), (1, 0), inplace=True)

    st.write(X)
    st.write(y)
    #Split the data
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=42)
    if side_bar_input['logistic_regression']==True and side_bar_input['svm']==False and side_bar_input['decision_tree']==False:

        st.write(X_train,y_train)
        #defining the model
        regr = LogisticRegression()
        cols = X_train.columns
        #Scaling the dataset
        X_train = pd.DataFrame(X_train, columns=[cols])
        X_test = pd.DataFrame(X_test, columns=[cols])
        X_train.reset_index()
        X_test.reset_index()
        #st.write(X_train)
        scaler = StandardScaler()
        X_train= scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        #Fit the model
        regr.fit(X_train,y_train)
        #The prediction output
        y_pred= regr.predict(X_test)
        st.write(y,y_pred)

    '''elif dict['logistic_regression']==False and dict['svm']==True and dict['decision_tree']==False:

        cols = X_train.columns
        scaler = StandardScaler()
        X_train= scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        X_train = pd.DataFrame(X_train, columns=[cols])
        X_test = pd.DataFrame(X_test, columns=[cols])   '''
