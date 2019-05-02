import numpy as np
import pytest

from hypothesis import given, strategies as st

from pycontest import simulation as sim2d
from pycontest.utils import momentum, E_kin

@pytest.mark.skip(reason="TODO")                                               
@given(mass1  = st.floats(min_value=.1, max_value=1e3),
       mass2  = st.floats(min_value=.1, max_value=1e3))
def test_energy_hypothesis(mass1, mass2):

    pass
