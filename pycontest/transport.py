import numpy as np

def transport(loc, vel, dt):
    """transport equations
    Args:
         loc: initial location (can be int/float or array)
         vel: velocity (can be int/float or array)
         dt: time step

    Returns:
        location after one time step
     """

    # if loc, vel are simple numbers
    if isinstance(loc, (int, float)) and isinstance(vel, (int, float)):
        loc = loc + vel * dt

    if isinstance(loc, np.ndarray) and isinstance(vel, np.ndarray):
        vel = vel.astype(np.float32, copy=False)
        loc[:] = loc[:] + vel[:] *dt
    return loc