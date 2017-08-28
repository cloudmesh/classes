
.. _python_intro:

Introduction to Python
======================


Portions of this lesson have been adapted from the `official Python
Tutorial`_ copyright `Python Software Foundation`_.

.. _official Python Tutorial: https://docs.python.org/2/tutorial/
.. _Python Software Foundation: http://www.python.org/

   
Python is an easy to learn programming language. It has efficient
high-level data structures and a simple but effective approach to
object-oriented programming. Python’s simple syntax and dynamic
typing, together with its interpreted nature, make it an ideal
language for scripting and rapid application development in many areas
on most platforms. The Python interpreter and the extensive standard
library are freely available in source or binary form for all major
platforms from the Python Web site, https://www.python.org/, and may
be freely distributed. The same site also contains distributions of
and pointers to many free third party Python modules, programs and
tools, and additional documentation. The Python interpreter can be
extended with new functions and data types implemented in C or C++ (or
other languages callable from C). Python is also suitable as an
extension language for customizable applications.

Python is an interpreted, dynamic, high-level programming language
suitable for a wide range of applications.


The philosophy of python is summarized in `The Zen of Python`_
as follows:

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

About the Tutorial
------------------

This tutorial introduces the reader informally to the basic concepts
and features of the Python language and system. It helps to have a
Python interpreter handy for hands-on experience, but all examples are
self-contained, so the tutorial can be read off-line as well. At the
end of this lesson you will be able to:

- use Python
- use the interactive Python interface
- understand the basic syntax of Python
- write and run Python programs stored in a file
- have an overview of the standard library
- install Python libraries using `pyenv` or if it is not available `virtualenv`

This tutorial does not attempt to be comprehensive and cover every
single feature, or even every commonly used feature. Instead, it
introduces many of Python's most noteworthy features, and will give
you a good idea of the language's flavor and style. After reading it,
you will be able to read and write Python modules and programs, and
you will be ready to learn more about the various Python library
modules.

.. _The Zen of Python: https://www.python.org/dev/peps/pep-0020/

In order to conduct this lesson you need

* A computer with Python 2.7.13 or 3.6.2
* Familiarity with command line usage
* A text editor such as `PyCharm
  <https://www.jetbrains.com/pycharm/>`_, emacs, vi or others. You
  should identity which works best for you and set it up.

Links
-----

* `Python <https://www.python.org/>`_
* `Pip <https://pip.pypa.io/en/stable/>`_
* `Virtualenv <https://virtualenv.pypa.io/en/stable/>`_
* `NumPy <http://www.numpy.org/>`_
* `SciPy <https://scipy.org/>`_
* `Matplotlib <http://matplotlib.org/>`_
* `Pandas <http://pandas.pydata.org/>`_
* `pyenv <https://github.com/pyenv/pyenv>`_
* `PyCharm <https://github.com/pyenv/pyenv>`_

Python module of the week is a Web site that provides a number of
short examples on how to use some elementary python modules. Not all
modules are equally useful and you should decide if there are better
alternatives. However for beginners this site provides a number of
good examples

* Python 2: https://pymotw.com/2/
* Python 3: https://pymotw.com/3/



Python Installation
-------------------

Python is easy to install and very good instructions for most
platforms can be found on the python.org Web page. We will be using
Python 2.7.13 and/or Python 3 in our activities.

To manage python modules, it is useful to have `pip
<https://pypi.python.org/pypi/pip>`_ package installation tool on your
system.

In the tutorial, we assume that you have a computer with python
installed.  However, we also recommend that for the class you use
Python's virtualenv (see below) to isolate your development Python
from the system installed Python.


Managing custom Python installs
-------------------------------


Often you have your own computer and you do not like to change its
environment to keep it in pristine condition. Python comes with mnay
libraries that could for example conflict with libraries that you have
installed. To avoid this it is bets to work in an isolated python we
can use tools such as virtualenv, pyenv or pyvenv for 3.6.2. Which you
use depends on you, but we highly recommend pyenv if you can.

.. _section_pyenv:

