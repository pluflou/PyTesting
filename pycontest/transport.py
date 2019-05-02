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

#what if input is list:
    if type(loc) is list:
        loc = np.array(loc)
    if type(vel) is list:
        vel = np.array(vel)

    if isinstance(loc, np.ndarray) and isinstance(vel, np.ndarray):
        vel = vel.astype(np.float32, copy=False) #to cast as float without making a copy
        loc = loc.astype(np.float32, copy=False) #why not dT?
        loc[:] = loc[:] + vel[:] *dt
    return loc
