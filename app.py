import streamlit as st
import pandas as pd
import re

st.set_page_config(
    page_title="Search Insights",
    layout="wide"
)

# ==================================================
# STYLING
# ==================================================

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.main-title {
    color: #4F6DF5;
    font-size: 64px;
    font-weight: 800;
    line-height: 0.9;
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
# BUTTON
# ==================================================

generate = st.button(
    "Generate Search Insights Report",
    use_container_width=True
)

# ==================================================
# HELPERS
# ==================================================

def load_file(uploaded_file):
    if uploaded_file.name.endswith(".csv"):
        return pd.read_csv(uploaded_file)
    return pd.read_excel(uploaded_file)

def clean_numeric(series):
    return (
        series.astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace("%", "", regex=False)
        .str.strip()
    )

# ==================================================
# REPORT
# ==================================================

if generate:

    top_geos = []
    high_potential_geos = []
    top_strategies = []

    # ----------------------------------------
    # GEO REPORT
    # ----------------------------------------

    if geo_report:

        geo_df = load_file(geo_report)

        geo_df.columns = geo_df.columns.str.strip()

        geo_df["Search ROI Numeric"] = pd.to_numeric(
            clean_numeric(geo_df["Search ROI"]),
            errors="coerce"
        )

        geo_df["RPC Numeric"] = pd.to_numeric(
            clean_numeric(
                geo_df["Search Revenue Per Search Click"]
            ),
            errors="coerce"
        )

        roi_geos = geo_df.sort_values(
            by="Search ROI Numeric",
            ascending=False
        )

        rpc_geos = geo_df.sort_values(
            by="RPC Numeric",
            ascending=False
        )

        top_geos = roi_geos[
            ["Country", "Search ROI Numeric"]
        ].head(5)

        high_potential_geos = rpc_geos[
            ["Country", "RPC Numeric"]
        ].head(5)

    # ----------------------------------------
    # MEDIA REPORT
    # ----------------------------------------

    if media_report:

        media_df = load_file(media_report)

        media_df.columns = media_df.columns.str.strip()

        media_df["Search ROI Numeric"] = pd.to_numeric(
            clean_numeric(media_df["Search ROI"]),
            errors="coerce"
        )

        media_df = media_df.sort_values(
            by="Search ROI Numeric",
            ascending=False
        )

        top_strategies = media_df[
            ["Ad Campaign Bid Type", "Search ROI Numeric"]
        ].head(3)

    # ----------------------------------------
    # PREVIEW
    # ----------------------------------------

    st.markdown("---")
    st.header("Search Insights Preview")

    st.subheader(month)

    st.markdown("## Top Performing Themes")
    st.info("AI Theme Generation Coming Next")

    st.markdown("## Top Performing Geos")

    if len(top_geos) > 0:
        for i, row in enumerate(top_geos.itertuples(), start=1):
            st.write(
                f"{i}. {row.Country} (${row._2:,.0f})"
            )

    st.markdown("## High Potential Geos")

    if len(high_potential_geos) > 0:
        for i, row in enumerate(high_potential_geos.itertuples(), start=1):
            st.write(
                f"{i}. {row.Country} ({row._2:.2f} RPC)"
            )

    st.markdown("## Top Media Buying Strategies")

    if len(top_strategies) > 0:
        for i, row in enumerate(top_strategies.itertuples(), start=1):
            st.write(
                f"{i}. {row[1]} (${row[2]:,.0f})"
            )

    st.markdown("## Key Updates")

    st.write(key_updates)
