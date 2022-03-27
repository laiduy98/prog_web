import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, RocCurveDisplay
from sklearn.metrics import roc_auc_score
import streamlit as st


def test(data_file_name):
    st.write("Test")

    column_name = [
        'erythema', 'scaling', 'definite borders', 'itching', 'koebner phenomenon', 'polygonal papules', 'class'
    ]
    data = pd.read_csv(data_file_name, names=column_name, usecols=[0, 1, 2, 3, 4, 5, 34])
    # print(data)
    clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
    X = data.drop('class', axis=1)
    y = data['class']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    clf.fit(X_train, y_train)

    predictions = clf.predict(X_test)

    cm = confusion_matrix(y_test, predictions, labels=clf.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
    disp.plot()
    # plt.show()
    # print(clf.predict([[2, 1, 2, 3, 1, 3]]))

    st.pyplot(plt)

    # RocCurveDisplay.from_estimator(clf, X_test, y_test)
    #
    # st.pyplot(plt)


def evaluation_step(results):
    st.subheader("IV. Evaluation")



    cm = confusion_matrix(results['y_test'], results['y_pred_logistic'], labels=results['y'])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=results['y'])
    disp.plot()
    # plt.show()
    # print(clf.predict([[2, 1, 2, 3, 1, 3]]))

    st.pyplot(plt)


if __name__ == '__main__':
    data_file_path = '../data/dertamology/dermatology.data'
    # data_file_path = 'data/dertamology/dermatology.data'
    test(data_file_path)
