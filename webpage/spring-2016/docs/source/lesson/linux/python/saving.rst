You can save your programs to files which the interpreter can then
execute.
This has the benefit of allowing you to track changes made to your programs and sharing them with other people.

Start by opening a new file ``hello.py``::

  $ nano hello.py

Now enter write a simple program and save::

  print "Hello world!"

As a check, make sure the file contains the expected contents::

  $ cat hello.py
  print "Hello world!"

To execute your program pass the file as a parameter to the ``python``
command::

  $ python hello.py
  Hello world!


Congratulations, you have written a Python **module**.
Files in which Python directives are stored are called **module**\s

You can make this programs more interesting as well.  Let's write a
program that asks the user to enter a number, *n*, and prints out the
*n*\-th number in the `Fibonacci sequence`_::

   $ nano print_fibs.py

.. include:: /class/lesson/linux/python/print_fibs.py
   :code: python

We can now run this like so::

  $ python print_fibs.py 5
  8

Let break this down a bit.
The first part::

  python print_fibs.py 5

can be translated to say:

  The Python interpreter ``python`` should run the ``print_fibs.py``
  program and pass it the parameter ``5``.

The interpreter then looks at the ``print_fibs.py`` file and begins to
execute it.
The first line it encounters is:

.. code:: python

   import sys

This line consists of the ``import`` keyword.
Here ``import`` attempts to load the ``sys`` module, which has several useful items.

Next the interpreter sees the ``def`` keyword.  The begins the
definition of a function, called ``fib`` here.  Our ``fib`` function
takes a single argument, named ``n`` within the function definition.

Next we begin a multi-line string between the triple double-quotes.
Python can take this string and create documentation from it.

The ``fib`` function returns the *n*\-th number in the `Fibonacci sequence`_.
This sequence is mathematically defined as (where *n* is subscripted):

.. math::

   F_0 &= 0 \\
   F_1 &= 1 \\
   F_n &= F_{n-1} + F_{n-2}

This translates to Python as:

.. code:: python

   if n == 0:
     return 0
   elif n == 1:
     return 1
   else:
     return fib(n-1) + fib(n-2)


Next we have the block:

.. code:: python

   if __name__ == '__main__':


If the interpreter is running this module then there will be a variable ``__name__`` whose value is ``__main__``.
This **if statement** checks for this condition and executes this block if the check passed.

.. tip::

   Try removing the ``if __name__ == '__main__'`` block and run the
   program.
   How does it behave differently?
   What about if you replace with something like:

   .. code:: python

      print fib(5)
      print fib(10)


The next line:

.. code:: python

   n = int(sys.argv[1])

does three different things.
First it gets the value in the ``sys.argv`` array at index 1.
This was the parameter `5` we originally passed to our program::

  $ python print_fibs.py 5

Substituting the parameter in, the line can be rewritten as:

.. code:: python

   n = int("5")

We see that the ``5`` is represented as a string.
However, we need to use integers for the ``fib`` function.
We can use ``int`` to convert ``"5"`` to ``5``

We now have:

.. code:: python

   n = 5

which assigns the value ``5`` to the variable ``n``.
We can now call ``fib(n)`` and ``print`` the result.

.. _Fibonacci sequence: http://en.wikipedia.org/wiki/Fibonacci_number
