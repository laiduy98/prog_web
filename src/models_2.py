import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import side_bar
import plotly.express as px
from matplotlib import pyplot as plt
from yellowbrick.classifier import ROCAUC
from streamlit_yellowbrick import st_yellowbrick


def models_select(cleaned_data):
    st.subheader("III. Training")
    # Definition of X,y columns
    result_models = {}
    data = cleaned_data["data"]
    # data = data.reset_index()
    X = data[cleaned_data['features']]
    y = data[cleaned_data['outputs']]

    # Split the data
    test_size = st.number_input('Test size', min_value=0.1, max_value=1.0, value=0.3)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    result_models['y_test'] = y_test
    result_models['y_train'] = y_train
    result_models['X_test'] = X_test
    result_models['X_train'] = X_train
    if cleaned_data['logistic_regression']:
        st.write('### In the case of using logistic regression')
        multi_class = st.radio('multi_class', ('ovr', 'multinomial'))
        # defining the model
        regression = LogisticRegression(multi_class=multi_class)
        # Fit the model
        regression.fit(X_train, y_train)
        # The prediction output
        y_pred_log = regression.predict(X_test)
        y_pred_log_proba = regression.predict_proba(X_test)



        result_models['y_pred_logistic'] = y_pred_log
        result_models['y_pred_logistic_proba'] = y_pred_log_proba
        # result_models['visualizer_log'] = visualizer_log

        # --- Features Importances ---
        importance_lr = regression.coef_[0]
        st.markdown("###### - Importance Score for the logistic regression")
        for i, v in enumerate(importance_lr):
            st.write('Feature: %0d, Score: %.5f' % (i, v))
        # plot feature importance:
        if st.checkbox("Show the bar chart for the feature importance scores from logistic regression:"):
            fig = px.bar([x for x in range(len(importance_lr))], importance_lr)
            st.plotly_chart(fig, use_container_width=True)
        # -------------------------------#

        st.markdown("<hr/>", unsafe_allow_html=True)

        try:
            visualizer_log = ROCAUC(regression)
            visualizer_log.fit(X_train, y_train)
            visualizer_log.score(X_test, y_test)
            st_yellowbrick(visualizer_log)
        except:
            pass

    if cleaned_data['svm']:
        svc = SVC()
        st.write('### In the case of using SVM')
        kernel = st.radio('kernel', ('rbf', 'linear', 'poly', 'sigmoid', 'precomputed'))
        decision_function_shape = st.radio('decision_function_shape', ('ovr', 'ovo'))

        svc = SVC(kernel=kernel, decision_function_shape=decision_function_shape, probability=True)
        # fit classifier to training set
        svc.fit(X_train, y_train)
        # make predictions on test set
        y_pred_svm = svc.predict(X_test)
        y_pred_svm_proba = svc.predict_proba(X_test)



        # result_models['visualizer_svm'] = visualizer_svm

        result_models['y_pred_svm'] = y_pred_svm
        result_models['y_pred_svm_proba'] = y_pred_svm_proba

        try:
            visualizer_svm = ROCAUC(svc)
            visualizer_svm.fit(X_train, y_train)
            visualizer_svm.score(X_test, y_test)
            st_yellowbrick(visualizer_svm)
        except:
            pass

    if cleaned_data['decision_tree']:
        st.write('### In the case of using dicision tree')

        criterion = st.radio('Choose your criterion', ('gini', 'entropy'))

        clf = DecisionTreeClassifier(criterion=criterion)
        clf.fit(X_train, y_train)

        y_pred_clf = clf.predict(X_test)
        y_pred_clf_proba = clf.predict_proba(X_test)


        # result_models['visualizer_clf'] = visualizer_clf

        result_models['y_pred_tree'] = y_pred_clf
        result_models['y_pred_tree_proba'] = y_pred_clf_proba

        # ---- Features Importances ----
        importance_dt = clf.tree_.compute_feature_importances(normalize=False)
        st.markdown("###### - Importance Score for the Decision Tree")
        for i, v in enumerate(importance_dt):
            st.write('Feature: %0d, Score: %.5f' % (i, v))
        if st.checkbox("Show the bar chart for the feature importance scores from decision tree:"):
            fig = px.bar([x for x in range(len(importance_dt))], importance_dt)
            st.plotly_chart(fig, use_container_width=True)
        # -------------------------------#
        st.markdown("<hr/>", unsafe_allow_html=True)

        try:
            visualizer_clf = ROCAUC(clf)
            visualizer_clf.fit(X_train, y_train)
            visualizer_clf.score(X_test, y_test)
            st_yellowbrick(visualizer_clf)
        except:
            pass

    # st.write(result_models)
    return result_models
