qecsimext
=========

**qecsimext** is an example Python 3 package that extends `qecsim`_ with
additional components.

.. _qecsim: https://bitbucket.org/qecsim/qecsim/

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

* Download the repository: `qecsimext-repo-0.1b2.zip`_

.. _qecsimext-repo-0.1b2.zip: https://bitbucket.org/qecsim/qecsimext/downloads/qecsimext-repo-0.1b2s.zip

* Install qecsimext in editable mode with developer dependencies:

.. code-block:: text

    $ unzip qecsimext-repo-0.1b2.zip        # extract repo (Windows: tar -xf qecsimext-repo-0.1b2.zip)
    $ cd qecsimext
    $ python3 --version                     # qecsimext requires Python 3.5+
    Python 3.7.7
    $ python3 -m venv venv                  # create virtual environment
    $ source venv/bin/activate              # activate venv (Windows: venv\Scripts\activate)
    (venv) $ pip install -U setuptools pip  # install / upgrade setuptools and pip
    ...
    Successfully installed pip-20.1.1 setuptools-47.3.1
    (venv) $ pip install deps/qecsim-1.0b2-py3-none-any.whl # TODO: remove when qecsim on PyPI
    ...
    Successfully installed ... qecsim-1.0b2 ...
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
    ==== 3 passed in 1.40s =====

* Run simulation example:

.. code-block:: text

    $ source venv/bin/activate              # activate venv (Windows: venv\Scripts\activate)
    (venv) $ qecsim run -r100 "ext_3qubit" "ext_3qubit.bit_flip" "ext_3qubit.lookup" 0.3
    ...
    [{"code": "3-qubit", "decoder": "3-qubit lookup", "error_model": "3-qubit bit-flip", "error_probability": 0.3, "logical_failure_rate": 0.22, ...}]


New components
--------------

New components can be implemented and integrated into the command-line
interface as described below. See also the `qecsim documentation`_.

.. _qecsim documentation: https://davidtuckett.com/qit/qecsim/

Implementation
~~~~~~~~~~~~~~

New codes, error models or decoders are implemented by writing classes that
extend ``qecsim.model.StabilizerCode``, ``qecsim.model.ErrorModel`` or
``qecsim.model.Decoder``, respectively. (Fault-tolerant decoders extend
``qecsim.model.DecoderFTP``). See ``./src/qecsimext/threequbit.py`` for
examples.

CLI integration
~~~~~~~~~~~~~~~

New codes, error models or decoders are integrated into the command-line
interface via entries in the ``[options.entry-points]`` section of
``./setup.cfg`` under the keys ``qecsim.cli.run.codes``,
``qecsim.cli.run.error_models`` or ``qecsim.cli.run.decoders``, respectively.
(Fault-tolerant compatible components are under ``qecsim.cli.run_ftp.*`` keys).
The format of entries is ``<short_name> = <module_path>:<class_name>``. See
``./setup.cfg`` for examples.

Optionally, one-line descriptions for command-line interface help messages can
be provided by decorating implementation classes with
``qecsim.model.cli_description``. See ``./src/qecsimext/threequbit.py`` for
examples.

Notes
~~~~~

* Since we installed qecsimext in editable mode there is no need to upgrade the
  installation after source code changes. However, after modifying
  ``setup.cfg``, the qecsimext installation must be upgraded:

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

Tasks for running tests with coverage, generating documentation and building
source and binary distributables can be executed using tox_. See ``./tox.ini``
for more details.

.. _tox: https://tox.readthedocs.io/

For example, distributables can be built as follows:

.. code-block:: text

    $ source venv/bin/activate              # activate venv (Windows: venv\Scripts\activate)
    (venv) $ tox -ebuild                    # build qecsimext distributables
    ...
    (venv) $ ls ./dist/                     # list qecsimext distributables
    qecsimext-0.1b2-py3-none-any.whl    qecsimext-0.1b2.tar.gz


Links
-----

* Source code: https://bitbucket.org/qecsim/qecsimext/
* qecsim source code: https://bitbucket.org/qecsim/qecsim/
* qecsim documentation: https://davidtuckett.com/qit/qecsim/
* Contact: qecsim@gmail.com

----

Copyright 2016, David Tuckett.
