import streamlit as st
import matplotlib.pyplot as plt
from fed_batch_reactor import run_simulation

with st.expander("", expanded=True):
# Title and headers
    st.title("Bioprocess Assignment")
    st.subheader("Submitted to Dr. Bunushree Behera")

# Sidebar for parameters
st.sidebar.header("Simulation Parameters")

# Flow parameters
flow_rate = st.sidebar.slider("Flow Rate [g/L/h]", 0.0, 5.0, 1.0, step=0.1)
feed_duration = st.sidebar.slider("Feed Duration [hours]", 0, 50, 10, step=1)

# Initial conditions
st.sidebar.header("Initial Conditions")
S0 = st.sidebar.slider("Initial Substrate Concentration [g/L]", 0.0, 50.0, 20.0, step=0.1)
X0 = st.sidebar.slider("Initial Biomass Concentration [g/L]", 0.0, 10.0, 0.1, step=0.1)
P0 = st.sidebar.slider("Initial Product Concentration [g/L]", 0.0, 10.0, 0.0, step=0.1)

# Model parameters
st.sidebar.header("Model Parameters")
mu_max = st.sidebar.slider("Maximum Specific Growth Rate [1/h]", 0.0, 1.0, 0.2, step=0.01)
Ks = st.sidebar.slider("Monod Constant [g/L]", 0.0, 5.0, 0.5, step=0.1)
Yxs = st.sidebar.slider("Biomass Yield Coefficient [g/g]", 0.0, 1.0, 0.5, step=0.01)
Yps = st.sidebar.slider("Product Yield Coefficient [g/g]", 0.0, 1.0, 0.3, step=0.01)
kD = st.sidebar.slider("Death Constant [1/h]", 0.0, 0.1, 0.02, step=0.001)

# Time points for simulation
st.sidebar.header("Simulation Time")
time_end = st.sidebar.slider("Simulation Duration [hours]", 10, 100, 50, step=5)
time_points = st.sidebar.slider("Number of Time Points", 100, 1000, 500, step=50)

# Run the simulation
t, S, X, P = run_simulation(S0, X0, P0, mu_max, Ks, Yxs, Yps, kD, flow_rate, feed_duration, time_end, time_points)

# Plot results
st.header("Simulation Results")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(t, X, label="Biomass (X) [g/L]", color='green')
ax.plot(t, S, label="Substrate (S) [g/L]", color='blue')
ax.plot(t, P, label="Penicillin (P) [g/L]", color='red')

# Add labels and legend
ax.set_xlabel('Time [hours]')
ax.set_ylabel('Concentration [g/L]')
ax.set_title('Penicillin Production Simulation')
ax.grid(True)
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

st.write("Submitted by:- Rajat Goyal (702200094)")
