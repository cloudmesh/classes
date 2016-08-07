Introduction
----------------------------------------------------------------------


----------------------------------------------------------------------
Variables, Expressions, and Statements
----------------------------------------------------------------------
Variables in Python can hold text and numbers. For example:

.. code:: python

    x = 2
    price = 2.5
    word = 'Hello'

The variable names are on the left and the values on the right. Once a variable is assigned, it can be used in other places of the program.
In the example above, we have three variables: x, price and word. Variables may not contain spaces or special characters. 
Text variables may be defined in 3 ways:

.. code:: python
    
    word = 'Hello'
    word = "Hello"
    word = '''Hello'''


The type depends on what you prefer.  Once defined variables can be replaced or modified:

.. code:: python

    x = 2

    # increase x by one
    x = x + 1

    # replace x
    x = 5

Python supports the operators +, -, / and * as well as brackets.  Variables may be shown on the screen using the print statement.

.. code:: python

    x = 5
    print(x)

    y = 3 * x
    print(y)

    # more detailed output
    print("x = " + str(x))
    print("y = " + str(y))

The first output of the program above is simply the raw value of the variables. If you want to print a more detailed message like “x = 5”, use the line ‘print(“x = ” + str(x))’. This str() function converts the numeric variable to text.

----------------------------------------------------------------------
Control Statements
----------------------------------------------------------------------
Computer programs do not only execute instructions. Occasionally, a choice needs to be made. Such as a choice is based on a condition. Python has several conditional operators:


.. code:: python

    >   greater than
    <   smaller than
    ==  equals
    !=  is not

Conditions are always combined with variables. A program can make a choice using the if keyword. For example:

.. code:: python
    
    x = int(input("Tell X"))
    if x == 4:
        print('You guessed correctly!')
    print('End of program.')


When you execute this program it will always print ‘End of program’, but the text ‘You guessed correctly!’ will only be printed if the variable x equals to four (see table above). Python can also execute a block of code if x does not equal to 4. The else keyword is used for that.


.. code:: python

    x = int(input("Tell X"))

    if x == 4:
        print('You guessed correctly!')
    else:
        print('Wrong guess')

    print('End of program.')

----------------------------------------------------------------------
Iterations
----------------------------------------------------------------------

To repeat code, the for keyword can be used. To execute a line of code 10 times we can do:

.. code:: python

    for i in range(1,11):
        print(i)

The last number (11) is not included. This will output the numbers 1 to 10. Python itself starts counting from 0, so this code will also work:

.. code:: python
    
    for i in range(0,10):
        print(i)

but will output 0 to 9.


The code is repeated while the condition is True. In this case the condition is: i < 10. Every iteration (round), the variable i is updated.Nested loops
Loops can be combined:

.. code:: python
    
    for i in range(0,10):
        for j in range(0,10):
            print(i,' ',j)

In this case we have a multidimensional loops. It will iterate over the entire coordinate range (0,0) to (9,9)

----------------------------------------------------------------------
Functions
----------------------------------------------------------------------


To repeat lines of code, you can use a function. A function has a unique distinct name in the program. Once you call a function it will execute one or more lines of codes, which we will call a code block.

.. code:: python
    import math

    def computePower(a):
        value = math.pow(a,2)
        print(value)

computePower(3)


We call the function with parameter a=3 .  A function can be called several times with varying parameters. There is no limit to the number of function calls.

The def keyword tells Python we define a function.  Always use four spaces to indent the code block, using another number of spaces will throw a syntax error.

It is also possible to store the output of a function in a variable.  To do so, we use the keyword return.

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
* http://www.numpy.org/
* https://www.scipy.org/
* http://matplotlib.org/

