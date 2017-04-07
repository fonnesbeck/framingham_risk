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
    test_vals = [('f', t, 30, 22.5, 125.0, False, False, False) for t in np.arange(10)+1]
    assert np.all(frs(*vals) > 0 for vals in test_vals)
    
def test_mc_precision():
    test_vals = 'm', 10, 30, 22.5, 125.0, True, True, True
    assert_almost_equal(frs(*test_vals), frs(*test_vals, ci=True)[0], decimal=4)