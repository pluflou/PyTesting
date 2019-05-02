import pytest

from pycontest import elastic_collisions as ec
from pycontest.utils import momentum, E_kin


# 2d are more complicated, depends on the vector r12
# but we can always check the simplest cases, that are basically 1d cases

# let's start from 2 balls that have only x velocity, and r12 also has only x component
def test_collision_2d_1():
    v1_f, v2_f = ec.collision_2d(v1=[1, 0], v2=[-2, 0], r12=[1, 0], m1=1, m2=1)
    assert (v1_f == [-2, 0]).all()
    assert (v2_f == [1, 0]).all()

# you cannow do the same for y components
def test_collision_2d_2():
    v1_f, v2_f = ec.collision_2d(v1=[0, 1], v2=[0, -2], r12=[0, 1], m1=1, m2=1)
    assert (v1_f == [0, -2]).all()
    assert (v2_f == [0, 1]).all()


# you can also check the energy and momentum

def test_collision_2d_en():
    v1_i, v2_i = [3, 1], [1, -2]
    m1, m2 = 1, 2
    v1_f, v2_f = ec.collision_2d(v1=v1_i, v2=v2_i, r12=[0, 1], m1=m1, m2=m2)
    assert E_kin([v1_i,v2_i], [m1, m2]) == E_kin([v1_f,v2_f], [m1, m2])


def test_collision_2d_mom():
    v1_i, v2_i = [3, 1], [1, -2]
    m1, m2 = 1, 2
    v1_f, v2_f = ec.collision_2d(v1=v1_i, v2=v2_i, r12=[0, 1], m1=m1, m2=m2)
    assert (momentum([v1_i,v2_i], [m1, m2]) == momentum([v1_f, v2_f], [m1, m2])).all()