Managing Multiple Python Versions with Pyenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python has several versions that are used by the community. This
includes Python 2 and Python 3, but alls different management of the
python libraries. As each OS may have their own version of python
installed. It is not recommended that you modify that version. Instead
you may want to create a localized python installation that you as a
user can modify. To do that we recommend *pyenv*. Pyenv allows users
to switch between multiple versions of Python
(https://github.com/yyuu/pyenv). To summarize:

* users to  change the global Python version on a per-user basis;
* users to enable support for per-project Python versions;
* easy version changes without complex environment variable
  management;
* to search installed commands across different python versions;
* integrate with tox (https://tox.readthedocs.io/).

Instalation without pyenv
"""""""""""""""""""""""""
If you need to have more than one python version
installed and do not want or can use pyenv, we recommend you download and install python 2.7.13
and 3.6.2 from python.org (https://www.python.org/downloads/)


Install pyenv on OSX from git 
""""""""""""""""""""""""""""""

This is our recommended way to install pyenv on OSX::

  $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  $ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
  $ git clone https://github.com/yyuu/pyenv-virtualenvwrapper.git $(pyenv root)/plugins/pyenv-virtualenvwrapper
  $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
  $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile


Instalation of Homebrew
"""""""""""""""""""""""

In many occasions it is beneficial to use readline as it provides nice
editing features for the terminal and xz for completion. First, make
sure you have xcode installed::
  
   $ xcode-select --install

Next install homebrew, pyenv, pyenv-virtualenv and
pyenv-virtualwrapper. Additionally install readline and
some compression tools::

   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   brew update
   brew install readline xz

Install pyenv on OSX with Homebrew
""""""""""""""""""""""""""""""""""

We describe here a mechanism of installing pyenv with homebrew. Other
mechanisms can be found on the pyenv documentation page
(https://github.com/yyuu/pyenv-installer).
You must have homebrew installed as discussed in the previous section.

To install pyenv with homebrew execute in the terminal::

  brew install pyenv pyenv-virtualenv pyenv-virtualenvwrapper

   
Install pyenv on Ubuntu
"""""""""""""""""""""""

.. warning:: the installation on ubuntu is not tested and we are
             looking for feedback
             
::

   $ sudo apt-get update
   $ sudo apt-get install git python-pip make build-essential libssl-dev
   $ sudo apt-get install zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev
   $ sudo pip install virtualenvwrapper

   $ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
   $ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv   
   $ git clone https://github.com/yyuu/pyenv-virtualenvwrapper.git ~/.pyenv/plugins/pyenv-virtualenvwrapper

   $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc


Install Different Python Versions
"""""""""""""""""""""""""""""""""

Pyenv provides a large list of different python versions. To see the
entire list please use the command::

   $ pyenv install -l

However, for us we only need to worry about python 2.7.13 and python
3.6.2 (once 3.6.2 becomes available we will use that).
You can now install different versions of python into your local
environment with the following commands::

   $ pyenv install 2.7.13
   $ pyenv install 3.6.2

You can set the global python default version with::

   $ pyenv global 2.7.13

Type the following to determine which versions you have available::

   $ pyenv version

Associate a specific environment name with a certain python version,
use the following commands::
  
   $ pyenv virtualenv 2.7.13 ENV2
   $ pyenv virtualenv 3.6.2 ENV3

In the example above, `ENV2` would represent python 2.7.13 while `ENV3`
would represent python 3.6.2. Often it is easier to type the alias rather 
than the explicit version.
   
Set up the Shell
""""""""""""""""

To make all work smoothly from your terminal, you can 
include the following in your .bashrc files::

   export PYENV_VIRTUALENV_DISABLE_PROMPT=1
   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"

   __pyenv_version_ps1() {
     local ret=$?;
     output=$(pyenv version-name)
     if [[ ! -z $output ]]; then
       echo -n "($output)"
     fi
     return $ret;
   }

   PS1="\$(__pyenv_version_ps1) ${PS1}"

We recommend that you do this towards the end of your file.   
   
Switching Environments
""""""""""""""""""""""

After setting up the different environments, switching between them is
now easy.  Simply use the following commands::

  
  (2.7.13) $ pyenv activate ENV2
  (ENV2) $ pyenv activate ENV3
  (ENV3) $ pyenv activate ENV2
  (ENV2) $ pyenv deactivate ENV2
  (2.7.13) $ 

To make it even easier, you can add the following lines to your
`.bash_profile` file::

  alias ENV2="pyenv activate ENV2"
  alias ENV3="pyenv activate ENV3"

If you start a new terminal, you can switch between the different
versions of python simply by typing::

  $ ENV2
  $ ENV3


Instalation without pyenv
-------------------------

If you need to have more than one python version installed and do not
want or can use pyenv, we recommend you download and install python
2.7.13 and 3.6.2 from python.org (https://www.python.org/downloads/)

Make sure pip is up to date
^^^^^^^^^^^^^^^^^^^^^^^^^^^

As you will want to install other packages, make sure pip is up to
date::

   pip install pip -U


pyenv  virtualenv anaconda3-4.3.1 ANA3
pyenv activate ANA3

Anaconda and Miniconda
----------------------

.. warning:: We do not recommend that you use anaconda or miniconda as it may
	     interfere with your default python interpreters and
	     setup.

Please note that beginners to pyton should always use anaconda or
miniconda only afterthey have installed pyenv and use it. For this
class neither anaconda nor miniconda is required. In fact we do not
recommend it. We keep this section as we know that other classes at IU
may use anaconda. We are not aware if these classes teach you the
right way to install it, with *pyenv*.


Miniconda
^^^^^^^^^

.. warning:: This section about miniconda is experimental and has not
             been tested. We are looking for contributors that help
             completing it. If you use anaconda or miniconda we
             recommend to manage it via pyenv.

To install mini conda you can use the following commands::

   $ mkdir ana
   $ cd ana
   $ pyenv install miniconda3-latest
   $ pyenv local miniconda3-latest
   $ pyenv activate miniconda3-latest
   $ conda create -n ana anaconda

To activate use::
  
   $ source activate ana

To deactivate use::

  $ source deactivate

To install cloudmesh cmd5 please use:: 

  $ pip install cloudmesh.cmd5
  $ pip install cloudmesh.sys

  
Anaconda
^^^^^^^^

.. warning:: This section about anaconda is experimental and has not
             been tested. We are looking for contributors that help
             completing it.


You can add anaconda to your pyenv with the following commands::

  pyenv install anaconda3-4.3.1

To switch more easily we recommend that you use the following in your
`.bash_profile` file::

  alias ANA="pyenv activate anaconda3-4.3.1"

Once you have done this you can easily switch to anaconda with the
command::

  $ ANA
  
Terminology in annaconda could lead to confusion. Thus we like to
point out that the version number of anaconda is unrelated to the
python version. Furthermore, anaconda uses the term root not for the
root user, but for the originating directory in which the anaconda
program is installed.

In case you like to build your own conda packages at a later time we
recommend that you install the `conda-build` package::

  $ conda install conda-build


When executing::

   pyenv versions

you will see after the install completed the anaconda versions installed::
   
   pyenv versions
   system
   2.7.13
   2.7.13/envs/ENV2
   3.6.2
   3.6.2/envs/ENV3
   ENV2 
   ENV3
   * anaconda3-4.3.1 (set by PYENV_VERSION environment variable)


Let us now create virtualenv for anaconda::

   $ pyenv virtualenv anaconda3-4.3.1 ANA

To activate it you can now use::

  $ pyenv ANA

However, anaconda may modify your .bashrc or .bash_profile files and ,
may result in incompatibilities with other python versions. For this
reason we recommend not to use it. If you find ways to get it to work
reliably with other versions, please let us know and we update this
tutorial.

To install cloudmesh cmd5 please use::

  $ pip install cloudmesh.cmd5
  $ pip install cloudmesh.sys
  
   
Exercise
"""""""""

Epyenv.1:
   Write installation instructions for an operating system of your choice
   and add to this documentation.

Epyenv.2:
   Replicate the steps above, so you can type in ENV2 and ENV3 in your
   terminals to switch between python 2 and 3.
   

   

.. _virtualenv_:

virtualenv
^^^^^^^^^^

environment while using virtualenv,. Documentation about it can be
found at::

* https://virtualenv.pypa.io

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

you can put this command in your `.bashrc` or `.bash_profile` files so you
do not forget to activate it. :ref:`Instructions for this can be
found in our lesson on Linux <bashrc>`.

Interactive Python
------------------

Python can be used interactively.  Start by entering the interactive
loop by executing the command::

  $ python

You should see something like the following::

  Python 2.7.13 (default, Nov 19 2016, 06:48:10)
  [GCC 5.4.0 20160609] on linux2
  Type "help", "copyright", "credits" or "license" for more information.
  >>>
  
The `>>>` is the prompt for the interpreter. This is similar to the
shell interpreter you have been using.

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

Python 3 Features in Python 2
-----------------------------

As mentioned earlier, we assume you will use Python 2.7.X because
there are still some libraries that haven't been ported to
Python 3. However, there are some features of Python 3 we can and want
to use in Python 2.7. Before we do anything else, we need to make
these features available to any subsequent code we write::

  >>> from __future__ import print_function, division

.. note::

   The first of these imports allows us to use the `print` function
   to output text to the screen, instead of the `print` statement,
   which Python 2 uses. This is simply a `design decision
   <https://www.python.org/dev/peps/pep-3105/>`_ that better reflects
   Python's underlying philosophy.

.. note::

   The second of these imports makes sure that the `division operator
   <https://www.python.org/dev/peps/pep-0238/>`_ behaves in a way a
   newcomer to the language might find more intruitive. In Python 2,
   division `/` is *floor division* when the arguments are integers,
   meaning that `5 / 2 == 2`, for example. In Python 3, division
   `/` is *true division*, thus `5 / 2 == 2.5`.

Statements and Strings
----------------------

Let us explore the syntax of Python.  Type into the interactive loop
and press Enter::

  >>> print("Hello world from Python!")
  Hello world from Python!

What happened: the `print` function was given a **string** to
process. A string is a sequence of characters.  A **character** can be
a alphabetic (A through Z, lower and upper case), numeric (any of the
digits), white space (spaces, tabs, newlines, etc), syntactic
directives (comma, colon, quotation, exclamation, etc), and so forth.
A string is just a sequence of the character and typically indicated
by surrounding the characters in double quotes.

.. tip::

   Standard output is discussed in the
   :doc:`../../lesson/linux/shell` lesson.

So, what happened when you pressed Enter?  The interactive Python
program read the line `print "Hello world from Python!"`, split it into
the `print` statement and the `"Hello world from Python!"` string, and
then executed the line, showing you the output.

Variables
---------

You can store data into a **variable** to access it later.
For instance, instead of:

.. code:: python

   >>> print('Hello world from Python!')

which is a lot to type if you need to do it multiple times, you can
store the string in a variable for convenient access:

.. code:: python

   >>> hello = 'Hello world from Python!'
   >>> print(hello)
   Hello world from Python!


Data Types
----------

Booleans
^^^^^^^^

A **boolean** is a value that indicates *truthness* of something.
You can think of it as a toggle: either "on" or "off", "one" or
"zero", "true" or "false".  In fact, the only possible values of the
**boolean** (or `bool`) type in Python are:

- `True`
- `False`

You can combine booleans with **boolean operators**:

- `and`
- `or`

.. code:: python

   >>> print(True and True)
   True
   >>> print(True and False)
   False
   >>> print(False and False)
   False
   >>> print(True or True)
   True
   >>> print(True or False)
   True
   >>> print(False or False)
   False

Numbers
^^^^^^^

The interactive interpreter can also be used as a calculator.
For instance, say we wanted to compute a multiple of 21:

.. code:: python

   >>> print(21 * 2)
   42

We saw here the `print` statement again. We passed in the result of
the operation `21 * 2`.  An **integer** (or **int**) in Python is a
numeric value without a fractional component (those are called
**floating point** numbers, or **float** for short).

The mathematical operators compute the related mathematical operation
to the provided numbers.  Some operators are:

- `*` --- multiplication
- `/` --- division
- `+` --- addition
- `-` --- subtraction
- `**` --- exponent

Exponentiation is read as `x**y` is `x` to the `y`\th power:

.. math::

   x^y

You can combine **float**\s and **int**\s:

.. code:: python

   >>> print(3.14 * 42 / 11 + 4 - 2)
   13.9890909091
   >>> print(2**3)
   8

Note that **operator precedence** is important.  Using parenthesis to
indicate affect the order of operations gives a difference results, as
expected:

.. code:: python

   >>> print(3.14 * (42 / 11) + 4 - 2)
   11.42
   >>> print(1 + 2 * 3 - 4 / 5.0)
   6.2
   >>> print( (1 + 2) * (3 - 4) / 5.0 )
   -0.6

REPL (Read Eval Print Loop)
----------------------------

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

There are many different types beyond what we have seen so far, such
as **dictionaries**\s, **list**\s, **set**\s. One handy way of using
the interactive python is to get the type of a value using `type()`:

.. code:: python

   >>> type(42)
   <type 'int'>
   >>> type(hello)
   <type 'str'>
   >>> type(3.14)
   <type 'float'>

You can also ask for help about something using `help()`:

.. code:: python

   >>> help(int)
   >>> help(list)
   >>> help(str)

.. tip::

   Using `help()` opens up a pager. To navigate you can use the
   spacebar to go down a page `w` to go up a page, the arrow keys to
   go up/down line-by-line, or `q` to exit.

Control Statements
------------------

Comparision
^^^^^^^^^^^

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

    >>> x = int(input("Guess x:"))
    >>> if x == 4:
    ...    print('You guessed correctly!')
    ...    <ENTER>

In this example, *You guessed correctly!* will only be printed if the
variable `x` equals to four (see table above). Python can also
execute multiple conditions using the `elif` and `else` keywords.

.. code:: python

    >>> x = int(input("Guess x:"))
    >>> if x == 4:
    ...     print('You guessed correctly!')
    ... elif abs(4 - x) == 1:
    ...     print('Wrong guess, but you are close!')
    ... else:
    ...     print('Wrong guess')
    ... <ENTER>

Iteration
^^^^^^^^^

To repeat code, the `for` keyword can be used. For example, to
display the numbers from 1 to 10, we could write something like this:

.. code:: python

    >>> for i in range(1, 11):
    ...    print('Hello!')

The second argument to `range`, *11*, is not inclusive, meaning that
the loop will only get to *10* before it finishes.  Python itself
starts counting from 0, so this code will also work:

.. code:: python

    >>> for i in range(0, 10):
    ...    print(i + 1)

In fact, the `range` function defaults to starting value of *0*, so the above is equivalent to:

.. code:: python

    >>> for i in range(10):
    ...	   print(i + 1)
	   
We can also nest loops inside each other:

.. code:: python

   >>> for i in range(0,10):
   ...     for j in range(0,10):
   ...         print(i,' ',j)
   ... <ENTER>

In this case we have two nested loops. The code will iterate over
the entire coordinate range (0,0) to (9,9)

Datatypes
---------

Lists
^^^^^

see: https://www.tutorialspoint.com/python/python_lists.htm

Lists in Python are ordered sequences of elements, where each element
can be accessed using a 0-based index.

To define a list, you simply list its elements between square brackest
`[]`:

.. code:: python

  >>> >>> names = ['Albert', 'Jane', 'Liz', 'John', 'Abby']
  >>> names[0] # access the first element of the list
  'Albert'
  >>> names[2] # access the third element of the list
  'Liz'

You can also use a negative index if you want to start counting
elements from the end of the list. Thus, the last element has index
*-1*, the second before last element has index *-2* and so on:

.. code:: python

  >>> names[-1] # access the last element of the list
  'Abby'
  >>> names[-2] # access the second last element of the list
  'John'

Python also allows you to take whole slices of the list by specifing a
beginning and end of the slice separated by a colon `:`:

.. code:: python

  >>> names[1:-1] # the middle elements, excluding first and last
  ['Jane', 'Liz', 'John']

As you can see from the example above, the starting index in the slice
is inclusive and the ending one, exclusive.

Python provides a variety of methods for manipulating the members of a
list.

You can add elements with `append`:

.. code:: python

  >>> names.append('Liz')
  >>> names
  ['Albert', 'Jane', 'Liz', 'John', 'Abby', 'Liz']

As you can see, the elements in a list need not be unique.

Merge two lists with `extend`:

.. code:: python

  >>> names.extend(['Lindsay', 'Connor'])
  >>> names
  ['Albert', 'Jane', 'Liz', 'John', 'Abby', 'Liz', 'Lindsay', 'Connor']

Find the index of the first occurrence of an element with `index`:

.. code:: python

  >>> names.index('Liz')
  2

Remove elements by value with `remove`:

.. code:: python

  >>> names.remove('Abby')
  >>> names
  ['Albert', 'Jane', 'Liz', 'John', 'Liz', 'Lindsay', 'Connor']

Remove elements by index with `pop`:

.. code:: python

  >>> names.pop(1)
  'Jane'
  >>> names
  ['Albert', 'Liz', 'John', 'Liz', 'Lindsay', 'Connor']

Notice that `pop` returns the element being removed, while
`remove` does not.

If you are familiar with stacks from other programming languages, you
can use `insert` and `pop`:

.. code:: python

  >>> names.insert(0, 'Lincoln')
  >>> names
  ['Lincoln', 'Albert', 'Liz', 'John', 'Liz', 'Lindsay', 'Connor']
  >>> names.pop()
  'Connor'
  >>> names
  ['Lincoln', 'Albert', 'Liz', 'John', 'Liz', 'Lindsay']

The Python documentation contains a `full list of list operations <>`_.

To go back to the `range` function you used earlier, it simply
creates a list of numbers:

.. code:: python

  >>> range(10)
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  >>> range(2, 10, 2)
  [2, 4, 6, 8]
    
Sets
^^^^

Python lists can contain duplicates as you saw above:

.. code:: python

  >>> names = ['Albert', 'Jane', 'Liz', 'John', 'Abby', 'Liz']

When we don't want this to be the case, we can use a `set
<https://docs.python.org/2/library/stdtypes.html#set>`_:

.. code:: python

  >>> unique_names = set(names)
  >>> unique_names
  set(['Lincoln', 'John', 'Albert', 'Liz', 'Lindsay'])

Keep in mind that the *set* is an unordered collection of objects,
thus we can not access them by index:

.. code:: python

  >>> unique_names[0]
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'set' object does not support indexing

However, we can convert a set to a list easily:

>>> unique_names = list(unique_names)
>>> unique_names
['Lincoln', 'John', 'Albert', 'Liz', 'Lindsay']
>>> unique_names[0]
'Lincoln'

Notice that in this case, the order of elements in the new list
matches the order in which the elements were displayed when we create
the set (we had `set(['Lincoln', 'John', 'Albert', 'Liz',
'Lindsay'])` and now we have `['Lincoln', 'John', 'Albert', 'Liz',
'Lindsay']`). You should not assume this is the case in general. That
is, don't make any assumptions about the order of elements in a set
when it is converted to any type of sequential data structure.

You can change a set's contents using the `add`, `remove` and
`update` methods which correspond to the `append`, `remove` and
`extend` methods in a list. In addition to these, *set* objects
support the operations you may be familiar with from mathematical
sets: *union*, *intersection*, *difference*, as well as operations to
check containment. You can read about this in the `Python
documentation for sets
<https://docs.python.org/2/library/stdtypes.html#set>`_.

Removal and Testing for Membership in Sets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One important advantage of a *set* over a *list* is that **access to
elements is fast**. If you are familiar with different data structures
from a Computer Science class, the Python list is implemented by an
array, while the set is implemented by a hash table.

We will demonstrate this with an example. Let's say we have a list and
a set of the same number of elements (approximately 100 thousand):

.. code:: python

  >>> import sys, random, timeit
  >>> nums_set = set([random.randint(0, sys.maxint) for _ in range(10**5)])
  >>> nums_list = list(nums_set)
  >>> len(nums_set)
  100000

We will use the `timeit
<https://docs.python.org/2/library/timeit.html>`_ Python module to
time 100 operations that test for the existence of a member in either
the list or set:

.. code:: python

  >>> timeit.timeit('random.randint(0, sys.maxint) in nums', setup='import random; nums=%s' % str(nums_set), number=100)
  0.0004038810729980469
  >>> timeit.timeit('random.randint(0, sys.maxint) in nums', setup='import random; nums=%s' % str(nums_list), number=100)
  0.3980541229248047

The exact duration of the operations on your system will be different,
but the take away will be the same: searching for an element in a set
is orders of magnitude faster than in a list. This is important to
keep in mind when you work with large amounts of data.

Dictionaries
^^^^^^^^^^^^

One of the very important data structures in python is a dictionary
also referred to as *dict*.

A dictionary represents a key value store:

.. code:: python
	  
  >>> person = {'Name': 'Albert', 'Age': 100, 'Class': 'Scientist'}
  >>> print("person['Name']: ", person['Name'])
  person['Name']:  Albert
  >>> print("person['Age']: ", person['Age'])
  person['Age']:  100

You can delete elements with the following commands:

.. code:: python

  >>> del person['Name'] # remove entry with key 'Name'
  >>> person
  {'Age': 100, 'Class': 'Scientist'}
  >>> person.clear()     # remove all entries in dict
  >>> person
  {}
  >>> del person         # delete entire dictionary
  >>> person
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'person' is not defined

You can iterate over a dict:

.. code:: python

  >>> person = {'Name': 'Albert', 'Age': 100, 'Class': 'Scientist'}
  >>> for item in person:
  ...   print(item, person[item])
  ...   <ENTER>
  Age 100
  Name Albert
  Class Scientist

Dictionary Keys and Values
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can retrieve both the keys and values of a dictionary using the
`keys()` and `values()` methods of the dictionary, respectively:

.. code:: python
     
  >>> person.keys()
  ['Age', 'Name', 'Class']
  >>> person.values()
  [100, 'Albert', 'Scientist']

Both methods return lists. Notice, however, that the order in which
the elements appear in the returned lists (`Age`, `Name`,
`Class`) is different from the order in which we listed the elements
when we declared the dictionary initially (`Name`, `Age`,
`Class`). It is important to keep this in mind: **you can't make any
assumptions about the order in which the elements of a dictionary will
be returned by the `keys()` and `values()` methods**.

However, you can assume that if you call `keys()` and `values()`
in sequence, the order of elements will at least correspond in both
methods. In the above example `Age` corresponds to `100`, `Name`
to `'Albert`, and `Class` to `Scientist`, and you will observe
the same correspondence in general as long as **`keys()` and
`values()` are called one right after the other**.

Counting with Dictionaries
^^^^^^^^^^^^^^^^^^^^^^^^^^

One application of dictionaries that frequently comes up is counting
the elements in a sequence. For example, say we have a sequence of
coin flips:

.. code:: python
	  
  >>> import random
  >>> die_rolls = [random.choice(['heads', 'tails']) for _ in range(10)]
  >>> die_rolls
  ['heads', 'tails', 'heads', 'tails', 'heads', 'heads', 'tails', 'heads', 'heads', 'heads']

The actual list `die_rolls` will likely be different when you
execute this on your computer since the outcomes of the die rolls are
random.

To compute the probabilities of heads and tails, we could count how
many heads and tails we have in the list:

.. code:: python
	  
  >>> counts = {'heads': 0, 'tails': 0}
  >>> for outcome in coin_flips:
  ...   assert outcome in counts
  ...   counts[outcome] += 1
  ...   <ENTER>
  >>> print('Probability of heads: %.2f' % (counts['heads'] / len(coin_flips)))
  Probability of heads: 0.70
  >>> print('Probability of tails: %.2f' % (counts['tails'] / sum(counts.values())))
  Probability of tails: 0.30

In addition to how we use the dictionary `counts` to count the
elements of `coin_flips`, notice a couple things about this example:

#. We used the `assert outcome in counts` statement. The `assert`
   statement in Python allows you to easily insert debugging
   statements in your code to help you discover errors more
   quickly. `assert` statements are executed whenever the internal
   Python `__debug__` variable is set to `True`, which is always
   the case unless you start Python with the `-O` option which
   allows you to run *optimized* Python.

#. When we computed the probability of tails, we used the built-in
   `sum` function, which allowed us to quickly find the total number
   of coin flips. `sum` is one of many built-in function you can
   `read about here
   <https://docs.python.org/2/library/functions.html>`_.


Functions
---------

You can reuse code by putting it inside a function that you can call
in other parts of your programs. Functions are also a good way of
grouping code that logically belongs together in one coherent whole. A
function has a unique name in the program. Once you call a function, it
will execute its body which consists of one or more lines of code:

.. code:: python

    def check_triangle(a, b, c):
	return \
		a < b + c and a > abs(b - c) and \
		b < a + c and b > abs(a - c) and \
		c < a + b and c > abs(a - b)

    print(check_triangle(4, 5, 6))

The `def` keyword tells Python we are defining a function. As part
of the definition, we have the function name, `check_triangle`, and
the parameters of the function -- variables that will be populated
when the function is called.

We call the function with arguments `4`, `5` and `6`, which are
passed in order into the parameters `a`, `b` and `c`.  A
function can be called several times with varying parameters. There is
no limit to the number of function calls.

It is also possible to store the output of a function in a variable,
so it can be reused.

.. code:: python

   def check_triangle(a, b, c):
	return \
		a < b + c and a > abs(b - c) and \
		b < a + c and b > abs(a - c) and \
		c < a + b and c > abs(a - b)

   result = check_triangle(4, 5, 6)
   print(result)

.. _doc_python_intro_sec_classes:

Classes
-------

A class is an encapsulation of data and the processes that work on
them. The data is represented in member variables, and the processes
are defined in the methods of the class (methods are functions inside
the class). For example, let's see how to define a `Triangle` class:

.. code:: python

   class Triangle(object):

	def __init__(self, length, width, height, angle1, angle2, angle3):
		if not self._sides_ok(length, width, height):
			print('The sides of the triangle are invalid.')
		elif not self._angles_ok(angle1, angle2, angle3):
			print('The angles of the triangle are invalid.')

		self._length = length
		self._width = width
		self._height = height

		self._angle1 = angle1
		self._angle2 = angle2
		self._angle3 = angle3
		
	def _sides_ok(self, a, b, c):
		return \
			a < b + c and a > abs(b - c) and \
			b < a + c and b > abs(a - c) and \
			c < a + b and c > abs(a - b)

	def _angles_ok(self, a, b, c):
		return a + b + c == 180

   triangle = Triangle(4, 5, 6, 35, 65, 80)

Python has full Aobject-oriented programming (OOP) capabilities,
however we can not cover all of them in a quick tutorial, so please
refer to the `Python docs on classes and OOP
<https://docs.python.org/2.7/tutorial/classes.html>`_.

Database Access
---------------

see: https://www.tutorialspoint.com/python/python_database_access.htm

Modules
-------

Make sure you are no longer in the interactive interpreter.
If you are you can type `quit()` and press Enter to exit.

You can save your programs to files which the interpreter can then
execute.  This has the benefit of allowing you to track changes made
to your programs and sharing them with other people.

Start by opening a new file `hello.py` in the Python editor of your
choice. If you don't have a preferred editor, we recommend `PyCharm
<https://www.jetbrains.com/pycharm/>`_.

Now write this simple program and save it:

.. code:: python

  from __future__ import print_statement, division
  print("Hello world!")

As a check, make sure the file contains the expected contents on the
command line::

  $ cat hello.py
  from __future__ import print_statement, division
  print("Hello world!")

To execute your program pass the file as a parameter to the `python`
command::

  $ python hello.py
  Hello world!

Files in which Python code is stored are called **module**\s. You can
execute a Python module form the command line like you just did, or
you can import it in other Python code using the `import` statement.

Let's write a more involved Python program that will receive as input
the lengths of the three sides of a triangle, and will output whether
they define a valid triangle. A triangle is valid if the length of
each side is less than the sum of the lengths of the other two sides
and greater than the difference of the lengths of the other two sides.::

  """Usage: check_triangle.py [-h] LENGTH WIDTH HEIGHT

  Check if a triangle is valid.

  Arguments:
    LENGTH     The length of the triangle.
    WIDTH      The width of the traingle.
    HEIGHT     The height of the triangle.

  Options:
  -h --help
  """
  from __future__ import print_function, division
  from docopt import docopt

  if __name__ == '__main__':
	args = docopt(__doc__)
	a, b, c = int(args['LENGTH']), int(args['WIDTH']), int(args['HEIGHT'])
	valid_triangle = \
		a < b + c and a > abs(b - c) and \
		b < a + c and b > abs(a - c) and \
		c < a + b and c > abs(a - b)
	print('Triangle with sides %d, %d and %d is valid: %r' % (
		a, b, c, valid_triangle
	))

Assuming we save the program in a file called `check_triangle.py`,
we can run it like so::

  $ python check_triangle.py 4 5 6
  Triangle with sides 4, 5 and 6 is valid: True

Let break this down a bit.

#. We are importing the `print_function` and `division` modules
   from Python 3 like we did earlier in this tutorial. It's a good
   idea to always include these in your programs.
#. We've defined a boolean expression that tells us if the sides that
   were input define a valid triangle. The result of the expression is
   stored in the `valid_triangle` variable.  inside are true, and
   `False` otherwise.
#. We've used the backslash symbol `\` to format are code
   nicely. The backslash simply indicates that the current line is
   being continued on the next line.
#. When we run the program, we do the check `if __name__ ==
   '__main__'`. `__name__` is an internal Python variable that
   allows us to tell whether the current file is being run from the
   command line (value `__name__`), or is being imported by a module
   (the value will be the name of the module). Thus, with this
   statement we're just making sure the program is being run by the
   command line.
#. We are using the `docopt` module to handle command line
   arguments. The advantage of using this module is that it generates
   a usage help statement for the program and enforces command line
   arguments automatically. All of this is done by parsing the
   docstring at the top of the file.
#. In the `print` function, we are using `Python's string formatting
   capabilities
   <https://docs.python.org/2/library/string.html#format-string-syntax>`_
   to insert values into the string we are displaying.

Installing Libraries
--------------------

Often you may need functionality that is not present in Python's
standard library.  In this case you have two option:

- implement the features yourself
- use a third-party library that has the desired features.

Often you can find a previous implementation of what you need.
Since this is a common situation, there is a service supporting it:
the `Python Package Index`_ (or PyPi for short).


Our task here is to install the `autopep8`_ tool from PyPi.  This will
allow us to illustrate the use if virtual environments using the
`pyenv` or `virtualenv` command, and installing and uninstalling
PyPi packages using `pip`.

Using pip to Install Packages
-----------------------------

Let's now look at another important tool for Python development: the
Python Package Index, or PyPI for short.  PyPI provides a large set of
third-party python packages.  If you want to do something in python,
first check pypi, as odd are someone already ran into the problem and
created a package solving it.

In order to install package from PyPI, use the `pip` command.
We can search for PyPI for packages::

  $ pip search --trusted-host pypi.python.org autopep8 pylint

It appears that the top two results are what we want so install them::

  $ pip install --trusted-host pypi.python.org autopep8 pylint

This will cause `pip` to download the packages from PyPI, extract
them, check their dependencies and install those as needed, then
install the requested packages.

.. note:: You can skip '--trusted-host pypi.python.org' option if you have
          patched urllib3 on Python 2.7.9.


GUI
---

GUIZero
^^^^^^^

Install guizero with the following command:

::

    sudo pip3 install guizero

For a comprehensive tutorial on guizero, `click
here <https://lawsie.github.io/guizero/howto/>`__.

Kivy
^^^^

You can install Kivy on OSX as followes::

    brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer
    pip install -U Cython
    pip install kivy
    pip install pygame

A hello world program for kivy is included in the cloudmesh.robot
repository. Which you can fine here

* https://github.com/cloudmesh/cloudmesh.robot/tree/master/projects/kivy

To run the program, please download it or execute it in
cloudmesh.robot as follows::

    cd cloudmesh.robot/projects/kivy
    python swim.py

To create stand alone packages with kivy, please see::

-  https://kivy.org/docs/guide/packaging-osx.html


          
.. _Virtual_Environments:

Formatting and Checking Python Code
-----------------------------------


First, get the bad code::

  $ wget --no-check-certificate http://git.io/pXqb -O bad_code_example.py

Examine the code::

  $ emacs bad_code_example.py

As you can see, this is very dense and hard to read.  Cleaning it up
by hand would be a time-consuming and error-prone process.  Luckily,
this is a common problem so there exist a couple packages to help in
this situation.

Using autopep8
--------------

We can now run the bad code through autopep8 to fix formatting
problems::

  $ autopep8 bad_code_example.py >code_example_autopep8.py

Let us look at the result.  This is considerably better than before.
It is easy to tell what the example1 and example2 functions are doing.

It is a good idea to develop a habit of using `autopep8` in your
python-development workflow.  For instance: use `autopep8` to check
a file, and if it passes, make any changes in place using the `-i`
flag::

  $ autopep8 file.py    # check output to see of passes
  $ autopep8 -i file.py # update in place

.. _Python Package Index: https://pypi.python.org/pypi

If you use pyCharm you have the ability to use a similar function
while p;ressing on `Inspect Code`. 

Further Learning
----------------

There is much more to python than what we have covered here:

- conditional expression (`if`, `if...then`,`if..elif..then`)
- function definition(`def`)
- class definition (`class`)
- function positional arguments and keyword arguments
- lambda expression
- iterators
- generators
- loops
- docopts
- humanize

Writing Python 3 Compatible Code
--------------------------------

To write python 2 and 3 compatib;e code we recommend that you take a
look at: http://python-future.org/compatible_idioms.html

Using Python on FutureSystems
-----------------------------

.. warning:: This is only important if you use Futuresystems resources.

In order to use Python you must log into your FutureSystems account.
Then at the shell prompt execute the following command::

  $ module load python

This will make the `python` and `virtualenv` commands available to
you.


.. tip::

   The details of what the `module load` command does are described
   in the future lesson :doc:`modules`.
   

Ecosystem
---------


pypi
^^^^

Link: `pypi <https://pypi.python.org/pypi>`_

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

Alternative Installations
^^^^^^^^^^^^^^^^^^^^^^^^^

The basic installation of python is provided by python.org. However
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

.. _python-resources:

.. _autoenv_:

Autoenv: Directory-based Environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning:: We do not recommend that you use autoenv. Instead we
	     recommend that you use `pyenv`.

Link: `Autoenv <https://pypi.python.org/pypi/autoenv/0.2.0>`
	     
If a directory contains a `.env` file, it will automatically be executed
when you `cd` into it. It's easy to use and install.

This is useful for 

* auto-activating virtualenvs
* project-specific environment variables


To use it add the ENV you created with virtualenv into `.env` file
within your project directory::

   $ echo "source ~/ENV/bin/activate" > yourproject/.env
   $ echo "echo 'whoa'" > yourproject/.env
   $ cd project
   whoa


To install it on Mac OS X use Homebrew::

   $ brew install autoenv
   $ echo "source $(brew --prefix autoenv)/activate.sh" >> ~/.bash_profile


To install it using pip use::

   $ pip install autoenv
   $ echo "source `which activate.sh`" >> ~/.bashrc


To install it using git use::

   $ git clone git://github.com/kennethreitz/autoenv.git ~/.autoenv
   $ echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc


Before sourcing activate.sh, you can set the following variables:

* `AUTOENV_AUTH_FILE`: Authorized env files, defaults to `~/.autoenv_authorized`
* `AUTOENV_ENV_FILENAME`: Name of the `.env` file, defaults to `.env`
* `AUTOENV_LOWER_FIRST`: Set this variable to flip the order of `.env` files executed


Autoenv overrides `cd`. If you already do this, invoke
`autoenv_init` within your custom `cd` after sourcing
`activate.sh`.

Autoenv can be disabled via `unset cd` if you experience I/O issues
   with certain file systems, particularly those that are FUSE-based
   (such as `smbnetfs`).


Resources
---------

If you are unfamiliar with programming in Python, we also refer you
to some of the numerous online resources. You may wish to start with
`Learn Python`_ or the book `Learn Python the Hard Way`_. Other
options include `Tutorials Point`_ or `Code Academy`_, and the Python wiki page
contains a long list of `references for learning`_ as well.
Additional resources include:

* https://virtualenvwrapper.readthedocs.io
* https://github.com/yyuu/pyenv
* https://amaral.northwestern.edu/resources/guides/pyenv-tutorial
* https://godjango.com/96-django-and-python-3-how-to-setup-pyenv-for-multiple-pythons/
* https://www.accelebrate.com/blog/the-many-faces-of-python-and-how-to-manage-them/
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


.. _lab-python-1:
.. _lab-python-2:

.. _e-python:

Exercises
---------

EPython.1:
    Write a python program called `iterate.py` that
    accepts an integer n from the command line.  Pass this integer to
    a function called `iterate`.

    The `iterate` function should then iterate from 1 to n.  If the
    ith number is a multiple of three, print "multiple of 3", if a
    multiple of 5 print "multiple of 5", if a multiple of both print
    "multiple of 3 and 5", else print the value.


EPython.2:
    #. Create a pyenv or virtualenv `~/ENV`
    #. Modify your `~/.bashrc` shell file to activate your environment
       upon login.
    #. Install the `docopt` python package using `pip`
    #. Write a program that uses `docopt` to define a commandline
       program. Hint: modify the iterate program.
    #. Demonstrate the program works and submit the code and output.

