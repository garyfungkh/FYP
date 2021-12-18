import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np

DATE_COLUMN = 'date'
@st.cache
def load_data(File):
    data1 = pd.read_csv(File)
    lowercase = lambda x: str(x).lower()
    data1.rename(lowercase, axis='columns', inplace=True)
    data1[DATE_COLUMN] = pd.to_datetime(data1[DATE_COLUMN])
    return data1

df = load_data('C:\\Users\\Gary Fung\\Desktop\\Dividend_00303.csv')

with st.form("my_form"):
    st.write("Display Option")
    report_type = st.radio('Which Report?', ('All', 'Middle', 'Final'))
    checkbox_npg = st.checkbox("Net Profit Growth",('Y'))
    checkbox_eps = st.checkbox("Earnings Per Share", ('Y'))
    checkbox_epsg = st.checkbox("EPS Growth", ('Y'))
    checkbox_pe = st.checkbox("PE", ('Y'))
    checkbox_y = st.checkbox('Yield',('Y'))
    checkbox_dp = st.checkbox('Dividend Payout',('Y'))

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Success")

if report_type =='Final':
    new_df_1 = df[df["report"]=='FINAL']['dividend']
    new_df_2 = df[df["report"]=='FINAL']['year']
    df1 = df[df["report"]=='FINAL'][['year','dividend']]
    df2 = df1.set_index('year')
    fig, ax = plt.subplots(figsize=(8, 8))
    sn.barplot(x="year", y="dividend", data=df1)
    st.subheader("Dividend of Vtech for Middle Financial Report")
    st.write(df2)
    st.write("Average Dividend")
    st.write(df1["dividend"].mean())
    st.pyplot(fig)

elif report_type=='Middle':
    new_df_1 = df[df["report"]=='MID']['dividend']
    new_df_2 = df[df["report"]=='MID']['year']
    df1 = df[df["report"]=='MID'][['year','dividend']]
    df2 = df1.set_index('year')
    fig, ax = plt.subplots(figsize=(8, 8))
    sn.barplot(x="year", y="dividend", data=df1)
    st.subheader("Dividend of Vtech for Middle Financial Report")
    st.write(df2)
    st.write("Average Dividend")
    st.write(df1["dividend"].mean())
    st.pyplot(fig)

else:
    new_df_1 = df['dividend']
    new_df_2 = df['year']
    df1 = df[['year', 'dividend']]
    df1 = df1.set_index('year')
    fig, ax = plt.subplots(figsize=(8, 8))
    sn.barplot(x="year", y="dividend", hue="report", data=df)
    st.subheader("Dividend of Vtech for All Financial Report")
    st.write(df1)
    st.pyplot(fig)


