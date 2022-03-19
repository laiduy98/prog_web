import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import os


# Web App Title
st.title("Data Analyse Interface")
st.subheader("I. Dataset Visualization")
st.set_option('deprecation.showPyplotGlobalUse', False)

#EDA:
my_data = "D:Projects_intelli/prog_web/data/breast-cancer-wisconsin.data"

# To Improve speed and cache data
@st.cache(persist=True)
def explore_data(dataset):
	df = pd.read_csv(os.path.join(dataset),header=None)
	return df


data = explore_data(my_data)

with st.container():
	#Part1:
	st.markdown(f"<h3 style='text-align: center; color: #0556FD;'>Dataset Information</h3>", unsafe_allow_html=True)
	# Show Dataset:
	if st.checkbox("Preview Data",value=True):
		st.text("Head of dataset: ")
		st.write(data.head())
		st.text("Tail of dataset:")
		st.write(data.tail())

	# Dimensions:

	data_dim = st.radio("What dimension do you want to show ?", ('Rows', 'Columns'))

	if data_dim == 'Rows':
		st.write("The Length of Rows is:", len(data))
	if data_dim == 'Columns':
		st.write("The Length of Columns is :", data.shape[1])

	if st.checkbox("Show All Data"):
		st.dataframe(data)

	st.markdown("<hr/>", unsafe_allow_html=True)

	st.markdown(f"<h3 style='text-align: center; color: #0556FD;'>Unidimensional analysis of variables</h3>", unsafe_allow_html=True)

	#Type of variable:
	numeric_data = data.select_dtypes(include=[np.number])
	categorical_data = data.select_dtypes(exclude=[np.number])

	col_quan, col_qual = st.columns(2)

	with col_quan:
		st.markdown("- Quantitative Variables:")
		st.write("Count : ", numeric_data.shape[1])
		if st.button("Show Quantitative Features", disabled=False):
			st.write(numeric_data.columns)

	with col_qual:
		st.markdown("- Qualitative Variables:")
		st.write("Count :", categorical_data.shape[1])
		if st.button("Show Qualitative Features", disabled=False):
			st.write(categorical_data.columns)


	# percentage of pie chart:
	labels = ['Quantitative variables','Qualitative variables']
	values = [numeric_data.shape[1],categorical_data.shape[1]]
	fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3,pull=[0, 0, 0.2, 0])])
	#st.header('Percentage')
	st.plotly_chart(fig)

	#Summary
	if st.checkbox("Show Summary of Quantitative Variables"):
			st.write(data.describe())
			option = st.selectbox(
				"Which column do you want to visualise as a boxplot?",
				numeric_data.columns)
			fig = px.box(data,y=option)
			st.plotly_chart(fig,use_container_width=True)

	if st.checkbox("Show Summary of Qualitative Variables"):
		option = st.selectbox(
			"Which column would you like to visualise?",
			categorical_data.columns)

		fig = px.bar(categorical_data,x=option)
		st.plotly_chart(fig,use_container_width=True)

		st.markdown("<hr/>", unsafe_allow_html=True)

#Two-dimension
	st.markdown("<hr/>", unsafe_allow_html=True)
	st.markdown(f"<h3 style='text-align: center; color: #0556FD;'> Two-dimensional analysis of variables</h3>", unsafe_allow_html=True)
	col_x, col_y = st.columns(2)
	with col_x:
		option_x = st.multiselect(
			'Select X axis',
			(data.columns))
	with col_y:
		option_y = st.selectbox(
			'Select Y axis',
			(data.columns))

	#scatter plot:
	if st.checkbox("Show the sactter plot"):
		fig = px.scatter(data, x=option_x, y=option_y)
		st.plotly_chart(fig)

	st.markdown("<hr/>", unsafe_allow_html=True)
	st.markdown(f"<h3 style='text-align: center; color: #0556FD;'> Missing Data Detection</h3>", unsafe_allow_html=True)

	st.markdown(f"<p> The number of missing values in each column is : </p>", unsafe_allow_html=True)
	series_missing =(data == '?').astype(int).sum()
	st.write(series_missing.sum())
	if st.checkbox("Show the heatmap"):
		st.write(sns.heatmap(data=='?', cbar=False),weight=150,height=200)
		st.pyplot()



	st.write("This is outside the container")






