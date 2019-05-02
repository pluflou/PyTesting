import pycontest
from pycontest import simulation as sim2d
import numpy as np                                                             
import pytest
import os

@pytest.mark.skip(reason="TODO")
def test_regression():

    # initial condition and simulation params

    # run simulation
    loc, vel = sim2d.simulation(...)

    # save reference simulations (only once when the test is created)
    np.save(os.path.join(os.path.dirname(__file__),"../data/locations_ref.npy"), loc)

    # read in reference values (every time the test is run)
    loc_ref = np.load(os.path.join(os.path.dirname(__file__), "../data/locations_ref.npy"))

    # from scipy docs:
    # The tolerance values are positive, typically very small numbers.
    # The relative difference (rtol * abs(b)) and the absolute difference atol
    # are added together to compare against the absolute difference 
    # between a and b.
    np.testing.assert_allclose(loc, loc_ref, atol=0, rtol=1e-9, err_msg="for locations")
