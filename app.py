import streamlit as st

st.set_page_config(
    page_title="Search Insights",
    layout="wide"
)

st.title("🔍 Search Insights Generator")

month = st.text_input("Month")

st.divider()

st.header("Top Performing Verticals")

verticals = []
for i in range(5):
    verticals.append(
        st.text_input(
            f"Vertical #{i+1}",
            key=f"vertical_{i}"
        )
    )

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.header("Top Performing Geos")

    top_geos = []

    for i in range(5):
        top_geos.append(
            st.text_input(
                f"Top Geo #{i+1}",
                key=f"top_geo_{i}"
            )
        )

with col2:

    st.header("High Potential Geos")

    high_potential_geos = []

    for i in range(5):
        high_potential_geos.append(
            st.text_input(
                f"High Potential Geo #{i+1}",
                key=f"potential_geo_{i}"
            )
        )

st.divider()

st.header("Top Performing Media Buying Strategies")

strategies = []

for i in range(3):
    strategies.append(
        st.text_input(
            f"Strategy #{i+1}",
            key=f"strategy_{i}"
        )
    )

st.divider()

st.header("Updates")

update_1 = st.text_area("Update #1")
update_2 = st.text_area("Update #2")
update_3 = st.text_area("Update #3")

st.divider()

if st.button("Generate Report", use_container_width=True):

    st.success("Data captured successfully!")

    st.write("### Preview")

    st.write("Month:", month)

    st.write("#### Top Performing Verticals")
    for item in verticals:
        if item:
            st.write("•", item)

    st.write("#### Top Performing Geos")
    for item in top_geos:
        if item:
            st.write("•", item)

    st.write("#### High Potential Geos")
    for item in high_potential_geos:
        if item:
            st.write("•", item)

    st.write("#### Media Buying Strategies")
    for item in strategies:
        if item:
            st.write("•", item)

    st.write("#### Updates")
    for item in [update_1, update_2, update_3]:
        if item:
            st.write("•", item)
