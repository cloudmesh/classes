
.. _python_intro:

Introduction to Python
======================

.. sidebar:: Page Contents

   .. contents::
      :local:


Acknowledgments
----------------------------------------------------------------------

Portions of this lesson have been adapted from the `official Python
Tutorial`_ copyright `Python Software Foundation`_.

.. _official Python Tutorial: https://docs.python.org/2/tutorial/
.. _Python Software Foundation: http://www.python.org/

Description
-----------------------------------------------------------------

Python is an easy to learn programming language. It has efficient
high-level data structures and a simple but effective approach to
object-oriented programming. Python’s simple syntax and dynamic
typing, together with its interpreted nature, make it an ideal
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

Python is an interpreted, dynamic, high-level programming language
suitable for a wide range of applications. The `The Zen of Python`_
summarizes some of its philosophy including:

* Explicit is better than implicit
* Simple is better than complex
* Complex is better than complicated
* Readability counts

The main features of Python are:

* Use of indentation whitespace to indicate blocks
* Object orient paradigm
* Dynamic typing
* Interpreted runtime
* Garbage collected memory management
* a large standard library
* a large repository of third-party libraries

Python is used by many companies (such as Google, Yahoo!, CERN, NASA)
and is applied for web development, scientific computing, embedded
applications, artificial intelligence, software development, and
information security, to name a few.

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



.. _The Zen of Python: https://www.python.org/dev/peps/pep-0020/


Installation
----------------------------------------------------------------------

Python is easy to install and very good instructions for most
platforms can be found on the python.org Web page. We will be
using Python 2.7.12 but not Python 3.

We assume that you have a computer with python installed.
However, we recommend that you use pythons virtualenv to
isolate your development python from the system installed python.

.. note:: If you are not familiar with virtualenv, please read up on
	  it.

Alternative Installations
-------------------------

The best installation of python is provided by python.og. However
others claim to have alternative environments that allow you to
install python. This includes

* `Canopy <https://store.enthought.com/downloads/#default>`_
* `Anaconda <https://www.continuum.io/downloads>`_
* `IronPython <http://ironpython.net/>`_

Typically they include not only the python compiler but also several
useful packages. It is fine to use such environments for the class,
but it should be noted that in both cases not every python library may
be available for install in the given environment. For example if you
need to use cloudmesh client, it may not be available as conda or
Canopy package. This is also the case for many other cloud related and
useful python libraries. Hence, we do recommend that if you are new to
python to use the distribution form python.org, and use pip and
virtualenv.

Additionally some python version have platform specific libraries or
dependencies. For example coca libraries, .NET or other frameworks are
examples. For the assignments and the projects such platform dependent
libraries are not to be used.

If however you can write a platform independent code that works on
Linux, OSX and Windows while using the python.org version but develop
it with any of the other tools that is just fine. However it is up to
you to guarantee that this independence is maintained and
implemented. You do have to write requirements.txt files that will
install the necessary python libraries in a platform independent
fashion. The homework assignment PRG1 has even a requirement to do so.

In order to provide platform independence we have given in the class a
"minimal" python version that we have tested with hundreds of
students: python.org. If you use any other version, that is your
decision. Additionally some students not only use python.org but have
used iPython which is fine too. However this class is not only about
python, but also about how to have your code run on any platform. The
homework is designed so that you can identify a setup that works for
you.

However we have concerns if you for example wanted to use chameleon
cloud which we require you to access with cloudmesh. cloudmesh is not
available as conda, canopy, or other framework package. Cloudmesh
client is available form pypi which is standard and should be
supported by the frameworks. We have not tested cloudmesh on any other
python version then python.org which is the open source community
standard. None of the other versions are standard.

