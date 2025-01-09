import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore

follower_page = st.Page('followers_page.py', title='Follower Metrics')
reach_page = st.Page('reach_page.py', title='Reach Metrics')

pg = st.navigation([reach_page, follower_page])
pg.run()