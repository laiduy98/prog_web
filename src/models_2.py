import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


def models_select(cleaned_data):
    st.subheader("III. Training")
    # Definition of X,y columns
    result_models = {}
    data = cleaned_data["data"]
    # data = data.reset_index()
    X = data[cleaned_data['features']]
    y = data[cleaned_data['outputs']]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    result_models['y_test'] = y_test
    result_models['y_train'] = y_train
    if cleaned_data['logistic_regression']:
        st.write('### In the case of using logistic regression')
        multi_class = st.radio('multi_class', ('ovr', 'multinomial'))
        # defining the model
        regression = LogisticRegression(multi_class=multi_class)
        # Fit the model
        regression.fit(X_train, y_train)
        # The prediction output
        y_pred_log = regression.predict(X_test)

        result_models['y_pred_logistic'] = y_pred_log

    if cleaned_data['svm']:
        st.write('### In the case of using SVM')
        kernel = st.radio('kernel', ('rbf', 'linear', 'poly', 'sigmoid', 'precomputed'))
        decision_function_shape = st.radio('decision_function_shape', ('ovr', 'ovo'))

        svc = SVC(kernel=kernel, decision_function_shape=decision_function_shape)
        # fit classifier to training set
        svc.fit(X_train, y_train)
        # make predictions on test set
        y_pred_svm = svc.predict(X_test)

        result_models['y_pred_svm'] = y_pred_svm

    if cleaned_data['decision_tree']:
        st.write('### In the case of using dicision tree')
        clf = DecisionTreeClassifier()
        clf.fit(X_train, y_train)
        y_pred_clf = clf.predict(X_test)
        result_models['y_pred_tree'] = y_pred_clf

    st.write(result_models)
    return result_models
