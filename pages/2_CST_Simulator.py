import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("🔬 CST Simulator: Phenol-Water System")

st.write("Adjust water added to phenol and observe temperature at which turbidity disappears.")

volume_water = st.slider("Volume of water added to 5 mL phenol (mL)", 3, 30, 5, 1)

# Mock logic
phenol_percent = (5 / (5 + volume_water)) * 100
temp = 40 + np.exp(-(volume_water - 15)**2 / 30) * 35  # bell curve

st.metric("Volume % of Phenol", f"{phenol_percent:.1f}%")
st.metric("Miscibility Temperature (°C)", f"{temp:.1f}")

fig, ax = plt.subplots()
vols = np.arange(3, 31, 1)
temps = 40 + np.exp(-(vols - 15)**2 / 30) * 35
ax.plot(vols, temps)
ax.set_xlabel("Volume of Water (mL)")
ax.set_ylabel("Miscibility Temp (°C)")
ax.set_title("Mean Temp vs Phenol %")
st.pyplot(fig)
