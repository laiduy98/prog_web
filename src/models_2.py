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
import plotly.express as px
from matplotlib import pyplot as plt




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


        st.markdown(f"<h3 style='text-align: center; color: #0556FD;'>Logistic Regression</h3>",
            unsafe_allow_html=True)

        st.markdown("###### - Prediction results from logistic regression")
        st.write(result_models)

        # --- Features Importances ---
        importance_lr = regression.coef_[0]
        st.markdown("###### - Importance Score for the logistic regression")
        for i,v in enumerate(importance_lr):
            st.write('Feature: %0d, Score: %.5f' % (i,v))
        #plot feature importance:
        if st.checkbox("Show the bar chart for the feature importance scores from logistic regression:"):
            fig = px.bar([x for x in range(len(importance_lr))], importance_lr)
            st.plotly_chart(fig, use_container_width=True)
        #-------------------------------#

        st.markdown("<hr/>", unsafe_allow_html=True)

    if cleaned_data['svm'] == True:
        svc=SVC() 
        # fit classifier to training set
        svc.fit(X_train,y_train)
        # make predictions on test set
        y_pred_svm=svc.predict(X_test)

        result_models['y_pred_svm']=y_pred_svm

        st.markdown(f"<h3 style='text-align: center; color: #0556FD;'>SVM</h3>",
                    unsafe_allow_html=True)
        st.markdown("###### - Prediction results from SVM")
        st.write(result_models)

        # --- Features Importances ---
         # impossible , Weights asigned to the features (coefficients in the primal problem).
         # This is only available in the case of linear kernel.
        #-------------------------------#
        st.markdown("<hr/>", unsafe_allow_html=True)



    if cleaned_data['decision_tree'] == True:
        clf = DecisionTreeClassifier()
        clf.fit(X_train, y_train)
        y_pred_clf = clf.predict(X_test)
        result_models['y_pred_tree'] = y_pred_clf

        st.markdown(f"<h3 style='text-align: center; color: #0556FD;'>Decision Tree</h3>",
                    unsafe_allow_html=True)
        st.markdown("###### - Prediction results from decision tree")
        st.write(result_models)

        # ---- Features Importances ----
        importance_dt = clf.tree_.compute_feature_importances(normalize=False)
        st.markdown("###### - Importance Score for the Decision Tree")
        for i,v in enumerate(importance_dt):
            st.write('Feature: %0d, Score: %.5f' % (i,v))
        if st.checkbox("Show the bar chart for the feature importance scores from decision tree:"):
            fig = px.bar([x for x in range(len(importance_dt))], importance_dt)
            st.plotly_chart(fig, use_container_width=True)
        #-------------------------------#
        st.markdown("<hr/>", unsafe_allow_html=True)
    

    return result_models
    


