import pycontest
from pycontest import simulation as sim2d
import numpy as np                                                             
import pytest
import os

def test_regression():

    # initial condition and simulation params
    vel_0 = np.array([[12., 12.], [-8, -15.], [-3, 4],     [10, 0],    [2., 12.],  [-8, -15.],
                      [3,    -4], [-10, 0],   [-12., 12.], [8, -15.],  [-3, -4],   [-10, 0]])
    loc_0 = np.array([[20., 45.], [65, 70.],  [85., 90.],  [10., 10.], [50., 45.], [15, 70.],
                      [15., 90.], [45., 10.], [75., 45.],  [40, 70.],  [45., 90.], [90., 10.]])
    domain = np.array([[0., 100.], [0., 100.]])
    mass = np.array([1., 2., 1., 3, 1., 2., 1., 3, 1., 2., 1., 3])
    dt = 1 / 30.
    t_max = 30
    radius = 5

    # run simulation
    loc, vel = sim2d.simulation(t_max, dt, mass, radius, loc_0, vel_0, domain, t0=dt)

    # save reference simulations
    #np.save(os.path.join(os.path.dirname(__file__),"../data/loc_ref.npy"), loc)
    #np.save(os.path.join(os.path.dirname(__file__),"../data/vel_ref.npy"), vel)

    # read in reference values
    loc_ref = np.load(os.path.join(os.path.dirname(__file__), "../data/loc_ref.npy"))
    vel_ref = np.load(os.path.join(os.path.dirname(__file__), "../data/vel_ref.npy"))

    # from scipy docs:
    # The tolerance values are positive, typically very small numbers.
    # The relative difference (rtol * abs(b)) and the absolute difference atol
    # are added together to compare against the absolute difference 
    # between a and b.
    np.testing.assert_allclose(loc, loc_ref, atol=0, rtol=1e-9, err_msg="for locations")
    np.testing.assert_allclose(vel, vel_ref, atol=0, rtol=1e-7, err_msg="for velocities")
