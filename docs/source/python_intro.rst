

Introduction to Python Programming
======================================================================

.. todo::

   The current contents are perhaps a bit too basic and covered by
   numerous other resources. Instead, the lesson should focus on
   installation of requirements, ecosystem (pip, virtualenv) usage,
   and demonstrate a simple visualization with Pandas/Matplotlib.

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

.. include:: /python_intro/resources.rst

Acknowledgments
----------------------------------------------------------------------

Portions of this lesson have been adapted from the `official Python
Tutorial`_ copyright `Python Software Foundation`_.

.. _official Python Tutorial: https://docs.python.org/2/tutorial/
.. _Python Software Foundation: http://www.python.org/

Introduction
----------------------------------------------------------------------

.. include:: /python_intro/introduction.rst

Using Python on FutureSystems
----------------------------------------------------------------------

.. include:: /python_intro/on-futuresystems.rst

Interactive Python
----------------------------------------------------------------------

.. include:: /python_intro/interactive.rst


Syntax
----------------------------------------------------------------------

.. include:: /python_intro/syntax.rst


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

.. todo:: describe
  

Libraries
----------

Scipy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* https://www.scipy.org/

According to the SciPy Web page, "SciPy (pronounced “Sigh Pie”) is a Python-based ecosystem of
open-source software for mathematics, science, and engineering. In
particular, these are some of the core packages:

* NumPy
* IPython
* Pandas
* Matplotlib
* Sympy
* SciPy library

It is thus an agglomeration of useful pacakes and will prbably sufice
for your projects in case you use Python.

MatplotLib
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* http://matplotlib.org/

According the the Matplotlib Web page, "matplotlib is a python 2D
plotting library which produces publication quality figures in a
variety of hardcopy formats and interactive environments across
platforms. matplotlib can be used in python scripts, the python and
ipython shell (ala MATLAB®* or Mathematica®†), web application
servers, and six graphical user interface toolkits."

Matplotlib is a very easy to use graphics library which you can use to
visuzlize elementary charts for your projects.

Pandas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* http://pandas.pydata.org/

According to the Pandas Web page, "Pandas is a library library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language."

In addition to access to charts via matplotlib it has elementary
functionality for conduction data analysis. Pandas may be very
suitable for your projects.

Tutorial: http://pandas.pydata.org/pandas-docs/stable/10min.html


Numpy
----------------------------------------------------------------------

* http://www.numpy.org/

According to the Numpy Web page "NumPy is a package for scientific
computing with Python. It contains a powerful N-dimensional array
object, sophisticated (broadcasting) functions, tools for integrating
C/C++ and Fortran code, useful linear algebra, Fourier transform, and
random number capabilities

Tutorial: https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
