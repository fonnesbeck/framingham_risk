from ..frs import frs
from numpy.testing import assert_almost_equal

def test_women():
    test_vals = 'f', 30, 22.5, 125.0, False, False, False
    assert_almost_equal(frs(*test_vals), 0.0108012)

def test_men():
    test_vals = 'm', 30, 22.5, 125.0, True, True, True
    assert_almost_equal(frs(*test_vals), 0.0838895)
    