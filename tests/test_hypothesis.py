import numpy as np
import pytest

from hypothesis import given, strategies as st

from pycontest import simulation as sim2d
from pycontest.utils import momentum, E_kin

#@pytest.mark.skip(reason="TODO")                                               
@given(mass1  = st.floats(min_value=.00001, max_value=1e8),
       mass2  = st.floats(min_value=-5, max_value=-1)) #so we have to make sure inputs make sense physically otherwise test is meaningless?

#checking energy conservation for a range of masses

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

    print("testing for mass = {}. E_ini= {}. E_end = {}".format(mass, E_ini, E_end))
    pass
