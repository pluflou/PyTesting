import pytest

from pycontest import elastic_collisions as ec
from pycontest.utils import momentum, E_kin


# a simple tests for equal masses (balls should exchange velocities)

# using default values of m1 and m2
def test_collision_1d_1():
    v1_f, v2_f = ec.collision_1d(v1_i=1, v2_i=-2)
    assert v1_f == -2
    assert v2_f == 1

# the same masses, but specifying the values
def test_collision_1d_2():
    v1_f, v2_f = ec.collision_1d(v1_i=1, v2_i=-2, m1=2, m2=2)
    assert v1_f == -2
    assert v2_f == 1

# we can imagine what happens when one ball is much heavier.
# The heavy ball won't change the velocity too much
# we can use pytest.approx
def test_collision_1d_3():
    v1_f, v2_f = ec.collision_1d(v1_i=1, v2_i=-2, m1=1, m2=1e6)
    assert v2_f == pytest.approx(-2, rel=1e-3)



# it is hard to know the answer when masses are completely independed,
# but we still can test if we don't break any physical lawa
# we can tests total kinetic energy and total momentum

def test_collision_1d_en():
    v1_i, v2_i = 1, -2
    m1, m2 = 1, 3
    v1_f, v2_f = ec.collision_1d(v1_i, v2_i, m1, m2)
    assert E_kin([v1_i, v2_i], [m1, m2]) == E_kin([v1_f, v2_f], [m1, m2])


def test_collision_1d_mom():
    v1_i, v2_i = 1, -2
    m1, m2 = 1, 3
    v1_f, v2_f = ec.collision_1d(v1_i, v2_i, m1, m2)
    assert momentum([v1_i, v2_i], [m1, m2]) == momentum([v1_f, v2_f], [m1, m2])
