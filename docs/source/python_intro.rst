

Introduction to Python Programming
======================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:


Installation
----------------------------------------------------------------------

We assume that you have a computer with python installed. We will be
using Python 2.7.10 but not Python 3

Instalation instructions are provided at the python.org web
pages. However, we recommend that you use pythons virtualenv to
isolate your development python from the system installed python.

This lesson will introduce you to programming in Python.

.. note:: Duration: 1 hour

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should

* A computer with python 2.7.x
* Familiarity with commandline usage
* A text editor such as PyCharm, emacs, vi or others. You should
  identity which works best for you and set it up.
* We do not recommend anaconda, or canopy as we ran into issues once
  you do some more advanced python. Instead we recommend you use pip
  and virtualenv. If you are unfamiliar with these tools, please
  consult the manual and tutorials available for it on the internet.

Dependencies
----------------------------------------------------------------------

  - `Python <https://www.python.org/>`_ 
  - `Pip <https://pip.pypa.io/en/stable/>`_
  - `Virtualenv <https://virtualenv.pypa.io/en/stable/>`_
  - `NumPy <http://www.numpy.org/>`_
  - `SciPy <https://scipy.org/>`_
  - `Matplotlib <http://matplotlib.org/>`_
  - `Pandas <http://pandas.pydata.org/>`_


Learning Goals
----------------------------------------------------------------------

At the end of this lesson you will be able to:

- use Python 
- use the interactive Python interface
- understand the basic syntax of Python
- write and run Python programs stored in a file
- have an overview of the standard library
- install Python libraries using ``virtualenv``


.. _python-resources:

Resources
----------------------------------------------------------------------
If you are unfamilliar with programming in Python, we also refer you
to some of the numerous online resources. You may wish to start with
`Learn Python`_ or the book `Learn Python the Hard Way`_. Other
options include `Tutorials Point`_ or `Code Academy`_, and the Python wiki page
contains a long list of `references for learning`_ as well.
Additional resources include:

- http://ivory.idyll.org/articles/advanced-swc/
- http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
- http://www.youtube.com/watch?v=0vJJlVBVTFg
- http://www.korokithakis.net/tutorials/python/
- http://www.afterhoursprogramming.com/tutorial/Python/Introduction/


.. _Code Academy: http://www.codecademy.com/en/tracks/python
.. _Python documentation site: https://docs.python.org/2.7/
.. _list of introductory books: https://wiki.python.org/moin/IntroductoryBooks
.. _Python Module index: https://docs.python.org/2/py-modindex.html
.. _StackOverflow python tags: http://stackoverflow.com/questions/tagged/python
.. _searching Google: https://www.google.com/?gws_rd=ssl#q=python+how+to
.. _PyCharm IDE: https://www.jetbrains.com/pycharm/
.. _Learn Python the Hard Way: http://learnpythonthehardway.org/book/
.. _Tutorials Point: http://www.tutorialspoint.com/python/
.. _references for learning: https://wiki.python.org/moin/BeginnersGuide/Programmers
.. _Learn Python: https://www.learnpython.org

Acknowledgments
----------------------------------------------------------------------

Portions of this lesson have been adapted from the `official Python
Tutorial`_ copyright `Python Software Foundation`_.

.. _official Python Tutorial: https://docs.python.org/2/tutorial/
.. _Python Software Foundation: http://www.python.org/

Introduction
----------------------------------------------------------------------
Python is an easy to learn, powerful programming language. It has
efficient high-level data structures and a simple but effective
approach to object-oriented programming. Python’s elegant syntax and
dynamic typing, together with its interpreted nature, make it an ideal
language for scripting and rapid application development in many areas
on most platforms.

The Python interpreter and the extensive standard library are freely
available in source or binary form for all major platforms from the
Python Web site, https://www.python.org/, and may be freely
distributed. The same site also contains distributions of and pointers
to many free third party Python modules, programs and tools, and
additional documentation.

The Python interpreter is easily extended with new functions and data
types implemented in C or C++ (or other languages callable from
C). Python is also suitable as an extension language for customizable
applications.

This tutorial introduces the reader informally to the basic concepts
and features of the Python language and system. It helps to have a
Python interpreter handy for hands-on experience, but all examples are
self-contained, so the tutorial can be read off-line as well.

