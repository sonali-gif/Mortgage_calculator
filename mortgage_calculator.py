import streamlit as st

st.set_page_config(#configure before stremlit strt
    page_title="Mortgage Calculator",
    page_icon="🏡",
    layout="wide" #can also be centered
)

st.title("Mortgage Calculator")#large texe
st.write("Calculate your monthy mortgage payment.")#normal text

loan_amount =st.number_input(#number_input() create a box tht accept only number
    "Enter Loan Amount(₨)",
    min_value=10000,
    value=500000,#default value
    step=10000
)

interest_rate = st.number_input(
    "Annual Interest Rate (%)",
    min_value=0.0,
    max_value=20.0,
    value=8.5,
    step=0.1
)

loan_years = st.number_input(
    "Loan Duration (Years)",
    min_value=1,
    max_value=40,
    value=20,
    step=1
)

