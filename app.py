import streamlit as st

st.set_page_config(
    page_title="Search Insights",
    layout="wide"
)

# ==================================================
# CUSTOM STYLING
# ==================================================

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

.main-title {
    color: #4F6DF5;
    font-size: 64px;
    font-weight: 800;
    line-height: 0.9;
    margin-bottom: 10px;
}

.section-header {
    background-color: #4F6DF5;
    color: white;
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 22px;
    font-weight: 700;
    display: inline-block;
    margin-bottom: 20px;
}

.preview-card {
    background: #F8F9FC;
    padding: 30px;
    border-radius: 12px;
    border: 1px solid #E5E7EB;
    margin-top: 30px;
}

.preview-title {
    color: #4F6DF5;
    font-size: 42px;
    font-weight: 800;
    line-height: 0.9;
}

.small-spacer {
    height: 15px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

st.markdown(
    """
    <div class="main-title">
    Search<br>
    Insights
    </div>
    """,
    unsafe_allow_html=True
)

month = st.text_input(
    "Month",
    placeholder="June 2026"
)

st.divider()

# ==================================================
# CONTENT
# ==================================================

st.markdown(
    "<div class='section-header'>Content</div>",
    unsafe_allow_html=True
)

st.subheader("Top Performing Verticals")

verticals = []

for i in range(5):
    verticals.append(
        st.text_input(
            f"{i+1}.",
            key=f"vertical_{i}"
        )
    )

st.divider()

# ==================================================
# MEDIA BUYING
# ==================================================

st.markdown(
    "<div class='section-header'>Media Buying</div>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.subheader("Top Performing Geos")

    top_geos = []

    for i in range(5):
        top_geos.append(
            st.text_input(
                f"{i+1}. ",
                key=f"top_geo_{i}"
            )
        )

with col2:

    st.subheader("High Potential Geos")

    high_potential_geos = []

    for i in range(5):
        high_potential_geos.append(
            st.text_input(
                f"{i+1}.  ",
                key=f"potential_geo_{i}"
            )
        )

st.markdown("")

st.subheader("Top Media Buying Strategies")

strategies = []

for i in range(3):
    strategies.append(
        st.text_input(
            f"{i+1}.   ",
            key=f"strategy_{i}"
        )
    )

st.divider()

# ==================================================
# KEY UPDATES
# ==================================================

st.subheader("Key Updates")

key_updates = st.text_area(
    "",
    height=200,
    placeholder="Add key findings, opportunities, trends, and recommendations..."
)

st.divider()

# ==================================================
# GENERATE REPORT
# ==================================================

generate = st.button(
    "Generate Search Insights Report",
    use_container_width=True
)

# ==================================================
# REPORT PREVIEW
# ==================================================

if generate:

    st.success("Report generated successfully!")

    st.markdown("---")

    st.markdown(
        """
        <div class="preview-card">
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="preview-title">
        Search<br>
        Insights
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"### {month}")

    st.markdown("## Top Performing Verticals")

    for i, item in enumerate(verticals, start=1):
        if item:
            st.write(f"{i}. {item}")

    st.markdown("## Top Performing Geos")

    for i, item in enumerate(top_geos, start=1):
        if item:
            st.write(f"{i}. {item}")

    st.markdown("## High Potential Geos")

    for i, item in enumerate(high_potential_geos, start=1):
        if item:
            st.write(f"{i}. {item}")

    st.markdown("## Top Media Buying Strategies")

    for i, item in enumerate(strategies, start=1):
        if item:
            st.write(f"{i}. {item}")

    st.markdown("## Key Updates")

    st.write(key_updates)

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )
