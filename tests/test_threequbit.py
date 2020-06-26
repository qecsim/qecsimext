"""TODO"""
import math

import pytest
from qecsim import app

from qecsimext.threequbit import ThreeQubitCode, ThreeQubitErrorModel, ThreeQubitDecoder


@pytest.mark.parametrize('physical_error_rate, logical_error_rate', [
    (0.1, 0.02),  # TODO work out expected
])
def test_error_rate_reduction(physical_error_rate, logical_error_rate):
    """TODO"""
    code = ThreeQubitCode()
    error_model = ThreeQubitErrorModel()
    decoder = ThreeQubitDecoder()
    data = app.run(code, error_model, decoder, physical_error_rate, max_runs=1000)
    assert math.isclose(logical_error_rate, data['logical_failure_rate'])
    print(data)

