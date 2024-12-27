import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore
import datetime

data1 = pd.read_csv('Data/training_data_reach.csv')

data1.columns = data1.iloc[0] 
data1 = data1.drop(0)
data1['Date'] = pd.to_datetime(data1['Date'])
data1 = data1.set_index('Date')


data1['Impressions (organic)'] = data1['Impressions (organic)'].astype(str).astype(int)
data1['Impressions (sponsored)'] = data1['Impressions (sponsored)'].astype(str).astype(int)
data1['Impressions (total)'] = data1['Impressions (total)'].astype(str).astype(int)
data1['Engagement rate (organic)'] = data1['Engagement rate (organic)'].astype(str).astype(float)
data1['Engagement rate (sponsored)'] = data1['Engagement rate (sponsored)'].astype(str).astype(float)
data1['Engagement rate (total)'] = data1['Engagement rate (total)'].astype(str).astype(float)
data1['Clicks (organic)'] = data1['Clicks (organic)'].astype(str).astype(float)
data1['Clicks (sponsored)'] = data1['Clicks (sponsored)'].astype(str).astype(float)
data1['Clicks (total)'] = data1['Clicks (total)'].astype(str).astype(float)

data6 = pd.read_csv('Data/visiter_metrics.csv')
data6['Date'] = pd.to_datetime(data6['Date'])
data6 = data6.set_index('Date')

type_map ={
    'Overview page views (total)':int,
    'Overview unique visitors (total)':int,
    'Life page views (total)': int,
    'Jobs page views (total)': int,
    'Total page views (total)':int,
}

for column, dtype in type_map.items():
    data6[column] = data6[column].astype(str).astype(dtype)

st.text('This dashboard is not automated in its data collection for now')
st.text('Once it is, it will update every 2 days when available on LinkedIn')
st.title('Impressions\n')
st.line_chart(data1, x=None,y=['Impressions (organic)','Impressions (sponsored)'],x_label='Date',y_label='Number of Impressions',height=None,color=["#FF0000", "#0000FF"])
st.line_chart(data1, x=None,y=['Impressions (total)'],x_label='Date',y_label='Number of Impressions',height=None,color=["#FF0000"])

st.title('Engagement\n')
st.line_chart(data1,x=None,y=['Engagement rate (organic)','Engagement rate (sponsored)'],x_label='Date',y_label='Engagement Rate',color=["#FF0000", "#0000FF"])
st.line_chart(data1,x=None,y=['Engagement rate (total)'],x_label='Date',y_label='Engagement Rate',color=["#0000FF"])

st.title('Clicks')
st.line_chart(data1,x=None,y=['Clicks (organic)','Clicks (sponsored)'],x_label='Date',y_label='Click Rate',color=["#FF0000", "#0000FF"])
st.line_chart(data1,x=None,y=['Clicks (total)'],x_label='Date',y_label='Click Rate',color=["#0000FF"])

st.title('Views')
st.line_chart(data6, x=None,y=['Total page views (total)'],x_label='Date',y_label='Views',color=['#0000FF'])