In fact we had students over the summer using canopy on their machines
and they got confused as they now had multiple python versions and did
not know how to switch between them and activate the correct
version. Certainly if you know how to do that, than feel free to use
canopy, and if you want to use canopy all this is up to you. However
the homework and project requires you to make your program portable to
python.org. If you know how to do that even if you use canopy,
anaconda, or any other python version that is fine. Graders will test
your programs on a python.org installation and not canpoy, anaconda,
ironpython while using virtualenv. It is obvious why. If you do not
know that answer you may want to think about that every time they test
a program they need to do a new virtualenv and run vanilla python in
it. If we were to run two instals in the same system, this will not
work as we do not know if one student will cause a side effect for
another. Thus we as instructors do not just have to look at your code
but code of hundreds of students with different setups. This is a non
scalable solution as every time we test out code from a student we
would have to wipe out the OS, install it new, install an new version
of whatever python you have elected, become familiar with that version
and so on and on. This is the reason why the open source community is
using python.org. We follow best practices. Using other versions is
not a community best practice, but may work for an individual.

We have however in regards to using other python version additional
bonus projects such as


* deploy run and document cloudmesh on ironpython
* deploy run and document cloudmesh on anaconde, develop script to
  generate a conda packge form github
* deploy run and document cloudmesh on canopy, develop script to
  generate a conda packge form github
* deploy run and document cloudmesh on ironpython
* other documentation that would be useful



Resources
----------------------------------------------------------------------
If you are unfamiliar with programming in Python, we also refer you
to some of the numerous online resources. You may wish to start with
`Learn Python`_ or the book `Learn Python the Hard Way`_. Other
options include `Tutorials Point`_ or `Code Academy`_, and the Python wiki page
contains a long list of `references for learning`_ as well.
Additional resources include:

* http://ivory.idyll.org/articles/advanced-swc/
* http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
* http://www.youtube.com/watch?v=0vJJlVBVTFg
* http://www.korokithakis.net/tutorials/python/
* http://www.afterhoursprogramming.com/tutorial/Python/Introduction/
* http://www.greenteapress.com/thinkpython/thinkCSpy.pdf


A very long list of useful information are also available from

* https://github.com/vinta/awesome-python
* https://github.com/rasbt/python_reference

This list may be useful as it also contains links to data
visualization and manipulation libraries, and AI tools and libraries.
Please note that for this class you can reuse such libraries if not
otherwise stated.

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

* `Python <https://www.python.org/>`_
* `Pip <https://pip.pypa.io/en/stable/>`_
* `Virtualenv <https://virtualenv.pypa.io/en/stable/>`_
* `NumPy <http://www.numpy.org/>`_
* `SciPy <https://scipy.org/>`_
* `Matplotlib <http://matplotlib.org/>`_
* `Pandas <http://pandas.pydata.org/>`_


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


Using Python on FutureSystems
----------------------------------------------------------------------

.. warning:: This is only important if you use Futuresystems resources.

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

Python can be used interactively.  Start by entering the interactive
loop by executing the command::

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

Statements and Strings
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




Control Statements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


.. _doc_python_intro_sec_classes:

Classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A class is a way to take a grouping of functions and data and place them inside a container, so you can access them with the . (dot) operator.

.. code:: python

        class Fruit(object):

        def __init__(self):
            self.tangerine = "are organge-colored citrus fruit, which is closely related to a mandarin organge"

        def apple(self):
            print "Apples are rich in antioxidants, flavanoids, and dietary fiber!"

    thing = Fruit()
    thing.apple()
    print thing.tangerine

Writing and Saving Programs
----------------------------------------------------------------------

Make sure you are no longer in the interactive interpreter.
If you are you can type ``quit()`` and press Enter to exit.

You can save your programs to files which the interpreter can then
execute.  This has the benefit of allowing you to track changes made
to your programs and sharing them with other people.

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

   $ emacs print_fibs.py

::

    import sys

    def fib(n):
	"""
	Return the nth fibonacci number

	The nth fibonacci number is defined as follows:
	Fn = Fn-1 + Fn-2
	F2 = 1
	F1 = 1
	F0 = 0
	"""

	if n == 0:
	    return 0
	elif n == 1:
	    return 1
	else:
	    return fib(n-1) + fib(n-2)


    if __name__ == '__main__':
	n = int(sys.argv[1])
	print fib(n)


