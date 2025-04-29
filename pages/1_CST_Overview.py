import streamlit as st

st.title("Experiment: Critical Solution Temperature for Phenol-Water System")
st.header("Aim:")
st.write("To determine the critical solution temperature for phenol-water system and find the percentage of phenol in the sample.")

st.header("Apparatus:")
st.markdown("- Boiling tube\n- Thermometer\n- Stirrer\n- Burette\n- Water bath")

st.header("Principle:")
st.write("""
Phenol and water are partially miscible at room temperature. As temperature increases, they become miscible in all proportions. The temperature at which they just become completely miscible is called the **Critical Solution Temperature (CST)**.
""")

if st.button("🚀 START THE EXPERIMENT"):
    st.switch_page("pages/2_CST_Simulator.py")
