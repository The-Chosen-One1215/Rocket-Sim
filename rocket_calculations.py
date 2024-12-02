# rocket_calculations.py
import math

def thrust_force(m_dot, V_e, V_0):
    return m_dot * (V_e - V_0)

def specific_impulse(F_thrust, m_dot, g0=9.81):
    return F_thrust / (m_dot * g0)

def delta_v(Isp, m0, mf, g0=9.81):
    return Isp * g0 * math.log(m0 / mf)

def drag_force(C_d, A, rho, V):
    return 0.5 * C_d * A * rho * V**2
