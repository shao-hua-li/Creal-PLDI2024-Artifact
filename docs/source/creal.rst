Run the Tool: Creal
=====

This is a guide of using Creal to generate new C programs.

The sourcecode is located in ``/artifact/generators/creal/``.

To generate new programs, run

.. code-block:: console

  $ cd /artifact/generators/creal/
  $ ./creal.py --dst ./tmp --syn-prob 20 --num-mutants 5

.. note::

  ``--dst``: path to the directory where programs will be saved.

  ``--syn-prob``: synthesis probabiliy (0~100).

  ``--num-mutants``: number of mutants per seed.

This script will first invoke Csmith to generate a seed program and then generate mutated programs. 
The seed program will be saved in the directory specified by ``"--dst"``, which is ``"./tmp"`` in the command above.
