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

    cetem_publico.download() # downloads small 10KB file
    # or
    cetem_publico.download(full=True) # downloads full 12GB file

    cp = cetem_publico.load()

    print(cp.tagged_sents())


