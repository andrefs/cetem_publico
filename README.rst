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

    cp = CETEMPublico.load() # loads a small 10KB sample
    # or
    cp = CETEMPublico.load(full=True) # loads the full 12GB

    print(cp.tagged_sents())


