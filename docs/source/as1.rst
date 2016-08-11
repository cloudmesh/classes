Homework H4: Get your software set up for later lectures and final project
===============================================================================

.. Homework HW4 (FirstProgram)
.. ===============================================================================

In this homework, you are expected to run Python or Java programs on
FutureSystems or on your local machine. A few examples for beginners will help
you to understand how to write and run Java or Python programs on your
environment.

.. comment::

  .. sidebar:: Page Contents

   .. contents::
         :local:

Setup
-------------------------------------------------------------------------------

Java and Python are installed on our cloud as explained in Unit 11. Here you
choose between Python on your laptop, Python in cloud or Java in cloud.

Local Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download Enthought Canopy Express (free) from
https://store.enthought.com/downloads/ including NumPy SciPy Matplotlib

Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set up Python in cloud or Java in cloud. `See Unit 11
<http://openedx.scholargrid.org/courses/SoIC/INFO590/FALL_2015/courseware/3cf90e09c7bf439fa97fda2fbdcce8fe/6cc23f2c65194720ab5fb8d339bda0b8/>`_.

First Program
-------------------------------------------------------------------------------

This code explains how to display a simple string on your screen. You can
download or write your own code using your editor.

Java
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Download: FirstProgram.java <https://raw.githubusercontent.com/cglmoocs/bdaafall2015/master/JavaFiles/FirstProgram.java>`_

.. code-block:: java

  /**
  * Sample Program to print out a message
  * 
  * Compile : javac FirstProgram.java
  * 	Run    : java FirstProgram
  */
  public class FirstProgram {	
  	public static void main(String[] args){
		  System.out.println("My first program on Big Data Applications and Analytics!");
	  }
  }

This example prints out the message on your screen by ``println`` method in the
``System`` class.  In Java Programming, you need to complie your code to
execute.

Compiling and Execution
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::
  
  javac FirstProgram.java
   
Now, you will have FirstProgram.class file on your system. Java Compiler
(javac) creates Java bytecode with a ``.class`` extension. We will execute the
class file with ``java`` command.

::

  java FirstProgram
  My first program on Big Data Applications and Analytics!


Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's write a same program in Python.

`Download: FirstProgram.py <https://raw.githubusercontent.com/cglmoocs/bdaafall2015/master/PythonFiles/FirstProgram.py>`_

.. code-block:: python

   # Run python FirstProgram.py
   print 'My first program on Big Data Applications and Analytics!'
   
Python function ``print`` simply displays a message on your screen. Compiling
is not necessary in Python. You can run your code directly with ``python``
command.

::

   python FirstProgram.py
   My first program on Big Data Applications and Analytics!
   

Display System Information
-------------------------------------------------------------------------------

This is an extension of your first program. We will lean how to import functions
and use them to get system information like hostname or username.

Java
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We now understand how to print out a message using Python or Java. System
information such as time, date, user name or hostname (machine name) can be
displayed as well with built-in functions in each language.

`Download: FirstProgramWithSystemInfo.java <https://raw.githubusercontent.com/cglmoocs/bdaafall2015/master/JavaFiles/FirstProgramWithSystemInfo.java>`_

.. code-block:: java

   import java.util.Date;
   import java.text.DateFormat;
   import java.text.SimpleDateFormat;
   import java.net.InetAddress;
   import java.net.UnknownHostException;

   /**
    *  * Sample Program with system information
    *  *
    *  * Compile : javac FirstProgramWithSystemInfo.java
    *  *   Run    : java FirstProgramWithSystemInfo
    *  */
   public class FirstProgramWithSystemInfo {
           public static void main(String[] args){
   
                   System.out.println("My first program with System Information!");
   
                   // Print Date with Time
                   DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
                   Date date = new Date();
                   System.out.println("Today is: " + dateFormat.format(date));
                   // Print Username
                   System.out.println("Username is: " + System.getProperty("user.name"));
                   // Print hostname
                   try {
                           java.net.InetAddress localMachine = java.net.InetAddress.getLocalHost();
                           System.out.println("Hostname is: " + localMachine.getHostName());
                   } catch (UnknownHostException e) {
                           e.printStackTrace();
                           System.out.println("No host name: " + e.getMessage());
                   }
           }
   }

Compiling and Execution
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

    javac FirstProgramWithSystemInfo.java
    
