====================
Formal Documentation
====================

:Version: |version|
:Release: |release|
:Date: |today|


.. _documentation-index:

About
=====

.. toctree::
    :maxdepth: 1

    about/formal

User's Manual
=============

.. toctree::
    :maxdepth: 1
    :glob:

    manual/*

Developer Documentation
=======================


.. toctree::
    :maxdepth: 1

    dev/index
    #dev/man/index
    #dev/api/index
    changes
    roadmap
    contributors

.. toctree::
    :hidden:

    glossary

.. ifconfig:: devel

   .. toctree::
    :hidden:

    todo
    readme

Indices and tables
==================

* :ref:`Index <genindex>`
* :ref:`modindex`
* :ref:`search`
* :doc:`glossary`
* :doc:`changes`

.. ifconfig:: devel

   * :doc:`todo`
   * :doc:`readme`
