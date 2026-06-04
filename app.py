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
# REPORT UPLOADS
# ==================================================

st.markdown(
    "<div class='section-header'>Upload Reports</div>",
    unsafe_allow_html=True
)

articles_report = st.file_uploader(
    "Top Performing Themes Report (Articles)",
    type=["csv", "xlsx"]
)

geo_report = st.file_uploader(
    "Geo Performance Report",
    type=["csv", "xlsx"]
)

media_buying_report = st.file_uploader(
    "Media Buying Strategies Report",
    type=["csv", "xlsx"]
)

st.divider()

# ==================================================
# KEY UPDATES
# ==================================================

st.markdown(
    "<div class='section-header'>Key Updates</div>",
    unsafe_allow_html=True
)

key_updates = st.text_area(
    "",
    height=200,
    placeholder="Add manual updates, partner recommendations, trends, and observations..."
)

st.divider()

# ==================================================
# GENERATE BUTTON
# ==================================================

generate = st.button(
    "Generate Search Insights Report",
    use_container_width=True
)

# ==================================================
# PREVIEW
# ==================================================

if generate:

    st.success("Reports uploaded successfully!")

    st.markdown("---")

    st.markdown(
        """
        <div class="preview-card">
        """,
        unsafe_allow_html=True
    )

    st.markdown("## Search Insights")
    st.markdown(f"### {month}")

    st.markdown("### Uploaded Reports")

    if articles_report:
        st.write("✅ Themes Report Uploaded")

    if geo_report:
        st.write("✅ Geo Report Uploaded")

    if media_buying_report:
        st.write("✅ Media Buying Report Uploaded")

    st.markdown("### Key Updates")

    st.write(key_updates)

    st.markdown(
        """
        🚧 Next Version:
        <br><br>
        • Read uploaded files
        <br>
        • Generate Top Performing Themes
        <br>
        • Generate Top Performing Geos
        <br>
        • Generate High Potential Geos
        <br>
        • Generate Top Media Buying Strategies
        <br>
        • Create ROI pie chart
        <br>
        • Export PDF
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)
