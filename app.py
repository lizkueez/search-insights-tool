import streamlit as st

st.set_page_config(
    page_title="Search Insights",
    layout="wide"
)

st.title("Search Insights Generator")

st.subheader("Month")
month = st.text_input("Month")

st.subheader("Top Performing Verticals")

for i in range(5):
    st.text_input(f"Vertical {i+1}")

st.button("Generate Report")
