Print Statements and Strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let us explore the syntax of Python.
Type into the interactive loop and press Enter::

  print "Hello world from Python!"

The output will look like this::

  >>> print "Hello world from Python!"
  Hello world from Python!

What happened: the ``print`` **statement** was given a **string** to
process.  A **statement** in Python, like ``print`` tells the
interpreter to do some primitive operation. In this case, ``print``
mean: write the following message to the standard output.

.. tip::

   Standard output is discussed in the
   :doc:`/class/lesson/linux/shell` lesson.

The "thing" we are ``print``ing in the case the the **string**
``Hello world from Python!``.  A **string** is a sequence of characters.  A
**character** can be a alphabetic (A through Z, lower and upper case),
numeric (any of the digits), white space (spaces, tabs, newlines,
etc), syntactic directives (comma, colon, quotation, exclamation,
etc), and so forth.  A string is just a sequence of the character and
typically indicated by surrounding the characters in double quotes.

So, what happened when you pressed Enter?  The interactive Python
program read the line ``print "Hello world from Python!"``, split it into
the ``print`` statement and the ``"Hello world from Python!"`` string, and
then executed the line, showing you the output.

Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can store data into a **variable** to access it later.
For instance, instead of:

.. code:: python

   >>> print "Hello world from Python!"

which is a lot to type if you need to do it multiple times, you can
store the string in a variable for convenient access:

.. code:: python

   >>> hello = "Hello world from Python!"
   >>> print hello
   Hello world from Python!

Booleans
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A **boolean** is a value that indicates the "truthness" of something.
You can think of it as a toggle: either "on" or "off", "one" or "zero", "true" or "false".
In fact, the only possible values of the **boolean** (or ``bool``) type in Python are:

- ``True``
- ``False``

You can combine booleans with **boolean operators**:

- ``and``
- ``or``

.. code:: python

   >>> print True and True
   True
   >>> print True and False
   False
   >>> print False and False
   False
   >>> print True or True
   True
   >>> print True or False
   True
   >>> print False or False
   False
   


Numbers and Math
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The interactive interpreter can also be used as a calculator.
For instance, say we wanted to compute a multiple of 21:

.. code:: python

   >>> print 21 * 2
   42

We saw here the ``print`` statement again. We passed in the result of
the operation ``21 * 2``.  An **integer** (or **int**) in Python is a numeric value
without a fractional component (those are called **floating point**
numbers, or **float** for short).

The mathematical operators compute the related mathematical operation
to the provided numbers.  Some operators are:

- ``*`` --- multiplication
- ``/`` --- division
- ``+`` --- addition
- ``-`` --- subtraction
- ``**`` --- exponent

Exponentiation is read as ``x**y`` is ``x`` to the ``y``\th power:

.. math::

   x^y

You can combine **float**\s and **int**\s:

.. code:: python

   >>> print 3.14 * 42 / 11 + 4 - 2
   13.9890909091
   >>> print 2**3
   8



Note that **operator precedence** is important.  Using parenthesis to
indicate affect the order of operations gives a difference results, as
expected:

.. code:: python

   >>> print 3.14 * (42 / 11) + 4 - 2
   11.42
   >>> print 1 + 2 * 3 - 4 / 5.0
   6.2
   >>> print (1 + 2) * (3 - 4) / 5.0
   -0.6

Types and Using the REPL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have so far seen a few examples of types: **string**\s, **bool**\s,
**int**\s, and **float**\s.  A **type** indicates that values of that
type support a certain set of operations. For instance, how would you
exponentiate a string? If you ask the interpreter, this results in an
error:

.. code:: python

   >>> "hello"**3
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

There are many different types beyond what we have seen so far, such as **dictionaries**\s, **list**\s, **set**\s. One handy way of using the interactive python is to get the type of a value using ``type()``:

.. code:: python

   >>> type(42)
   <type 'int'>
   >>> type(hello)
   <type 'str'>
   >>> type(3.14)
   <type 'float'>

You can also ask for help about something using ``help()``:

.. code:: python

   >>> help(int)
   >>> help(list)
   >>> help(str)

.. tip::

   Using ``help()`` opens up a pager. To navigate you can use the
   spacebar to go down a page ``w`` to go up a page, the arrow keys to
   go up/down line-by-line, or ``q`` to exit.


Further Learning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /class/lesson/linux/python/further-learning.rst