We can now run this like so::

  $ python print_fibs.py 5
  5

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

Installing Libraries
----------------------------------------------------------------------

Often you may need functionality that is not present in Python's
standard library.  In this case you have two option:

- implement the features yourself
- use a third-party library that has the desired features.

Often you can find a previous implementation of what you need.
Since this is a common situation, there is a service supporting it:
the `Python Package Index`_ (or PyPi for short).


Our task here is to install the `autopep8`_ tool from PyPi.
This will allow us to illustrate the use if virtual environments using
the ``virtualenv`` command, and installing and uninstalling PyPi
packages using ``pip``.


Virtual Environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often when you use shared computing resources, such as
``india.futuresystems.org`` you will not have permission to install
applications in the default global location.

Let's see where ``grep`` is located::

  $ which grep
  /bin/grep

It seems that there are many programs installed in ``/bin`` such as
``mkdir`` and ``pwd``::

  $ ls /bin
  alsacard    dbus-cleanup-sockets  env             hostname         mailx          pwd
  alsaunmute  dbus-daemon           ex              igawk            mkdir          raw
  ...

If we wished to add a new program it seems like putting it in ``/bin`` is the place to start.
Let's create an empty file ``/bin/hello-$PORTALNAME``::

  $ touch /bin/hello-$(whoami)
  touch: cannot touch `/bin/hello-albert': Permission denied


.. tip::

   Recall that $PORTALNAME is your username on FutureSystems, which
   can also be obtained using the ``whoami`` shell command.  t seems
   that this is not possible.  Since ``india`` is a shared resources
   not all users should be allowed to make changes that could affect
   everyone else.  Only a small number of users, the administrators,
   have the ability to globally modify the system.

We can still create our program in our home directory::

  $ touch ~/hello-$(whoami)

but this becomes cumbersome very quickly if we have a large number of
programs to install.  Additionally, it is not a good idea to modify
the global environment of one's computing system as this can lead to
instability and bizarre errors.

A virtual environment is a way of encapsulating and automating the
creation and use of a computing environment that is consistent and
self-contained.

The tool we use with Python to accomplish this is called ``virtualenv``.

Let's try it out. Start by cleaning up our test earlier and going
into the home directory::

  $ rm ~/hello-$(whoami)
  $ cd ~


Now lets create a virtual env::

  $ virtualenv ENV
  PYTHONHOME is set.  You *must* activate the virtualenv before using it
  New python executable in ENV/bin/python
  Installing setuptools............done.
  Installing pip...............done.


When using ``virtualenv`` you pass the directory where you which to
create the virtual environment, in this case ``ENV`` in the current
(home) directory.  We are then told that we must activate the virtual
environment before using it and that the python program, setuptools,
and pip are installed.

Let's see what we have::

  $ ls ENV/bin
  activate  activate.csh  activate.fish  activate_this.py  easy_install
  easy_install-2.7  pip  pip-2.7  python  python2  python2.7

It seems that there are several programs installed.  Let's see where
our current ``python`` is and what happens after activating this
environment::
  $ which python
  /N/soft/python/2.7/bin/python
  $ source ENV/bin/activate
  (ENV) $ which python
  ~/ENV/bin/python

.. important::

   As virtualenv stated, you **must** activate the virtual environment
   before it can be used.

.. tip::

   Notice how the shell prompt changed upon activation.

Autoenv: Directory-based Environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a directory contains a ``.env`` file, it will automatically be executed
when you ``cd`` into it. It's easy to use and install.

This is great for...

   - auto-activating virtualenvs
   - project-specific environment variables


Here is how to use it. Add the ENV you created with virtualenv into ``.env`` file within your project directory::

   $ echo "source ~/ENV/bin/activate" > project.env
   $ echo "echo 'whoa'" > project/.env
   $ cd project
   whoa

Here is how to install.
Mac OS X Using Homebrew::

   $ brew install autoenv
   $ echo "source $(brew --prefix autoenv)/activate.sh" >> ~/.bash_profile


Using pip::

   $ pip install autoenv
   $ echo "source `which activate.sh`" >> ~/.bashrc


Using git::

   $ git clone git://github.com/kennethreitz/autoenv.git ~/.autoenv
   $ echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc


Before sourcing activate.sh, you can set the following variables:

   - ``AUTOENV_AUTH_FILE``: Authorized env files, defaults to ``~/.autoenv_authorized``
   - ``AUTOENV_ENV_FILENAME``: Name of the ``.env`` file, defaults to ``.env``
   - ``AUTOENV_LOWER_FIRST``: Set this variable to flip the order of ``.env`` files executed


Autoenv overrides ``cd``. If you already do this, invoke ``autoenv_init`` within your custom ``cd`` after sourcing ``activate.sh``.

Autoenv can be disabled via ``unset cd`` if you experience I/O issues with
   certain file systems, particularly those that are FUSE-based (such as
   ``smbnetfs``).

Fixing Bad Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's now look at another important tool for Python development: the
Python Package Index, or PyPI for short.  PyPI provides a large set of
third-party python packages.  If you want to do something in python,
first check pypi, as odd are someone already ran into the problem and
created a package solving it.

I'm going to demonstrate creating a user python environment,
installing a couple packages from pypi, and use them to examine some
code.

First, get the bad code like so::

   $ wget --no-check-certificate http://git.io/pXqb -O bad_code_example.py

Let's examine the code::

  $ nano bad_code_example.py

As you can see, this is very dense and hard to read.  Cleaning it up
by hand would be a time-consuming and error-prone process.  Luckily,
this is a common problem so there exist a couple packages to help in
this situation.

Using pip to install packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to install package from PyPI, use the ``pip`` command.
We can search for PyPI for packages::
 $ pip search --trusted-host pypi.python.org autopep8 pylint

It appears that the top two results are what we want so install them::

  $ pip install --trusted-host pypi.python.org autopep8 pylint

This will cause ``pip`` to download the packages from PyPI, extract
them, check their dependencies and install those as needed, then
install the requested packages.

.. note:: You can skip '--trusted-host pypi.python.org' option if you have a
        patch on urllib3 on Python 2.7.9.

Using autopep8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can now run the bad code through autopep8 to fix formatting
problems::

  $ autopep8 bad_code_example.py >code_example_autopep8.py

Let's look at the result.
This is considerably better than before.
It is easy to tell what the example1 and example2 functions are doing.

It is a good idea to develop a habit of using ``autopep8`` in your
python-development workflow.  For instance: use ``autopep8`` to check
a file, and if it passes, make any changes in place using the ``-i``
flag::

  $ autopep8 file.py    # check output to see of passes
  $ autopep8 -i file.py # update in place




.. _Python Package Index: https://pypi.python.org/pypi

Further Learning
----------------------------------------------------------------------
There is much more to python than what we have covered here:

- conditional expression (``if``, ``if...then``,``if..elif..then``)
- function definition(``def``)
- class definition (``class``)
- function positional arguments and keyword arguments
- lambda expression
- iterators
- generators
- loops
- docopts
- humanize

.. note:: you can receive extra credit if you contribute such a
	  section of your choice addressing the above topics


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
be the package called cloudmesh_client which you can install with::

   pip install cloudmesh_client

If all goes well the package will be installed.

Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Useful ecosystem Links:

* https://virtualenvwrapper.readthedocs.io
* https://github.com/yyuu/pyenv
* https://amaral.northwestern.edu/resources/guides/pyenv-tutorial
* https://godjango.com/96-django-and-python-3-how-to-setup-pyenv-for-multiple-pythons/
* https://www.accelebrate.com/blog/the-many-faces-of-python-and-how-to-manage-them/
