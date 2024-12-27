"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore

follower_page = st.Page('followers_page.py', title='Follower Metrics')
reach_page = st.Page('reach_page.py', title='Reach Metrics')
prediction_page = st.Page('predictive_page.py', title='Predictive Analytics')
pg = st.navigation([reach_page, follower_page, prediction_page])
pg.run()