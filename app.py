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

st.header("Top Media Buying Strategies")

strategies = []

for i in range(3):
    strategies.append(
        st.text_input(
            f"Strategy #{i+1}",
            key=f"strategy_{i}"
        )
    )

st.divider()

st.header("Key Updates")

key_updates = st.text_area(
    "Key Updates",
    height=250,
    placeholder="Add key findings, trends, opportunities, and recommendations..."
)

st.divider()

if st.button("Generate Report", use_container_width=True):

    st.success("Report generated successfully!")

    st.markdown("---")

    st.title("Search Insights Preview")

    st.subheader(month)

    st.markdown("### Top Performing Verticals")

    for i, item in enumerate(verticals, start=1):
        if item:
            st.write(f"{i}. {item}")

    st.markdown("### Top Performing Geos")

    for i, item in enumerate(top_geos, start=1):
        if item:
            st.write(f"{i}. {item}")

    st.markdown("### High Potential Geos")

    for i, item in enumerate(high_potential_geos, start=1):
        if item:
            st.write(f"{i}. {item}")

    st.markdown("### Top Media Buying Strategies")

    for i, item in enumerate(strategies, start=1):
        if item:
            st.write(f"{i}. {item}")

    st.markdown("### Key Updates")

    st.write(key_updates)
