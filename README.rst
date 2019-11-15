cetem_publico
=============

`cetem_publico` is a Python wrapper for the CETEMPublico corpus. It
takes care of downloading, storing and importing the corpus into NLTK.

Installing
----------

Install and update using `pip`:

.. code-block:: text

    pip install [--user] cetem_publico


A Simple Example
----------------

.. code-block:: python

    import cetem_publico

    cetem_publico.download() # downloads small version (10KB)
                             # use full=True to download the full 12GB version

    cp = cetem_publico.load()

    print(cp.tagged_sents())


