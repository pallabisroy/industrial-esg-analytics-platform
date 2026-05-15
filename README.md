# Industrial ESG Analytics Platform

Interactive ESG analytics platform for global industrial activity intelligence using Python, Tableau, Streamlit, and geospatial analytics.

---

# Project Overview

This project analyzes global industrial operational activity data to generate ESG-focused sustainability insights, geospatial intelligence, operational concentration analysis, and interactive analytics dashboards.

The platform combines:
- Python-based exploratory data analysis (EDA)
- Interactive geospatial analytics
- Tableau executive dashboards
- Streamlit analytics application
- ESG and sustainability storytelling

This project demonstrates how industrial operational data can be transformed into actionable sustainability intelligence and business insights.

---

# Key Features

## Exploratory Data Analysis
- Data cleaning and preprocessing
- Missing value analysis
- Statistical summaries
- Distribution analysis
- Country-level operational analysis

---

## Geospatial Analytics
- Interactive global industrial activity map
- Geographic operational hotspots
- Facility-level spatial intelligence
- Operational density visualization

---

## Tableau Dashboard
Interactive Tableau dashboard featuring:
- KPI cards
- Country activity analysis
- Global operational map
- Industrial activity trends
- Top operational facilities

---

## Streamlit Analytics App
Interactive web application with:
- Country filters
- Activity range filters
- KPI monitoring
- Dynamic visualizations
- Geospatial analytics

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data analysis |
| Pandas | Data processing |
| Matplotlib | Visualization |
| Seaborn | Statistical visualization |
| Plotly | Interactive charts |
| Streamlit | Web application |
| Tableau | BI dashboarding |
| GitHub | Version control |

---

# Project Structure

```text
industrial-esg-analytics-platform
│
├── data
│   └── cleaned_wastewater.csv
│
├── notebooks
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_save_visualizations.ipynb
│
├── streamlit_app
│   └── app.py
│
├── tableau
│   └── industrial_esg_dashboard.twbx
│
├── visualizations
│   ├── activity_distribution.png
│   ├── global_activity_map.png
│   ├── top_countries_activity.png
│   ├── top_facilities.png
│   └── correlation_heatmap.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Solution Architecture

```text
                ┌────────────────────┐
                │ Industrial Dataset │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Python EDA Layer   │
                │ Pandas • Plotly    │
                └─────────┬──────────┘
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
┌───────────────────┐         ┌───────────────────┐
│ Tableau Dashboard │         │ Streamlit App     │
│ ESG Intelligence  │         │ Interactive UI    │
└───────────────────┘         └───────────────────┘
```

---

# Dashboard Preview

## Tableau Dashboard
Add Tableau dashboard screenshot here.

---

## Streamlit Analytics App
Add Streamlit app screenshot here.

---

# ESG & Sustainability Storytelling

This project demonstrates:
- industrial operational concentration analysis
- sustainability intelligence generation
- geospatial ESG hotspot identification
- operational density monitoring
- interactive industrial analytics

The platform enables exploration of global industrial operational patterns through interactive visual intelligence.

---

# Tableau Public Dashboard

Add your Tableau Public dashboard link here.

Example:

```text
https://public.tableau.com/...
```

---

# Run Streamlit App Locally

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
cd streamlit_app

streamlit run app.py
```

---

# Future Enhancements

- Snowflake integration
- Real-time ESG monitoring
- Predictive analytics
- AI-driven sustainability insights
- Advanced geospatial clustering
- Cloud deployment

---

# Author

Pallabi S Roy

---

# Project Highlights

- ESG Analytics
- Sustainability Intelligence
- Tableau Dashboarding
- Streamlit Application Development
- Geospatial Analytics
- Interactive Visualization
- Business Intelligence Storytelling
