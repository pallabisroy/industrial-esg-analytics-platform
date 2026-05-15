import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Industrial ESG Analytics Platform",
    layout="wide"
)

# -----------------------------------
# LOAD DATA
# -----------------------------------

df = pd.read_csv('../data/cleaned_wastewater.csv')

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.header("Filters")

# -----------------------------------
# COUNTRY FILTER
# -----------------------------------

countries = sorted(df['iso3_country'].unique())

select_all = st.sidebar.checkbox(
    "Select All Countries",
    value=True
)

if select_all:
    country_filter = countries
else:
    country_filter = st.sidebar.multiselect(
        "Select Countries",
        options=countries
    )

# -----------------------------------
# ACTIVITY RANGE FILTER
# -----------------------------------

activity_range = st.sidebar.slider(
    "Select Activity Range",
    float(df['activity'].min()),
    float(df['activity'].max()),
    (
        float(df['activity'].min()),
        float(df['activity'].max())
    )
)

# -----------------------------------
# FILTER DATA
# -----------------------------------

filtered_df = df[
    (df['iso3_country'].isin(country_filter)) &
    (df['activity'] >= activity_range[0]) &
    (df['activity'] <= activity_range[1])
]

# -----------------------------------
# TITLE
# -----------------------------------

st.title("Global Industrial ESG Analytics Dashboard")

st.markdown("""
Interactive sustainability analytics platform providing insights into industrial activity, operational hotspots, geospatial intelligence, and operational concentration patterns across global industrial facilities.
""")

# -----------------------------------
# KPI SECTION
# -----------------------------------

total_activity = int(filtered_df['activity'].sum())
total_facilities = filtered_df['source_id'].nunique()
total_countries = filtered_df['iso3_country'].nunique()
avg_activity = int(filtered_df['activity'].mean())

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Activity",
    f"{total_activity:,}"
)

col2.metric(
    "Total Facilities",
    f"{total_facilities:,}"
)

col3.metric(
    "Total Countries",
    total_countries
)

col4.metric(
    "Average Activity",
    f"{avg_activity:,}"
)

# -----------------------------------
# COUNTRY ACTIVITY CHART
# -----------------------------------

country_activity = (
    filtered_df.groupby('iso3_country')['activity']
    .sum()
    .sort_values(ascending=False)
    .head(15)
    .reset_index()
)

fig_country = px.bar(
    country_activity,
    x='iso3_country',
    y='activity',
    title='Top Countries by Industrial Activity',
    color='activity'
)

# -----------------------------------
# ACTIVITY DISTRIBUTION
# -----------------------------------

fig_distribution = px.histogram(
    filtered_df,
    x='activity',
    nbins=50,
    title='Industrial Activity Distribution'
)

# -----------------------------------
# CHART LAYOUT
# -----------------------------------

chart1, chart2 = st.columns(2)

chart1.plotly_chart(
    fig_country,
    use_container_width=True
)

chart2.plotly_chart(
    fig_distribution,
    use_container_width=True
)

# -----------------------------------
# GLOBAL MAP
# -----------------------------------

sample_df = filtered_df.sample(
    min(3000, len(filtered_df))
)

fig_map = px.scatter_geo(
    sample_df,
    lat='lat',
    lon='lon',
    size='activity',
    color='activity',
    hover_name='iso3_country',
    title='Global Industrial Activity Map',
    height=700
)

fig_map.update_layout(
    geo=dict(
        showland=True,
        landcolor="rgb(240,240,240)",
        showcountries=True,
    )
)

st.plotly_chart(
    fig_map,
    use_container_width=True
)

# -----------------------------------
# TOP FACILITIES
# -----------------------------------

top_facilities = (
    filtered_df.groupby('source_name')['activity']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_facilities = px.bar(
    top_facilities,
    x='source_name',
    y='activity',
    title='Top Industrial Facilities',
    color='activity'
)

st.plotly_chart(
    fig_facilities,
    use_container_width=True
)

# -----------------------------------
# ESG INSIGHTS
# -----------------------------------

st.subheader("ESG & Sustainability Insights")

st.markdown("""
- Industrial activity is concentrated across specific geographic regions.
- High operational density may indicate elevated sustainability and infrastructure pressure.
- Geospatial industrial monitoring supports ESG intelligence and operational oversight.
- Interactive analytics enables identification of industrial hotspots and operational concentration.
""")