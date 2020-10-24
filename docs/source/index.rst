.. strup documentation master file, created by
   sphinx-quickstart on Sat Oct 10 22:20:41 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :hidden:
   :maxdepth: 2

   self
   api.rst

:mod:`strup` --- string unpack
====================================

.. .. image:: https://travis-ci.org/readthedocs/sphinx_rtd_theme.svg?branch=master
   :target: https://travis-ci.org/readthedocs/sphinx_rtd_theme
   :alt:  Build Status
   .. image:: https://readthedocs.org/projects/sphinx-rtd-theme/badge/?version=latest
   :target: http://sphinx-rtd-theme.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
   .. image:: https://img.shields.io/pypi/l/sphinx_rtd_theme.svg
   :target: https://pypi.python.org/pypi/sphinx_rtd_theme/
   :alt: License

This Python package is for unpacking basic objects from a text string.
The standard data types :attr:`string`, :attr:`int`, :attr:`float` and :attr:`bool` are supported.


The function :func:`unpack`
===========================

We may extract the objects from a text string :attr:`text` using the utility
function :py:mod:`unpack(fmt, text)`.
Each format character in the string :attr:`fmt` indicates the data type for the corresponding object.

.. code-block:: python

  >>> from strup import unpack
  >>> i, x, s, ok = unpack("ifs?", "5 2.3   ole  True")
  >>> i, x, s, ok
  (5, 2.3, 'ole', True)

The format characters for the data types are consistent with the syntax applied in the standard library module
`struct <https://docs.python.org/3/library/struct.html>`_ for handling of binary data.
Characters in :attr:`fmt` are case sensitive.

+-----------+-----------------------+
| Character | Data Object           |
+===========+=======================+
|     i     |    int                |
+-----------+-----------------------+
|     f     |    float              |
+-----------+-----------------------+
|     s     |    string             |
+-----------+-----------------------+
|     ?     |    bool               |
+-----------+-----------------------+
|     .     |    ignore this item   |
+-----------+-----------------------+

Each eventual dot inside :attr:`fmt` indicates that the corresponding item should not be part of the result.

.. code-block:: python

  >>> unpack("f..s", "2.3 ole 55   dole")
  (2.3, 'dole')

In case of bool objects, the actual item of :attr:`text` must follow the convention applied in
`distutils.util.strtobool <https://docs.python.org/3/distutils/apiref.html#distutils.util.strtobool>`_.
Consequently, `y`, `yes`, `t`, `true`, `on` and `1` are interpreted as `True` and
`n`, `no`, `f`, `false`, `off` and `0` as `False`. For all other values
a :exc:`ValueError` exception is raised.

.. code-block:: python

   >>> strup.unpack("?????s????", "NO 0 F off False ---  yes 1 ON TruE")
   (False, False, False, False, False, '---', True, True, True, True)

The set of items to consider from the string :attr:`text`, is by default
the items returned from the standard library :meth:`text.split()` method.

Only the :attr:`len(fmt)` first items of :meth:`text.split()` are considered. Trailing dots
are not needed in :attr:`fmt` and should not be specified.


Optional Parameters
===================

The optional argument :attr:`sep` as defined in the standard Python :meth:`string.split()` is
also applicable in this context.

.. code-block:: python

  >>> unpack("f..s", " 2.3 ,ole,55,   dole", sep=',')
  (2.3, '   dole')

By specifying the optional parameter :attr:`none=True`, zero-sized string items in :attr:`text`
are interpreted as :attr:`None` independent of the format character. By default :attr:`none=False`.

.. code-block:: python

  >>> unpack("fissi", "2.3,,, ,12", sep=',', none=True)
  (2.3, None, None, ' ', 12)

String objects are often defined using quotes. The optional argument :attr:`quote` has default value
:attr:`None` but may be :attr:`"` or :attr:`'`.

  >>> unpack("isf", "100 'Donald Duck' 125.6", quote="'")
  (100, 'Donald Duck', 125.6)

