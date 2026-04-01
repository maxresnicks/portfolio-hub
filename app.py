import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Max Resnick | Portfolio", page_icon="📊", layout="centered")

# --- HEADER SECTION ---
st.title("Max Resnick")
st.subheader("Analytical Operations Professional")
st.write("""
Building scalable reporting infrastructure, data models, and automated workflows to solve complex operational bottlenecks. 
Proven track record of aiding in technical operations, translating messy data into actionable strategy for cross-functional teams, and leveraging AI & automation tools.
""")

# --- SOCIAL LINKS ---
st.write("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.link_button("💻 GitHub", "https://github.com/maxresnicks", use_container_width=True)
with col2:
    st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/resnick7", use_container_width=True)
with col3:
    st.link_button("📧 Email Me", "mailto:maxresnick1996@gmail.com", use_container_width=True)
with col4:
    st.link_button("📄 View Resume", "https://docs.google.com/document/d/1ZnIy8_TlLTdT-5rCvUtZiYBw_lvi7ahqPYcQ3GuhWjY/edit?usp=sharing", use_container_width=True) # Swap with a Google Drive link to your PDF later!

# --- PROJECTS GALLERY ---
st.write("---")
st.header("Featured Projects")

# Project 1: Two Chairs / Healthcare
st.subheader("Healthcare Operations & Capacity Pipeline")
st.write("**Tech Stack:** Python, Streamlit, DuckDB, Pandas")
st.write("""
An end-to-end data pipeline built to model clinical supply against patient demand. 
Ingests simulated EMR/HR data, audits historical patient attrition, and features an interactive sensitivity model to project the impact of new clinical hires on regional waitlists.
""")
# Buttons for the project
p1_col1, p1_col2 = st.columns([1, 1])
with p1_col1:
    st.link_button("Live Dashboard", "https://mental-healthcare-operations.streamlit.app/")
with p1_col2:
    st.link_button("View Source Code", "https://github.com/maxresnicks/mental-healthcare-pipeline")


