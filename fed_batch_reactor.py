import numpy as np
from scipy.integrate import odeint

def penicillin_model(y, t, mu_max, Ks, Yxs, Yps, kD, flow_rate, feed_duration):
    """
    Differential equations for the penicillin production model.

    Parameters:
        y : list [S, X, P]
            Current state variables: Substrate (S), Biomass (X), Product (P).
        t : float
            Current time.
        mu_max : float
            Maximum specific growth rate [1/h].
        Ks : float
            Monod constant [g/L].
        Yxs : float
            Biomass yield coefficient [g/g].
        Yps : float
            Product yield coefficient [g/g].
        kD : float
            Death constant [1/h].
        flow_rate : float
            Rate of substrate addition [g/L/h].
        feed_duration : float
            Duration for substrate feeding [hours].

    Returns:
        list: Derivatives [dSdt, dXdt, dPdt].
    """
    S, X, P = y
    mu = mu_max * (S / (Ks + S))  # Specific growth rate using Monod equation
    feed = flow_rate if t <= feed_duration else 0
    dXdt = (mu - kD) * X
    dSdt = feed - mu * X / Yxs
    dPdt = mu * X / Yps
    return [dSdt, dXdt, dPdt]

def run_simulation(S0, X0, P0, mu_max, Ks, Yxs, Yps, kD, flow_rate, feed_duration, time_end, time_points):
    """
    Runs the penicillin production simulation.

    Parameters:
        S0, X0, P0 : float
            Initial concentrations of Substrate (S), Biomass (X), Product (P).
        mu_max, Ks, Yxs, Yps, kD : float
            Model parameters.
        flow_rate, feed_duration : float
            Flow parameters.
        time_end : float
            Total simulation time [hours].
        time_points : int
            Number of points in the time array.

    Returns:
        tuple: Time array (t), Substrate (S), Biomass (X), Product (P).
    """
    t = np.linspace(0, time_end, time_points)
    initial_conditions = [S0, X0, P0]
    solution = odeint(
        penicillin_model,
        initial_conditions,
        t,
        args=(mu_max, Ks, Yxs, Yps, kD, flow_rate, feed_duration)
    )
    S, X, P = solution.T
    return t, S, X, P