Eventual quotes inside quoted strings are controlled using the optional argument :attr:`quote_escape`.
By default :attr:`quote_escape=None` means that internal quotes are identified in  :attr:`text`
using double quotes

  >>> unpack("isf", "100 'She''s the best' 125.6", quote="'")
  (100, "She's the best", 125.6)
  >>> unpack("isf", '3 "A ""quote"" test"  93.4 ignored', quote='"')
  (3, 'A "quote" test', 93.4)

However, other escape sequences are supported like :attr:`quote_escape=r"\\'"` or :attr:`quote_escape=r'\\"'`

  >>> unpack("isf", r"100 'She\'s the best' 125.6", quote="'", quote_escape=r"\'")
  (100, "She's the best", 125.6)


The class :class:`Unpack`
=========================

All processing within the function :meth:`unpack()`, as described above, is handled by the class
:class:`Unpack`.

.. code-block:: python

   >>> from strup import Unpack

All arguments for the function :meth:`unpack()`, except :attr:`text`, are handled by the constructor of :class:`Unpack`.
This constructor also performs preprocessing. Finally, :meth:`Unpack.__call__` process the actual :attr:`text`.

Consequently, when the same unpack pattern is applied in loops, we may benefit from utilizing :class:`Unpack` directly.

.. code-block:: python

   >>> mydecode = Unpack('.s..f', quote='"')     # Preprocess the pattern
   >>> for line in ['5.3 "Donald Duck" 2 yes 5.4',
                    '-2.2 "Uncle Sam" 4  no 1.5',
                    '3.3  "Clint Eastwood" 7 yes 6.5']:
   ...      mydecode(line)
   ("Donald Duck", 5.4)
   ("Uncle Sam", 1.5)
   ("Clint Eastwood", 6.5)


Exception Handling
==================

==========================  =======================================
Exceptions                  Description
==========================  =======================================
:exc:`ValueError`           Input error with relevant error message
==========================  =======================================

.. code-block:: bash

   >>> w1, w2, ival, w3 = unpack("ssis", "you,need,some,help", sep=",")
   Traceback (most recent call last):
      File "e:\repositories\github\jeblohe\strup\strup\unpack.py", line 85, in unpack
      raise ValueError(msg)
   ValueError: strup.unpack()
   fmt='ssis'
   text='you,need,some,help'
   argv=(), kwargs={'sep': ','}
   Error decoding element 2:'some' of items=['you', 'need', 'some', 'help']


API
===

Docstrings from the source code are provided :doc:`here <api>`.


Considerations
==============

A major goal with :attr:`strup` is to provide a clean and intuitive interface.
If standard `string methods <https://docs.python.org/3/library/stdtypes.html#string-methods>`_
are too low level and the `re-module <https://docs.python.org/3/library/re.html>`_
adds too much complexity, then :attr:`strup` might be your compromise.

Backward compatibility of the API is strongly emphasized.

:attr:`strup` will not grow into a general purpose parser.
Text processing is in general a comprehensive topic.
For high volume text processing it is recommended to apply optimized packages like
`numpy <http://numpy.org>`_ and `pandas <https://pandas.pydata.org/>`_.


Installation
============

This package is platform independent and available from PyPI and Anaconda.

To install :attr:`strup` from PyPI:

.. code-block:: bash

   pip install strup           # For end users
   pip install -e .[dev]       # For package development (from the root of your strup repo)


or from Anaconda:

.. code-block:: bash

   conda install -c jeblohe strup

The source code is hosted on GitHub. Continuous integration at CircleCI.
The code is extensively tested on Python 2.7, 3,4, 3.5, 3.6, 3.7, 3.8 and 3.9.
The test coverage is reported by Coveralls.

License
=======

This software is licensed under the MIT-license.


Version
=======

1.0.0 - 2020.10.24
------------------

First official release
