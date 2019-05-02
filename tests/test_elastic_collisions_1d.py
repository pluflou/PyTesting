import pytest

from pycontest import elastic_collisions as ec
from pycontest.utils import momentum, E_kin


# a simple tests for equal masses (balls should exchange velocities)

# using default values of m1 and m2
def test_collision_1d_1():
    v1_f, v2_f = ec.collision_1d(v1_i=1, v2_i=-2)


