import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import matplotlib.pyplot as plt
import altair as alt

# Load data
data3 = pd.read_csv('Data/location_metrics.csv')
data4 = pd.read_csv('Data/industry_metrics.csv')
dataPrediction = pd.read_csv('Data/followers_november.csv')


def preprocess(data3, data4, dataPrediction):
    dataPrediction['Date'] = pd.to_datetime(dataPrediction['Date'])
    dataPrediction = dataPrediction.set_index('Date')
    dataPrediction = dataPrediction[['Total followers']]

    type_map_3 = {
        'Location': str,
        'Total followers': int
    }

    for column, dtype in type_map_3.items():
        data3[column] = data3[column].astype(str).astype(dtype)

    data3['Location'] = data3['Location'].replace({
        'Karachi Division, Pakistan': 'Karachi, Pakistan',
        'Karāchi, Pakistan': 'Karachi, Pakistan',
        'Lahore District, Pakistan': 'Lahore, Pakistan'
    })

    data3 = data3.groupby('Location', as_index=False).sum()
    data3 = data3.sort_values(by='Total followers', ascending=False)

    type_map_4 = {
        'Industry': str,
        'Total followers': int
    }

    for column, dtype in type_map_4.items():
        data4[column] = data4[column].astype(str).astype(dtype)

    return data3, data4, dataPrediction


def plot_total_followers(dataPrediction):
    st.title('Total follower gain (1 year span)')
    st.line_chart(dataPrediction, color=["#FF0000"])


def plot_followers_locations(data3):
    st.title('Followers by Location')
    
    # Streamlit Altair Chart without specifying explicit colors
    bars = alt.Chart(data3.head(7)).mark_bar().encode(
        x=alt.X('Total followers:Q', title='Total Followers', scale=alt.Scale(domain=(0, max(data3['Total followers'][:7]) + 1000))),
        y=alt.Y('Location:N', sort='-x', title='Location'),
        color=alt.Color('Location:N', legend=None)  # Let Altair handle colors based on Location
    )
    
    # Add text labels to bars
    text = bars.mark_text(
        align='left',
        baseline='middle',
        dx=5  # Move text slightly to the right
    ).encode(
        text='Total followers:Q'
    )

    # Combine bar chart and text
    chart = (bars + text).properties(
        width=600,
        height=300,
        title="Top Locations by Total Followers"
    )

    # Display in Streamlit
    st.altair_chart(chart, use_container_width=True)

    fig, ax = plt.subplots()
    ax.pie(x=data3['Total followers'][:7], labels=(data3['Location'][:7]), autopct='%1.1f%%')
    st.pyplot(fig)


def plot_followers_industry(data4):
    st.title('Followers by Industry')

    bars = alt.Chart(data4.head(7)).mark_bar(color='red').encode(
        x=alt.X('Total followers:Q', title='Total Followers', scale=alt.Scale(domain=(0, max(data4['Total followers'][:7]) + 1000))),
        y=alt.Y('Industry:N', sort='-x', title='Industry')
    )

    # Add text labels to bars
    text = bars.mark_text(
        align='left',
        baseline='middle',
        dx=5  # Move text slightly to the right
    ).encode(
        text='Total followers:Q'
    )

    # Combine bar chart and text
    chart = (bars + text).properties(
        width=600,
        height=300,
        title="Top Industries by Total Followers"
    )

    # Display in Streamlit
    st.altair_chart(chart, use_container_width=True)

    fig1, ax = plt.subplots()
    ax.pie(x=data4['Total followers'][:7], labels=(data4['Industry'][:7]), autopct='%1.1f%%')
    st.pyplot(fig1)


# Process data and call plotting functions
data3, data4, dataPrediction = preprocess(data3, data4, dataPrediction)
plot_total_followers(dataPrediction)
plot_followers_locations(data3)
plot_followers_industry(data4)
