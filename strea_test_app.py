import pandas as pd
import numpy as np
import streamlit as st
import urllib
import altair as alt

@st.cache_data
def get_UN_data():
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    df=df.head(10)
    
    # return df.set_index("Region")
    st.dataframe(df)
    
get_UN_data()
# try:
# df = get_UN_data()
# countries = st.multiselect(
#     "Choose countries", list(df.index), ["China", "United States of America"]
# )
# if not countries:
#     st.error("Please select at least one country.")
# else:
#     data = df
#     data /= 1000000.0
#     st.write("### Gross Agricultural Production ($B)", data)

#     data = data.T.reset_index()
#     # data = pd.melt(data, id_vars=["index"]).rename(
#     #     columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
#     # )
#     chart = (
#         alt.Chart(data)
#         .mark_area(opacity=0.3)
#         .encode(
#             x="year:T",
#             y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
#             color="Region:N",
#         )
#     )
#     st.altair_chart(chart, use_container_width=True)
# except urllib.error as e:
#     st.error(
#         """
#         **This demo requires internet access.**
#         Connection error: %s
#     """
#         % e.reason
#     )