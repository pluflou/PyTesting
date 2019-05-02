import numpy as np

def E_kin(vel, mass):
    """ calculate the kinematic energy of all particles """
    vel = np.array(vel)
    mass = np.array(mass)
    return 0.5 * np.sum(mass * vel**2)

def momentum(vel, mass):
    """ calculate the momentum of all particles """
    vel = np.array(vel)
    mass = np.array(mass)
    return np.sum(mass * vel, axis=0)
