import streamlit as st
import pandas as pd

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
# FILE UPLOADS
# ==================================================

st.markdown(
    "<div class='section-header'>Upload Reports</div>",
    unsafe_allow_html=True
)

themes_report = st.file_uploader(
    "Top Performing Themes Report",
    type=["csv", "xlsx"]
)

geo_report = st.file_uploader(
    "Geo Performance Report",
    type=["csv", "xlsx"]
)

media_report = st.file_uploader(
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
    placeholder="Add manual updates..."
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
# HELPER FUNCTIONS
# ==================================================

def load_file(uploaded_file):
    if uploaded_file.name.endswith(".csv"):
        return pd.read_csv(uploaded_file)
    else:
        return pd.read_excel(uploaded_file)

# ==================================================
# REPORT LOGIC
# ==================================================

if generate:

    st.success("Generating report...")

    top_geos = []
    high_potential_geos = []
    top_strategies = []

    # ------------------------------------------
    # GEO REPORT
    # ------------------------------------------

    if geo_report:

        geo_df = load_file(geo_report)

        geo_df.columns = geo_df.columns.str.strip()

        roi_geos = geo_df.sort_values(
            by="Search ROI",
            ascending=False
        )

        rpc_geos = geo_df.sort_values(
            by="Search Revenue Per Search Click",
            ascending=False
        )

        top_geos = roi_geos["Country"].head(5).tolist()

        high_potential_geos = rpc_geos["Country"].head(5).tolist()

    # ------------------------------------------
    # MEDIA BUYING REPORT
    # ------------------------------------------

    if media_report:

        media_df = load_file(media_report)

        media_df.columns = media_df.columns.str.strip()

        media_df = media_df.sort_values(
            by="Search ROI",
            ascending=False
        )

        top_strategies = media_df[
            "Ad Campaign Bid Type"
        ].head(3).tolist()

    # ==================================================
    # PREVIEW
    # ==================================================

    st.markdown("---")

    st.markdown(
        """
        <div class="preview-card">
        """,
        unsafe_allow_html=True
    )

    st.markdown("# Search Insights")

    st.markdown(f"### {month}")

    st.markdown("## Top Performing Themes")

    st.info(
        "AI Theme Generation Coming Next"
    )

    st.markdown("## Top Performing Geos")

    for i, geo in enumerate(top_geos, start=1):
        st.write(f"{i}. {geo}")

    st.markdown("## High Potential Geos")

    for i, geo in enumerate(high_potential_geos, start=1):
        st.write(f"{i}. {geo}")

    st.markdown("## Top Media Buying Strategies")

    for i, strategy in enumerate(top_strategies, start=1):
        st.write(f"{i}. {strategy}")

    st.markdown("## Key Updates")

    st.write(key_updates)

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )
