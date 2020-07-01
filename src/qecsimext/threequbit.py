"""
This module contains qecsim extension examples for new code, error model and decoder components.
"""
import functools

import numpy as np
from qecsim import paulitools as pt
from qecsim.model import StabilizerCode, ErrorModel, Decoder, cli_description


@cli_description('3-qubit (e.g. plugin code)')
class ThreeQubitCode(StabilizerCode):
    """Implements 3-qubit bit-flip code.

    This code can correct any single bit-flip error but it fails to correct any single phase-flip error.

    Notes:

    * This class extends :class:`qecsim.model.StabilizerCode`, implementing all the abstract properties / methods.

    * This code is integrated into the command-line interface by the following entry in ``setup.cfg``:

    .. code-block:: text

        [options.entry_points]
        qecsim.cli.run.codes =
            ext_3qubit = qecsimext.threequbit:ThreeQubitCode

    * A one-line description for command-line interface help messages is provided by the class decorator
      :func:`qecsim.model.cli_description`.

    * In order to demonstrate how to implement a new code in general, we implement all the abstract properties / methods
      of :class:`qecsim.model.StabilizerCode`. However, a more concise implementation is possible by extending
      :class:`qecsim.models.basic.BasicCode`, for an example see :class:`qecsim.models.basic.FiveQubitCode`.
    """

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


@cli_description('3-qubit bit-flip (e.g. plugin error model)')
class ThreeQubitBitFlipErrorModel(ErrorModel):
    """Implements 3-qubit bit-flip error model.

    This error model applies a bit-flip with the given error probability to any of the qubits of the 3-qubit code.

    Notes:

    * This class extends :class:`qecsim.model.ErrorModel`, implementing all the abstract properties / methods.

    * This code is integrated into the command-line interface by the following entry in ``setup.cfg``:

    .. code-block:: text

        [options.entry_points]
        qecsim.cli.run.error_models =
            ext_3qubit.bit_flip = qecsimext.threequbit:ThreeQubitBitFlipErrorModel

    * A one-line description for command-line interface help messages is provided by the class decorator
      :func:`qecsim.model.cli_description`.

    * In order to demonstrate how to implement a new error model in general, we implement all the abstract properties /
      methods of :class:`qecsim.model.ErrorModel`. However, qecsim includes a generic bit-flip error model that is
      compatible with all codes, see :class:`qecsim.models.generic.BitFlipErrorModel`.
    """

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
        return '3-qubit bit-flip'


@cli_description('3-qubit lookup (e.g. plugin decoder)')
class ThreeQubitLookupDecoder(Decoder):
    """Implements 3-qubit lookup decoder.

    This decoder uses a lookup table to determine the most probable error configuration on the 3-qubit code for the
    given syndrome.

    Notes:

    * This class extends :class:`qecsim.model.Decoder`, implementing all the abstract properties / methods.

    * This code is integrated into the command-line interface by the following entry in ``setup.cfg``:

    .. code-block:: text

        [options.entry_points]
        qecsim.cli.run.decoders =
            ext_3qubit.lookup = qecsimext.threequbit:ThreeQubitLookupDecoder

    * A one-line description for command-line interface help messages is provided by the class decorator
      :func:`qecsim.model.cli_description`.

    * In order to demonstrate how to implement a new decoder in general, we implement all the abstract properties /
      methods of :class:`qecsim.model.Decoder`. However, qecsim includes a generic decoder that iteratively searches for
      a minimum-weight recovery operator for any *small* code, see :class:`qecsim.models.generic.NaiveDecoder`.
    """

    def decode(self, code, syndrome, **kwargs):
        """See :meth:`qecsim.model.Decoder.decode`"""
        assert isinstance(code, ThreeQubitCode)
        syndrome_to_pauli = {(0, 0): 'III', (0, 1): 'IIX', (1, 0): 'XII', (1, 1): 'IXI'}
        return pt.pauli_to_bsf(syndrome_to_pauli[tuple(syndrome)])

    @property
    def label(self):
        """See :meth:`qecsim.model.Decoder.label`"""
        return '3-qubit lookup'
