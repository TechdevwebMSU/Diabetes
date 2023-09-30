import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


c1,c2,c3=st.columns([5,5,5])
st.title("On the top you can see graphs plotted for 3 columns from dataset")

uploaded_file = 'https://raw.githubusercontent.com/TechdevwebMSU/Diabetes/master/diabetes.csv'
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

  # Add some matplotlib code !
    fig, ax = plt.subplots()
    df.hist(
        bins=8,
        column="Insulin",
        grid=False,
        figsize=(10, 10),
        color="#86bf91",
        zorder=2,
        rwidth=0.9,
        ax=ax,
    )
    c1.write(fig)

    fig, ax = plt.subplots()
    df.hist(
        bins=8,
        column="Age",
        grid=False,
        figsize=(10, 10),
        color="#86bf91",
        zorder=2,
        rwidth=0.9,
        ax=ax,
    )
    c2.write(fig)

    fig, ax = plt.subplots()
    df.hist(
        bins=8,
        column="BMI",
        grid=False,
        figsize=(10, 10),
        color="#86bf91",
        zorder=2,
        rwidth=0.9,
        ax=ax,
    )
    c3.write(fig)

