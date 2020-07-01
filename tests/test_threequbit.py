"""
This module contains tests of the qecsim extension examples defined in :mod:`qecsimext.threequbit`.
"""
import math

import pytest
from qecsim import app

from qecsimext.threequbit import ThreeQubitCode, ThreeQubitBitFlipErrorModel, ThreeQubitLookupDecoder


@pytest.mark.parametrize('p', [
    0.1, 0.2, 0.3,
])
def test_threequbit_error_rate_reduction(p):
    """Test that the 3-qubit code with bit-flip noise and minimum-weight decoding reduces the error rate as expected."""
    # calculate expected logical error rate
    # 3 ways to fail with 2 bit-flips and 1 way to fail with 3 bit-flips
    expected_logical_p = 3 * (1 - p) * p ** 2 + p ** 3
    # initialise models
    code = ThreeQubitCode()
    error_model = ThreeQubitBitFlipErrorModel()
    decoder = ThreeQubitLookupDecoder()
    # run simulations (with seeded random number generator for test consistency)
    data = app.run(code, error_model, decoder, p, max_runs=1000, random_seed=13)
    # extract logical error rate
    recorded_logical_p = data['logical_failure_rate']
    # check logical error rate is less than physical error rate
    assert recorded_logical_p < p
    # check logical error rate is within 20% of expected logical error rate
    assert math.isclose(expected_logical_p, recorded_logical_p, rel_tol=0.2)
