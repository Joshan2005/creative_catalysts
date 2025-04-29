import streamlit as st

st.title("Experiment: Conductometric Titration")

st.header("Aim:")
st.write("To find the strength of HCl and CH₃COOH in a given mixture using NaOH solution, conductometrically.")

st.header("Apparatus:")
st.markdown("- Conductivity meter\n- Burette\n- Beakers\n- Pipettes")

st.header("Principle:")
st.write("""
During titration, conductivity changes due to ion replacement. Strong acid (HCl) shows a V-curve. Weak acid (CH₃COOH) shows a rising curve due to salt formation and OH⁻.
""")

if st.button("🚀 START THE EXPERIMENT"):
    st.switch_page("pages/4_Conductometry_Simulator.py")
