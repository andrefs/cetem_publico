cetem_publico
=============

``cetem-publico`` is a Python wrapper for the CETEMPublico corpus. It
takes care of downloading, storing and importing the corpus into NLTK.

Installing
----------

Install and update using `pip`:

.. code-block:: text

    pip install [--user] cetem-publico


A Simple Example
----------------

.. code-block:: python

    import CETEMPublico

    CETEMPublico.download() # downloads small 10KB file
    # or
    CETEMPublico.download(full=True) # downloads full 12GB file

    cp = CETEMPublico.load()

    print(cp.tagged_sents())


