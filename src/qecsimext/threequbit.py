"""TODO"""
import functools

import numpy as np
from qecsim import paulitools as pt
from qecsim.model import StabilizerCode, ErrorModel, Decoder, cli_description


@cli_description('3-qubit (e.g. plugin code)')
class ThreeQubitCode(StabilizerCode):
    """TODO"""

    @property
    @functools.lru_cache()
    def stabilizers(self):
        """See :meth:`qecsim.model.StabilizerCode.stabilizers`"""
        return pt.pauli_to_bsf(['ZZI', 'IZZ'])

    @property
    @functools.lru_cache()
    def logical_xs(self):
        """See :meth:`qecsim.model.StabilizerCode.logical_xs`"""
        return pt.pauli_to_bsf('XXX')

    @property
    @functools.lru_cache()
    def logical_zs(self):
        """See :meth:`qecsim.model.StabilizerCode.logical_zs`"""
        return pt.pauli_to_bsf('IIZ')

    @property
    def n_k_d(self):
        """See :meth:`qecsim.model.StabilizerCode.n_k_d`"""
        return 3, 1, 1

    @property
    def label(self):
        """See :meth:`qecsim.model.StabilizerCode.label`"""
        return '3-qubit'


@cli_description('3-qubit (e.g. plugin error model)')
class ThreeQubitErrorModel(ErrorModel):
    """TODO"""

    def probability_distribution(self, probability):
        """See :meth:`qecsim.model.ErrorModel.probability_distribution`"""
        p_i = 1 - probability
        p_x = probability
        p_y = p_z = 0
        return p_i, p_x, p_y, p_z

    def generate(self, code, probability, rng=None):
        """See :meth:`qecsim.model.ErrorModel.generate`"""
        assert isinstance(code, ThreeQubitCode)
        rng = np.random.default_rng() if rng is None else rng
        error_pauli = ''.join(rng.choice(('I', 'X', 'Y', 'Z'), size=3, p=self.probability_distribution(probability)))
        return pt.pauli_to_bsf(error_pauli)

    @property
    def label(self):
        """See :meth:`qecsim.model.ErrorModel.label`"""
        return '3-qubit'


@cli_description('3-qubit (e.g. plugin decoder)')
class ThreeQubitDecoder(Decoder):
    """TODO"""

    def decode(self, code, syndrome, **kwargs):
        """See :meth:`qecsim.model.Decoder.decode`"""
        assert isinstance(code, ThreeQubitCode)
        syndrome_to_pauli = {(0, 0): 'III', (0, 1): 'IIX', (1, 0): 'XII', (1, 1): 'IXI'}
        return pt.pauli_to_bsf(syndrome_to_pauli[tuple(syndrome)])

    @property
    def label(self):
        """See :meth:`qecsim.model.Decoder.label`"""
        return '3-qubit'
