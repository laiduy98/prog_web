from pathlib import Path
import streamlit as st

from side_bar import user_input_features
from data_visualization import data_visualization
from clean import data_clean
from models_2 import models_select
from evaluation import evaluation_step
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def main():
    image_path = Path(dir_path)
    # print(str(image_path.parent.absolute()))
    # print(str(image_path.parent.absolute()) + '/report/assets/images/uparis.png')
    st.image(str(image_path.parent.absolute()) + '/report/assets/images/uparis.png')

    st.write('''
    # Programmation web project
    ##### This is a web application for visualising existing datasets, exploratory data analysis and training of different models.
    ''')

    side_bar_input = user_input_features()

    if side_bar_input is not None:
        data_visualization(side_bar_input)

        cleaned_data = data_clean(side_bar_input)


        result = models_select(cleaned_data)

        evaluation_step(result)


if __name__ == '__main__':
    main()
