import matplotlib.pyplot as plt
import streamlit as st

from sklearn.metrics import confusion_matrix, \
    ConfusionMatrixDisplay, \
    RocCurveDisplay, \
    precision_score, recall_score, f1_score, roc_auc_score


def evaluation_step(results):
    st.subheader("IV. Evaluation")
    # st.write(results['y_pred_logistic'])
    # st.write(results['y_test'])
    average_meth = st.radio('Average method for the score',
                            (None, 'micro', 'macro', 'samples', 'weighted', 'binary'))

    if 'y_pred_logistic' in results:
        st.write('### In the case of using logistic regression')

        col1, col2, col3 = st.columns(3)

        with col1:
            logistic_precision = precision_score(results['y_test'], results['y_pred_logistic'], average=average_meth)
            st.write('Precision score')
            st.write(logistic_precision)

        with col2:
            logistic_recall = recall_score(results['y_test'], results['y_pred_logistic'], average=average_meth)
            st.write('Recall score')
            st.write(logistic_recall)

        with col3:
            logistic_f1 = recall_score(results['y_test'], results['y_pred_logistic'], average=average_meth)
            st.write('F1 score')
            st.write(logistic_f1)

        st.write('-----')
    if 'y_pred_svm' in results:
        st.write('### In the case of using SVM')

        col1, col2, col3 = st.columns(3)

        with col1:
            svm_precision = precision_score(results['y_test'], results['y_pred_svm'], average=average_meth)
            st.write('Precision score')
            st.write(svm_precision)

        with col2:
            svm_recall = recall_score(results['y_test'], results['y_pred_svm'], average=average_meth)
            st.write('Recall score')
            st.write(svm_recall)

        with col3:
            svm_f1 = f1_score(results['y_test'], results['y_pred_svm'], average=average_meth)
            st.write('F1 score')
            st.write(svm_f1)

        st.write('-----')
    if 'y_pred_tree' in results:
        st.write('### In the case of using dicision tree')

        col1, col2, col3 = st.columns(3)

        with col1:
            tree_precision = precision_score(results['y_test'], results['y_pred_tree'], average=average_meth)
            st.write('Precision score')
            st.write(tree_precision)

        with col2:
            tree_recall = recall_score(results['y_test'], results['y_pred_tree'], average=average_meth)
            st.write('Recall score')
            st.write(tree_recall)

        with col3:
            tree_f1 = recall_score(results['y_test'], results['y_pred_tree'], average=average_meth)
            st.write('F1 score')
            st.write(tree_f1)

        st.write('-----')

    st.write('Confusion matrix')
    col1, col2, col3 = st.columns(3)
    with col1:
        if 'y_pred_logistic' in results:
            st.write('### In the case of using logistic regression')
            cm = confusion_matrix(results['y_test'], results['y_pred_logistic'])
            disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=None)
            disp.plot()
            st.pyplot(plt)

    with col2:
        if 'y_pred_svm' in results:
            st.write('### In the case of using SVM')
            cm = confusion_matrix(results['y_test'], results['y_pred_svm'])
            disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=None)
            disp.plot()
            st.pyplot(plt)

    with col3:
        if 'y_pred_tree' in results:
            st.write('### In the case of using dicision tree')
            cm = confusion_matrix(results['y_test'], results['y_pred_tree'])
            disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=None)
            disp.plot()
            st.pyplot(plt)


if __name__ == '__main__':
    data_file_path = '../data/dertamology/dermatology.data'
    # data_file_path = 'data/dertamology/dermatology.data'
