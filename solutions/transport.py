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

    # if loc or vel is list, we want to convert to numpy arrays
    if type(loc) is list:
        loc = np.array(loc)
    if type(vel) is list:
        vel = np.array(vel)

    # for numpy arrays
    if isinstance(loc, np.ndarray) and isinstance(vel, np.ndarray):
        # be sure that the type is float
        loc = loc.astype(np.float32, copy=False)
        vel = vel.astype(np.float32, copy=False)
        loc[:] = loc[:] + vel[:] *dt
    return loc