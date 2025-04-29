import streamlit as st

st.set_page_config(page_title="Creative Catalysts", layout="centered")

st.markdown("<h1 style='text-align: center;'>WELCOME TO CREATIVE CATALYSTS</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>a virtual heat transfer lab powered by chemical engineering students of SRM</h3>", unsafe_allow_html=True)

st.markdown("---")
st.subheader("Choose an experiment to begin:")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔬 Critical Solution Temperature (Phenol-Water)"):
        st.switch_page("pages/1_CST_Overview.py")
with col2:
    if st.button("⚡ Conductometric Titration"):
        st.switch_page("pages/3_Conductometry_Overview.py")
