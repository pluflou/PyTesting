import numpy as np
import pytest

from hypothesis import given, strategies as st

from pycontest import simulation as sim2d                                      
from pycontest.utils import momentum, E_kin

# hypothesis simple example
@given(mass1  = st.floats(min_value=.1, max_value=1e3),
       mass2  = st.floats(min_value=.1, max_value=1e3))
def test_energy_hypothesis(mass1, mass2):

    # initial condition and simulation parameters
    domain = ([0, 20], [0, 20])
    dt = 0.5
    t_max = 6
    loc_0 = np.array([[3, 4],[15, 2]])
    vel_0 = np.array([[1, 0.5], [-1, -.25]])
    radius = 1

    # mass chosen by hypothesis
    mass = [mass1, mass2]

    # run the simulation
    loc, vel = sim2d.simulation(t_max, dt, mass, radius, loc_0, vel_0, domain)

    E_ini = E_kin(vel_0, mass)
    E_end = E_kin(vel, mass)

    print("testing for mass = {}. E_end = {}".format(mass, E_end))

    assert E_ini == E_end
