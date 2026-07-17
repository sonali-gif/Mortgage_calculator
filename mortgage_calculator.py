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

