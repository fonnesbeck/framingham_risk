from ..frs import frs
from numpy.testing import assert_almost_equal
import numpy as np

def test_women():
    test_vals = 'f', 10, 30, 22.5, 125.0, False, False, False
    assert_almost_equal(frs(*test_vals), 0.0108012)

def test_men():
    test_vals = 'm', 10, 30, 22.5, 125.0, True, True, True
    assert_almost_equal(frs(*test_vals), 0.0838895)
    
def test_increasing_risk():
    test_vals = 'f', np.arange(10)+1, 30, 22.5, 125.0, False, False, False
    assert (frs(*test_vals) > 0).all()