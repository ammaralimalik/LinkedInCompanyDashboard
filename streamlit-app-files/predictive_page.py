import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import matplotlib.pyplot as plt
import altair as alt
from datetime import timedelta
import datetime
from statsmodels.tsa.exponential_smoothing.ets import ETSModel
from forecasting_model import ForecastingModel
    
def plot_historical_data(start, end):

    end_date = dataPrediction.index[-1]
    filtered_data = dataPrediction.loc[start:end]
    model = ForecastingModel(
            error="add",                
            trend="add",                
            seasonal="mul",             
            damped_trend=True,          
            seasonal_periods=12,       
            initialization_method='estimated'
        )

    model = model.fit(dataPrediction['Total followers'])
    

    if end < end_date.date():
        st.line_chart(filtered_data, color=["#FF0000"])
    elif start < end_date.date() and end > end_date.date():
        days = (end - end_date.date()).days
        steps = model.forecast(steps=days).tolist()
        forecast_dates = pd.date_range(start=end_date + timedelta(days=1), periods=days, freq='D')

      
        historical_df = pd.DataFrame({'date': filtered_data.index, 'value': filtered_data['Total followers'], 'type': 'Historical'})
        forecast_df = pd.DataFrame({'date': forecast_dates, 'value': steps, 'type': 'Forecast'})
        combined_df = pd.concat([historical_df, forecast_df])

        line_chart = alt.Chart(combined_df).mark_line().encode(
            x='date:T',
            y='value:Q',
            color=alt.Color('type:N', scale=alt.Scale(domain=['Historical', 'Forecast'], range=['red', 'blue']))).properties(title="Historical and Forecasted Data")

        st.altair_chart(line_chart, use_container_width=True)

    else:
       days = end - start
       steps = model.forecast(steps=days.days)
       st.line_chart(steps, color=["#0000FF"])



st.title('Follower Forecasting')
start = st.date_input('Please enter start date for forcasting: ', datetime.date(2024,1,1))
end = st.date_input('Please enter end date for forcasting: ', datetime.datetime.now().date())
st.text('Model is still under work. Not as powerful as it needs to be.')
st.text('Only sees the average returns for now.')
st.text('Adding ability to predict spikes and more accurate results')

dataPrediction = pd.read_csv('Data/training_data_followers.csv')
dataPrediction['Date'] = pd.to_datetime(dataPrediction['Date'])
dataPrediction = dataPrediction.set_index('Date')
dataPrediction = dataPrediction[['Total followers']]
plot_historical_data(start,end)