::
 
    java FirstProgramWithSystemInfo
    My first program with System Information!
    Today is: 2015/01/01 18:54:10
    Username is: albert
    Hostname is: bigdata-host


Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Download FirstProgramWithSystemInfo.py <https://raw.githubusercontent.com/cglmoocs/bdaafall2015/master/PythonFiles/FirstProgramWithSystemInfo.py>`_

.. code-block:: python

   from datetime import datetime
   import getpass
   import socket

   # Run python FirstProgramWithSystemInfo.py
   print ('My first program with System Information!')

   print ("Today is: " + str(datetime.now()))
   print ("Username is: " + getpass.getuser())
   print ("Hostname is: " + socket.gethostname())

Execution
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

   python  FirstProgramWithSystemInfo.py
   My first program with System Information!
   Today is: 2015-01-01 18:58:10.937227
   Username is: albert
   Hostname is: bigdata-host
   
Submission of HW4
-------------------------------------------------------------------------------

**Submit these compiled files or screenshot image files to** `IU Canvas <canvas.iu.edu>`_

[Java]

* **FirstProgram.class or a screenshot image of the 'FirstProgram' execution (25%) **
* **FirstProgramWithSystemInfo.class or a screenshot image of the 'FirstProgramWithSystemInfo' execution (25%)**

[Python]

* FirstProgram.pyc or a screenshot image of the 'FirstProgram' execution (25%)
   - run ``python -m compileall FirstProgram.py`` to generate ``FirstProgram.pyc``
* FirstProgramWithSystemInfo.pyc or a screenshot image of the 'FirstProgramWithSystemInfo' execution (25%)
   - run ``python -m compileall FirstProgramWithSystemInfo.py`` to generate ``FirstProgramWithSystemInfo.pyc``


Challenge tasks
-------------------------------------------------------------------------------

* Run any Java or Python on a FutureSystems OpenStack instance
   - Submit screenshot images of your terminal executing Java or Python code on FutureSystems
* Run `NumPyTutorial <https://raw.githubusercontent.com/cglmoocs/bdaafall2015/master/IPythonFiles/NumPyTutorial.ipynb>`_ Python on IPython Notebook
   - Submit screentshot images of your web browser executing NumPyTutorial on FutureSystems
* **Tips: See** `tutorials for Big Data Applications and Analytics Shell on FutureSystems <http://cloudmesh.github.io/introduction_to_cloud_computing/class/cm-mooc/index.html>`_

Preview Course Examples
-------------------------------------------------------------------------------

* The Elusive Mr.Higgs [`Java <https://github.com/cglmoocs/bdaafall2015/tree/master/JavaFiles/Section-4_Physics-Units-9-10-11/Unit-9_The-Elusive-Mr.Higgs>`_][`Python <https://github.com/cglmoocs/bdaafall2015/tree/master/PythonFiles/Section-4_Physics-Units-9-10-11/Unit-9_The-Elusive-Mr.-Higgs>`_]
* Number Theory [`Python <https://github.com/cglmoocs/bdaafall2015/tree/master/PythonFiles/Section-4_Physics-Units-9-10-11/Unit-10_Number-Theory>`_]
* Calculated Dice Roll [`Java <https://github.com/cglmoocs/bdaafall2015/tree/master/JavaFiles/Section-4_Physics-Units-9-10-11/Unit-11_A-Calculated-Dice-Roll>`_][`Python <https://github.com/cglmoocs/bdaafall2015/tree/master/PythonFiles/Section-4_Physics-Units-9-10-11/Unit-11_A-Calculated-Dice-Roll>`_]
* KNN [`Java <https://github.com/cglmoocs/bdaafall2015/tree/master/JavaFiles/Section_7_Unit_19/KNN>`_][`Python <https://github.com/cglmoocs/bdaafall2015/tree/master/PythonFiles/Section%205%20e-Commerce%20Unit%2015_%20K'th%20Nearest%20Neighbor/knn>`_]

* PageRank [`Java <https://github.com/cglmoocs/bdaafall2015/tree/master/JavaFiles/Unit-27_PageRank>`_][`Python <https://github.com/cglmoocs/bdaafall2015/tree/master/PythonFiles/Unit%2019_%20PageRank/Page-Rank>`_]
* KMeans [`Java <https://github.com/cglmoocs/bdaafall2015/tree/master/JavaFiles/Unit-28_KMeans>`_][`Python <https://github.com/cglmoocs/bdaafall2015/tree/master/PythonFiles/Unit%2016_%20Kmeans-%20Software/K-Means>`_]