This tutorial does not attempt to be comprehensive and cover every
single feature, or even every commonly used feature. Instead, it
introduces many of Python's most noteworthy features, and will give
you a good idea of the language's flavor and style. After reading it,
you will be able to read and write Python modules and programs, and
you will be ready to learn more about the various Python library
modules.


Using Python on FutureSystems
----------------------------------------------------------------------
In order to use Python you must log into your FutureSystems account.
Then at the shell prompt execute the following command::

  $ module load python

This will make the ``python`` and ``virtualenv`` commands available to
you.


.. tip::

   The details of what the ``module load`` command does are described
   in the future lesson :doc:`modules`.

Interactive Python
----------------------------------------------------------------------

tart by entering the interactive loop by executing the command::

  $ python

You should see something like the following::

  Python 2.7 (r27:82500, Aug 10 2010, 11:35:15)
  [GCC 4.1.2 20080704 (Red Hat 4.1.2-48)] on linux2
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

The ``>>>`` is the prompt for the interpreter.
This is similar to the shell interpreter you have been using.


.. tip::

   Often we show the prompt when illustrating an example. This is to
   provide some context for what we are doing. If you are following
   along you will not need to type in the prompt.


This interactive prompt does the following:

- *read* your input commands
- *evaluate* your command
- *print* the result of evaluation
- *loop* back to the beginning.

This is why you may see the interactive loop referred to as a
**REPL**: **R**\ead-**E**\valuate-**P**\rint-**L**\oop.

Syntax
----------------------------------------------------------------------

tatements and Strings
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




Writing and Saving Programs
----------------------------------------------------------------------

Make sure you are no longer in the interactive interpreter.
If you are you can type ``quit()`` and press Enter to exit.

.. include:: /python_intro/saving.rst

Installing Libraries
----------------------------------------------------------------------

.. include:: /python_intro/pip-install.rst

Further Learning
----------------------------------------------------------------------

.. include:: /python_intro/further-learning.rst

  
Exercises
----------------------------------------------------------------------

.. _lab-python-1:

Lab - Python - FizzBuzz
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Write a python program called fizzbuzz.py that accepts an integer n
from the command line.  Pass this integer to a function called
fizzbuzz.

The fizzbuzz function should then iterate from 1 to n.  If the ith
number is a multiple of three, print "fizz", if a multiple of 5 print
"buzz", if a multiple of both print "fizzbuzz", else print the value.


.. _lab-python-2:

Lab - Python - Setup for FutureSystems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Create a virtualenv ``~/ENV``
#. Modify your ``~/.bashrc`` shell file to activate your environment
   upon login.
#. Install the ``docopt`` python package using ``pip``
#. Write a program that uses ``docopt`` to define a commandline
   program. Hint: modify the FizzBuzz program.
#. Demonstrate the program works and submit the code and output.


OTHER TEXT 
======================================================================


Variables, Expressions, and Statements
----------------------------------------------------------------------

Variables in Python can hold text and numbers. For example:

.. code:: python

    x = 7
    price = 7.5
    word = 'Hello World'

Variable names on the left and the values are on the right. Once a
variable is assigned, it can be used in other places of the program.
In the example above, we have three variables: x, price and
word. Variables may not contain spaces or special characters.  Text
variables may be defined in 3 ways:

.. code:: python
    
    word = 'Hello World'
    word = "Hello World"
    word = '''Hello World'''


The type depends on what you prefer.  Once defined variables can be
replaced or modified:

.. code:: python

    x = 2

    # increase x by one
    x = x + 1

    # replace x
    x = 5

Python supports the operators +, -, / and * as well as brackets.
Variables may be shown on the screen using the print statement.

.. code:: python

    x = 5
    print(x)

    y = 3 * x
    print(y)

    # more detailed output
    print("x = " + str(x))
    print("y = " + str(y))

The first output of the program above is simply the raw value of the
variables. If you want to print a more detailed message like “x = 5”,
use the line ‘print(“x = ” + str(x))’. This str() function converts
the numeric variable to text.


Control Statements
----------------------------------------------------------------------

Computer programs do not only execute instructions. Occasionally, a
choice needs to be made. Such as a choice is based on a
condition. Python has several conditional operators:


.. code:: python

    >   greater than
    <   smaller than
    ==  equals
    !=  is not

Conditions are always combined with variables. A program can make a
choice using the if keyword. For example:

.. code:: python
    
    x = int(input("Tell X"))
    if x == 4:
        print('You guessed correctly!')
    print('End of program.')


