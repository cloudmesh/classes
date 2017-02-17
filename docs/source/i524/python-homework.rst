Python Homework
===============

.. contents::
   
In this homework you need to complete a few simple Python
exercises. Before you begin, please refer to the Python lessons on the
course website:

#. :doc:`Python Introduction <../lesson/prg/python_intro>`
#. :doc:`Python for Big Data <../lesson/prg/python_big_data>`
      

`cmd` Module
------------

The Python `cmd` module contains a public class, `Cmd`, designed to be
used as a base class for command processors such as interactive shells
and other command interpreters.

*Hello, World* with `cmd`
~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows a very simple command interpreter that simply
responds to the `greet` command.

In order to demonstrate commands provided by `cmd`, let's save the
following program in a file called `helloworld.py`.

.. code:: python

  from __future__ import print_function, division
  import cmd


  class HelloWorld(cmd.Cmd):
      '''Simple command processor example.'''

      def do_greet(self, line):
          if line is not None and len(line.strip()) > 0:
              print('Hello, %s!' % line.strip().title())
          else:
              print('Hello!')

      def do_EOF(self, line):
          print('bye, bye')
          return True


  if __name__ == '__main__':
      HelloWorld().cmdloop()

A session with this program might look like this::

  $ python helloworld.py

  (Cmd) help

  Documented commands (type help <topic>):
  ========================================
  help

  Undocumented commands:
  ======================
  EOF  greet

  (Cmd) greet
  Hello!
  (Cmd) greet albert
  Hello, Albert!
  <CTRL-D pressed>
  (Cmd) bye, bye


The `Cmd` class can be used to customize a subclass that becomes a
user-defined command prompt. After you have executed your program,
commands defined in your class can be used. Take note of the
following in this example:

* The methods of the class of the form `do_xxx` implement the shell
  commands, with `xxx` being the name of the command. For example, in
  the `HelloWorld` class, the function `do_greet` maps to the `greet`
  on the command line.

* The `EOF` command is a special command that is executed when you
  press CTRL-D on your keyboard.

* As soon as any command method returns `True` the shell application
  exits. Thus, in this example the shell is exited by pressing CTRL-D,
  since the `do_EOF` method is the only one that returns `True`.

* The shell application is started by calling the `cmdloop` method of
  the class.

A More Involved Example
~~~~~~~~~~~~~~~~~~~~~~~

Let's look at a little more involved example. Save the following code
in a file called `calculator.py`.

.. code:: python

   from __future__ import print_function, division
   import cmd


   class Calculator(cmd.Cmd):
	prompt = 'calc >>> '
	intro = 'Simple calculator that can do addition, subtraction, multiplication and division.'

	def do_add(self, line):
		args = line.split()
		total = 0
		for arg in args:
			total += float(arg.strip())
		print(total)

	def do_subtract(self, line):
		args = line.split()
		total = 0
		if len(args) > 0:
			total = float(args[0])
		for arg in args[1:]:
			total -= float(arg.strip())
		print(total)
			
	def do_EOF(self, line):
		print('bye, bye')
		return True


   if __name__ == '__main__':
	Calculator().cmdloop()

A session with this program might look like this::

  $ python calculator.py
  Simple calculator that can do addition, subtraction, multiplication and division.
  calc >>> help

  Documented commands (type help <topic>):
  ========================================
  help

  Undocumented commands:
  ======================
  EOF  add  subtract

  calc >>> add
  0
  calc >>> add 4 5 6
  15.0
  calc >>> subtract
  0
  calc >>> subtract 10 2
  8.0
  calc >>> subtract 10 2 20
  -12.0
  calc >>> bye, bye

* In this case we are using the `prompt` and `intro` class variables
  to define what the default prompt looks like and a welcome message
  when the command interpreter is invoked.

* In the `add` and `subtract` commands we are using the `strip` and
  `split` methods to parse all arguments. If you want to get fancy,
  you can use Python modules like `getopts` or `argparse` for this,
  but this is not necessary in this simple example.

Help Messages
~~~~~~~~~~~~~

Notice that all commands presently show up as undocumented. To remedy
this, we can define `help_` methods for each command:

.. code:: python

  from __future__ import print_function, division
  import cmd


  class Calculator(cmd.Cmd):
	prompt = 'calc >>> '
	intro = 'Simple calculator that can do addition, subtraction, multiplication and division.'

	def do_add(self, line):
		args = line.split()
		total = 0
		for arg in args:
			total += float(arg.strip())
		print(total)

	def help_add(self):
		print('\n'.join([
			'add [number,]',
			'Add the arguments together and display the total.'
		]))

	def do_subtract(self, line):
		args = line.split()
		total = 0
		if len(args) > 0:
			total = float(args[0])
		for arg in args[1:]:
			total -= float(arg.strip())
		print(total)

	def help_subtract(self):
		print('\n'.join([
			'subtract [number,]',
			'Subtract all following arguments from the first argument.'
		]))
			
	def do_EOF(self, line):
		print('bye, bye')
		return True


  if __name__ == '__main__':
	Calculator().cmdloop()

Now, we can obtain help for the `add` and `subtract` commands::

  $ python calculator.py
  Simple calculator that can do addition, subtraction, multiplication and division.
  calc >>> help

  Documented commands (type help <topic>):
  ========================================
  add  help  subtract

  Undocumented commands:
  ======================
  EOF

  calc >>> help add
  add [number,]
  Add the arguments together and display the total.
  calc >>> help subtract
  subtract [number,]
  Subtract all following arguments from the first argument.
  calc >>> bye, bye

Exercises
---------

For more information on the use of `cmd`, please refer to
https://pymotw.com/2/cmd/.

Now that you know a little about the `cmd` module, complete the
following exercises:

Exercise 1
~~~~~~~~~~

Finish implementing the `Calculator` class by adding `multiply` and
`divide` methods.

Exercise 2
~~~~~~~~~~

Create a command-line interpreter, `mycmd`, that has the following
commands:

#. deploy
#. kill
#. benchmark
#. report

Each command should simply print out its name to the screen.

Exercise 3
~~~~~~~~~~

In the :doc:`tutorial on Python for big data
<../lesson/prg/python_big_data>`, you saw how to plot a histogram of
the ages of people who received traffic citations in Q1 2016. Generate
the same histogram with the `pygal <http://pygal.org/en/stable/>`_
Python module.

Submission
----------

* For **residential students**, please have this ready on your GitHub
  accounts by class time on Monday, February 20th. We will pick
  students at random to demonstrate their solutions.

* For **online students**, you don't need to submit anything to
  us. However, we still strongly encourage you to do these
  exercises. They will help you get up to speed in Python if you're
  not familiar with it; or if you are, they might introduce you to
  some modules that you haven't used before. Of course, if you have
  any questions about the exercises, please discuss them with the AIs
  during office hours or on Piazza.
