import pandas as pd
from openai import OpenAI

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Search Insights",
    layout="wide"
)

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# ==================================================
# STYLING
# ==================================================

st.markdown("""
<style>

.main-title {
    color: #4F6DF5;
    font-size: 72px;
    font-weight: 800;
    line-height: 0.9;
    margin-bottom: 20px;
}

.blue-pill {
    background-color: #4F6DF5;
    color: white;
    padding: 8px 16px;
    border-radius: 8px;
    font-weight: 700;
    display: inline-block;
    margin-bottom: 15px;
}

.report-title {
    font-size: 54px;
    font-weight: 800;
    color: #4F6DF5;
    line-height: 0.9;
}

.section-title {
    font-size: 32px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 10px;
}

.list-item {
    font-size: 20px;
    margin-bottom: 10px;
}

.placeholder-box {
    border: 2px dashed #D9D9D9;
    border-radius: 12px;
    height: 320px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #999999;
    font-size: 18px;
}

.update-box {
    background: #F7F8FA;
    border-left: 5px solid #4F6DF5;
    padding: 15px;
    margin-bottom: 12px;
    border-radius: 8px;
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

st.markdown("### Upload Reports")

articles_report = st.file_uploader(
    "Top Performing Articles Report",
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

key_updates = st.text_area(
    "Key Updates",
    height=200
)

st.divider()

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
# REPORT GENERATION
# ==================================================

if generate:

    top_geos = []
    high_potential_geos = []
    top_strategies = []
    
    ai_insights = None

    # ---------------- ARTICLES ----------------

    if articles_report:

        articles_df = load_file(
            articles_report
        )

        articles_df.columns = (
            articles_df.columns
            .str.strip()
        )

        top_articles = (
            articles_df.head(30)
        )

        title_column = (
            top_articles.columns[0]
        )

        titles = (
            top_articles[
                title_column
            ]
            .astype(str)
            .tolist()
        )

        titles_text = "\n".join(titles)

        prompt = f"""
Analyze these top-performing article titles.

Return:

# Top Performing Themes

# Executive Summary

# Recommendations

Do not mention article titles directly.

Article Titles:

{titles_text}
"""

        response = (
            client.chat.completions.create(
                model="gpt-5-mini",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )

        ai_insights = (
            response
            .choices[0]
            .message
            .content
        )

    # ---------------- GEO ----------------

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

        top_geos = roi_geos["Country"].head(5).tolist()

        high_potential_geos = rpc_geos["Country"].head(5).tolist()

    # ---------------- MEDIA ----------------

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
            "Ad Campaign Bid Type"
        ].head(3).tolist()

    # ==================================================
    # REPORT PREVIEW
    # ==================================================

    st.markdown("---")

    st.markdown(
        f"""
        <div class="report-title">
        Search<br>
        Insights
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"### {month}")

    st.write("")

    # ==================================================
    # CONTENT
    # ==================================================

    st.markdown(
        '<div class="blue-pill">Content</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns([1,1])

    with left:

        st.markdown(
        '<div class="section-title">Top Performing Themes</div>',
        unsafe_allow_html=True
    )

        st.markdown(
        "AI TEST"
    )

    with right:

        st.markdown(
            """
            <div class="placeholder-box">
            Theme ROI Pie Chart
            <br><br>
            (Coming Soon)
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    # ==================================================
    # MEDIA BUYING
    # ==================================================

    st.markdown(
        '<div class="blue-pill">Media Buying</div>',
        unsafe_allow_html=True
    )

    geo_col, rpc_col = st.columns(2)

    with geo_col:

        st.markdown(
            '<div class="section-title">Top Performing Geos</div>',
            unsafe_allow_html=True
        )

        for i, geo in enumerate(top_geos, start=1):
            st.markdown(
                f'<div class="list-item">{i}. {geo}</div>',
                unsafe_allow_html=True
            )

    with rpc_col:

        st.markdown(
            '<div class="section-title">High Potential Geos</div>',
            unsafe_allow_html=True
        )

        for i, geo in enumerate(high_potential_geos, start=1):
            st.markdown(
                f'<div class="list-item">{i}. {geo}</div>',
                unsafe_allow_html=True
            )

    st.write("")
    st.write("")

    st.markdown(
        '<div class="section-title">Top Performing Media Buying Strategies</div>',
        unsafe_allow_html=True
    )

    for i, strategy in enumerate(top_strategies, start=1):
        st.markdown(
            f'<div class="list-item">{i}. {strategy}</div>',
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    # ==================================================
    # KEY UPDATES
    # ==================================================

    st.markdown("---")

    st.markdown(
        '<div class="section-title">Key Updates</div>',
        unsafe_allow_html=True
    )

    updates = [
        x.strip()
        for x in key_updates.split("\n")
        if x.strip()
    ]

    for update in updates:

        st.markdown(
            f"""
            <div class="update-box">
            {update}
            </div>
            """,
            unsafe_allow_html=True
        )