When you execute this program it will always print ‘End of program’,
but the text ‘You guessed correctly!’ will only be printed if the
variable x equals to four (see table above). Python can also execute a
block of code if x does not equal to 4. The else keyword is used for
that.


.. code:: python

    x = int(input("What is the value of  X"))

    if x == 4:
        print('You guessed correctly!')
    else:
        print('Wrong guess')

    print('End of program.')


Iterations
----------------------------------------------------------------------

To repeat code, the for keyword can be used. To execute a line of code
10 times we can do:

.. code:: python

    for i in range(1,11):
        print(i)

The last number (11) is not included. This will output the numbers 1
to 10. Python itself starts counting from 0, so this code will also
work:

.. code:: python
    
    for i in range(0,10):
        print(i)

but will output 0 to 9.


The code is repeated while the condition is True. In this case the
condition is: i < 10. Every iteration (round), the variable i is
updated.Nested loops Loops can be combined:

.. code:: python
    
    for i in range(0,10):
        for j in range(0,10):
            print(i,' ',j)

In this case we have a multidimensional loops. It will iterate over
the entire coordinate range (0,0) to (9,9)


Functions
----------------------------------------------------------------------


To repeat lines of code, you can use a function. A function has a
unique distinct name in the program. Once you call a function it will
execute one or more lines of codes, which we will call a code block.

.. code:: python
	  
    import math

    def computePower(a):
        value = math.pow(a,2)
        print(value)

    computePower(3)


We call the function with parameter a = 3 .  A function can be called
several times with varying parameters. There is no limit to the number
of function calls.

The def keyword tells Python we define a function.  Always use four
spaces to indent the code block, using another number of spaces will
throw a syntax error.

It is also possible to store the output of a function in a variable.
To do so, we use the keyword return.

.. code:: python

    import math

    def computePower(a):
        value = math.pow(a,2)
        return value

    result = computePower(3)
    print(result)


Strings
----------------------------------------------------------------------


Modules
----------------------------------------------------------------------
Modules are are a great way to import 


Ecosystem
----------------------------------------------------------------------

virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often you have your own computer and you do not like to change its
environment to keep it in prestine condition. Python comes with mnay
libraries that could for example conflict with libraries that you have
installed. To avoid this it is bets to work in an isolated python
environment while using virtualenv,. Documentation about it can be
found at::

* http://virtualenv.readthedocs.org/

The installation is simple once you have pip installed. If it is not
installed you can say::

  $ easy_install pip

After that you can install the virtual env with::

  $ pip install virtualenv

To setup an isolated environment for example in the directory ~/ENV
please use::

  $ virtualenv ~/ENV

To activate it you can use the command::

  $ source ~/ENV/bin/activate

you can put this command n your bashrc or bash_profile command so you
do not forget to activate it.



pypi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Python Package Index is a large repository of software for the
Python programming language containing a large number of packages
[link]. The nice think about pipy is that many packages can be
installed with the program 'pip'.

To do so you have to locate the <package_name> for example with the
search function in pypi and say on the commandline::

    pip install <package_name>

where pagage_name is the string name of the package. an example would
be the package called fabric which you can install with::

   pip install fabric
 
If all goes well the package will be installed.


github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Github is a code repository that allows the development of code in a
distributed fashion. There are many good tutorials about github.

Some of them can be found on the github Web page. An interactive
tutorial is for example available at

* https://try.github.io/

A more extensive list of tutorials can be found at 

*
https://help.github.com/articles/what-are-other-good-resources-for-learning-git-and-github

Important is that you always want to make sure that you want to use
the git init command and add your Name and e-mail. Do it consistent in
the machines you use, or your checkins in git (if you do them) do not
show up in a consistant fashion as a single user. This is done with
the following commands::

  $ git config --global user.name "John Doe"
  $ git config --global user.email johndoe@example.com

You can set also the editor with::

  $ git config --global core.editor emacs

More information about a first time setup is documented at::

  $ http://git-scm.com/book/en/Getting-Started-First-Time-Git-Setup

To check your setup you can say::

  $ git config --list

gitlab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gitlab provides a Git repository management with code reviews, issue
tracking, activity feeds and wikis. It comes with GitLab CI for
continuous integration and delivery. It supports public and private
repositories in the community addition and has fewer space
restrictions. Thus we are using gitlab for this projet. 

You can find a list of features at https://about.gitlab.com/features/

A comparision to the enterprise level is given here: https://about.gitlab.com/features/#compare

