qecsimext
=========

**qecsimext** is an example Python 3 package that extends `qecsim`_ with
additional components.

.. _qecsim: https://github.com/qecsim/qecsim

The qecsim package is a quantum error correction simulator, which can be
extended with new codes, error models and decoders that integrate into its
command-line interface. This qecsimext package includes very basic examples of
such components to provide a starting point for developing more sophisticated
components.


Installation
------------

Since qecsimext is intended as an example of how to develop extensions for
qecsim, we will download the repository and install qecsimext in editable mode
in a virtual environment.
(Alternatively, you may choose to `clone`_ or `fork`_ the qecsimext repository
instead of downloading it.)

.. _clone: https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository
.. _fork: https://docs.github.com/en/github/getting-started-with-github/fork-a-repo

* Download the repository: `qecsimext-0.1b9.zip`_

.. _qecsimext-0.1b9.zip: https://github.com/qecsim/qecsimext/archive/0.1b9.zip

* Install qecsimext in editable mode with developer dependencies:

.. code-block:: text

    $ unzip qecsimext-0.1b9.zip             # extract repo (Windows: tar -xf qecsimext-0.1b9.zip)
    $ cd qecsimext-0.1b9
    $ python3 --version                     # qecsimext requires Python 3.5+
    Python 3.7.8
    $ python3 -m venv venv                  # create virtual environment
    $ source venv/bin/activate              # activate venv (Windows: venv\Scripts\activate)
    (venv) $ pip install -U setuptools pip  # install / upgrade setuptools and pip
    ...
    Successfully installed pip-21.0.1 setuptools-52.0.0
    (venv) $ pip install -e .[dev]          # install qecsimext with dev tools
    ...
    Successfully installed ... qecsimext ...
    (venv) $ deactivate                     # deactivate venv
    $


* Test installation:

.. code-block:: text

    $ source venv/bin/activate              # activate venv (Windows: venv\Scripts\activate)
    (venv) $ pytest                         # run tests
    ...
    ==== 3 passed in 1.34s =====

* Run simulation example via console script:

.. code-block:: text

    $ source venv/bin/activate              # activate venv (Windows: venv\Scripts\activate)
    (venv) $ qecsim run -r100 "ext_3qubit" "ext_3qubit.bit_flip" "ext_3qubit.lookup" 0.3
    ...
    [{"code": "3-qubit", "decoder": "3-qubit lookup", "error_model": "3-qubit bit-flip", "error_probability": 0.3, "logical_failure_rate": 0.22, ..., "wall_time": 0.043655599000000045}]

* Run simulation example via module script with Python optimize flag:

.. code-block:: text

    $ source venv/bin/activate              # activate venv (Windows: venv\Scripts\activate)
    (venv) $ python3 -O -m qecsim run -r100 "ext_3qubit" "ext_3qubit.bit_flip" "ext_3qubit.lookup" 0.3
    ...
    [{"code": "3-qubit", "decoder": "3-qubit lookup", "error_model": "3-qubit bit-flip", "error_probability": 0.3, "logical_failure_rate": 0.22, ..., "wall_time": 0.03045584499999965}]


New components
--------------

New components can be implemented and integrated into the command-line
interface as described below. See also the `qecsim documentation`_.

.. _qecsim documentation: https://qecsim.github.io/


Implementation
~~~~~~~~~~~~~~

New codes, error models or decoders are implemented by writing classes that
extend ``qecsim.model.StabilizerCode``, ``qecsim.model.ErrorModel`` or
``qecsim.model.Decoder``, respectively. (Fault-tolerant decoders extend
``qecsim.model.DecoderFTP``). See `<./src/qecsimext/threequbit.py>`__ for
examples.


CLI integration
~~~~~~~~~~~~~~~

New codes, error models or decoders are integrated into the command-line
interface via entries in the ``[options.entry-points]`` section of
`<./setup.cfg>`__ under the keys ``qecsim.cli.run.codes``,
``qecsim.cli.run.error_models`` or ``qecsim.cli.run.decoders``, respectively.
(Fault-tolerant compatible components are under ``qecsim.cli.run_ftp.*`` keys).
The format of entries is ``<short_name> = <module_path>:<class_name>``. See
`<./setup.cfg>`__ for examples.

Optionally, one-line descriptions for command-line interface help messages can
be provided by decorating implementation classes with
``qecsim.model.cli_description``. See `<./src/qecsimext/threequbit.py>`__ for
examples.


Notes
~~~~~

* Since we installed qecsimext in editable mode there is no need to upgrade the
  installation after source code changes. However, after modifying
  `<./setup.cfg>`__, the qecsimext installation must be upgraded:

.. code-block:: text

    $ source venv/bin/activate              # activate venv (Windows: venv\Scripts\activate)
    (venv) $ pip install -U -e .[dev]       # upgrade qecsimext
    ...
    Successfully installed qecsimext


* When developing new components, qecsimext may be used as a starting point.
  However, if you intend to put the components in the public domain then it
  would be good practice to use a unique repository and root package name.


Tools
_____

Tasks for running tests with coverage, checking style, generating documentation
and building source and binary distributables can be executed using tox_. See
`<./tox.ini>`__ for more details.

.. _tox: https://tox.readthedocs.io/

For example, distributables can be built as follows:

.. code-block:: text

    $ source venv/bin/activate              # activate venv (Windows: venv\Scripts\activate)
    (venv) $ tox -ebuild                    # build qecsimext distributables
    ...
    (venv) $ ls ./dist/                     # list qecsimext distributables
    qecsimext-0.1b9-py3-none-any.whl    qecsimext-0.1b9.tar.gz


License / Citing
----------------

qecsimext is released under the BSD 3-Clause license; see `<LICENSE>`__.

If you use qecsim in your research, please see the `qecsim documentation`_ for
citing details.


Links
-----

* Source code: https://github.com/qecsim/qecsimext
* qecsim source code: https://github.com/qecsim/qecsim
* qecsim documentation: https://qecsim.github.io/
* Contact: qecsim@gmail.com

----

Copyright 2016 - 2021, David K. Tuckett.
