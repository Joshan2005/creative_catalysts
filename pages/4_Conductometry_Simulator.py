import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Conductometric Titration Simulator", layout="centered")

# Title
st.title("⚡ Conductometric Titration Simulator")
st.write("""
This simulator helps visualize how **conductivity** changes during titration of different acid systems with NaOH.
""")

# Select the system
acid_type = st.selectbox("Select Acid System:", ["HCl only", "CH₃COOH only", "Mixture (HCl + CH₃COOH)"])

# User-defined max NaOH volume
volume_added = st.slider("Set Maximum Volume of NaOH added (mL)", min_value=5.0, max_value=30.0, value=15.0, step=0.5)

# Generate x-values (NaOH volumes)
volumes = np.arange(0, volume_added + 0.5, 0.5)
conductance = []

# Simulate based on system
if acid_type == "HCl only":
    for v in volumes:
        if v < 7:
            c = 10 - v  # decreasing due to H+ replaced by Na+
        else:
            c = 2 + (v - 7) * 0.8  # increase due to OH-
        conductance.append(c)

elif acid_type == "CH₃COOH only":
    for v in volumes:
        if v < 8:
            c = 4 + v * 0.5  # gradual increase due to salt formation
        else:
            c = 8 + (v - 8) * 1.2  # sharp increase from OH-
        conductance.append(c)

else:  # Mixture
    for v in volumes:
        if v < 5:
            c = 10 - v * 1.2  # HCl neutralization
        elif v < 12:
            c = 5 + (v - 5) * 0.5  # CH3COOH neutralization
        else:
            c = 8 + (v - 12) * 1.5  # OH- dominates
        conductance.append(c)

# Plotting
fig, ax = plt.subplots()
ax.plot(volumes, conductance, marker='o', linestyle='-', color='blue')
ax.set_title("Conductance vs Volume of NaOH Added")
ax.set_xlabel("Volume of NaOH (mL)")
ax.set_ylabel("Conductance (mS)")
ax.grid(True)
st.pyplot(fig)

# Theory section
with st.expander("📘 Theoretical Background"):
    st.write("""
    - **Conductometric titration** measures the change in electrical conductivity during neutralization.
    - **HCl (strong acid):** High initial conductance due to H⁺ → drops as replaced by slower Na⁺ → rises with OH⁻.
    - **CH₃COOH (weak acid):** Conductivity increases steadily as salt (strong electrolyte) forms → then jumps with OH⁻.
    - **Mixture:** Shows a two-stage curve with HCl endpoint first, followed by CH₃COOH.
    """)

# Footer
st.success("✅ Simulation complete. You can change system or volume and re-run.")
