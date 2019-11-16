cetem-publico
=============

``cetem-publico`` is a Python wrapper for the CETEMPublico corpus. It
takes care of downloading, storing and importing the corpus into NLTK.

**THIS IS STILL A WORK IN PROGRESS, API MIGHT BREAK WITHOUT WARNING.**

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


Acknowledgements
----------------

This module only exists thanks to the `Publico <https://www.publico.pt>`_ newspaper and the team responsible for the `CETEMPublico <https://www.linguateca.pt/CETEMPublico/>`_ corpus.

Bugs and stuff
--------------

Open a `GitHub issue <https://github.com/andrefs/cetem_publico/issues>`_ or, preferably, send me a pull request.

License
-------

MIT

