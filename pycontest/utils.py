import numpy as np

def E_kin(vel, mass):
    """ calculate the kinematic energy of all particles.

    Arguments:
        vel: velocities
        mass: masses

    Returns:
        Total kinetic energy
    """
    vel = np.array(vel)
    mass = np.array(mass)
    v_sq = vel**2
    return 0.5 * np.sum((mass*v_sq.transpose()).transpose())

def momentum(vel, mass):
    """ calculate the momentum of all particles

    Arguments:
        vel: velocities
        mass: masses

    Returns:
            Total momentum
    """
    vel = np.array(vel)
    mass = np.array(mass)
    return np.sum((mass*vel.transpose()).transpose(), axis=0)
