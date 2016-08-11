Programming Assignments
======================================================================

.. sidebar:: Page Contents

.. contents::
   :local:

HOMEWORK H4: GET YOUR SOFTWARE SET UP FOR LATER
----------------------------------------------------------------------

First some background: You will need modest software for some of
lectures and homeworks. This can be most easily done in Python but
Java is also possible; no other languages are relevant. You MIGHT use
software in final project. Note the final project will be individual
or up to a three person team and can either be a significant PAPER or
a SOFTWARE PROJECT. We can support Software in Java on clouds or
Python but other software such as R allowed in final project Your team
chooses. You can find sample software and paper projects. See Chapter
Two: Sample Project.

Preparing Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Java and Python are installed on our cloud as explained in Unit 11.
Here you choose between Python on your laptop, Python in cloud or Java
in cloud.

• DO - Install a Python environment on your system. You need:

  - `Python <https://www.python.org/`_ 
  - `NumPy <http://www.numpy.org/`_
  - `SciPy <https://scipy.org/`_
  - `Matplotlib <http://matplotlib.org/>`_
  - `Pandas <http://pandas.pydata.org/`_

  We do not recommend Enthought Canopy of Continuum Anaconda for this.

• OR - Set up Python in cloud or Java in cloud. See Unit 11.

Tasks
~~~~~~~~~

Submit results to show your software is set up and running. Solve
tasks following instructions. See Chapter Three Homework HW4
(FirstProgram).

• Submit your Java OR Python program results to IU Canvas

Discussion D5
~~~~~~~~~~~~~

Use Slack and post at least one discussion post to discuss final
project you want to do and look for team members if that’s what you
want. 


Software projects will involve running an analysis on a data set. You
will be provided with a Hadoop cluster running MapReduce version 1
(see HadoopClusterAccess.html). Your goal will be to use the Hadoop
cluster to run a “Big Data” computation. One possible approach is the
Terabyte Sort procedure. The components are:

• TeraGen: create the data
• TeraSort: analyze the data using MapReduce
• TeraValidate: validation of the output
  
Invocation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The teragen command accepts two parameters:

* number of 100-byte rows
* the output directory

::

   hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.1.jar
   teragen $COUNT /user/$USER/tera-gen
   hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.1.jar
   terasort /user/$USER/tera-gen /user/$USER/tera-sort
   hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.1.jar
   teravalidate /user/$USER/tera-sort /user/$USER/tera-validate

Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the Terabyte Sort procedure for various sizes of data:

• 1 GB
• 10 GB
• 100 GB

For each component (tera{gen,sort,validate}), report the execution
time, data read and written (in GB) as well as the cumulative values.

Sample Software Project
----------------------------------------------------------------------

The following are projects from previous classes:

Paper

• Review of Recommender Systems: technology & applications
• Review of Big Data in Bioinformatics
• Review of Data visualization including high dimensional data
• Design of a NoSQL database for a specialized application

Software

• Use R to analyze a particular dataset (business or sports)


Chapter 3. Previous Projects
----------------------------------------------------------------------

In this homework, you are expected to run Python or Java programs on
FutureSystems or on your local machine. A few examples for beginners
will help you to understand how to write and run Java or Python
programs on your environment.

First Program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This code explains how to display a simple string on your screen. You
can download or write your own code using your editor.

Java
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download: FirstProgram.java

::
   /**
     * Sample Program to print out a message
     *
     * Compile : javac FirstProgram.java
     * Run : java FirstProgram
   */
   public class FirstProgram {
      public static void main(String[] args){
            System.out.println("My first program on Big Data Applications and Analytics!");
	 }
   }

This example prints out the message on your screen by println method
in the System class. In Java Programming, you need to complie your
code to execute. Compiling and Execution::

  javac FirstProgram.java

Now, you will have FirstProgram.class file on your system. Java
Compiler (javac) creates Java bytecode with a .class extension. We
will execute the class file with java command::

  java FirstProgram

My first program on Big Data Applications and Analytics!


Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let’s write a same program in Python.

Create the following program: FirstProgram.py::

  # Run python FirstProgram.py
  print ’My first program on Big Data Applications and Analytics!’


Python function print simply displays a message on your screen.
Compiling is not necessary in Python. You can run your code directly
with python command.::

  python FirstProgram.py

My first program on Big Data Applications and Analytics!


First Program with system information
----------------------------------------------------------------------

Java
~~~~~~~~~~~
We now understand how to print out a message using Python or Java. System information such as time, date, user
name or hostname (machine name) can be displayed as well with built-in functions in each language.
Download: FirstProgramWithSystemInfo.java::

    import java.util.Date;
    import java.text.DateFormat;
    import java.text.SimpleDateFormat;
    import java.net.InetAddress;
    import java.net.UnknownHostException;
    /**
    * * Sample Program with system information
    * *
    * * Compile : javac FirstProgramWithSystemInfo.java
    * * Run : java FirstProgramWithSystemInfo
    * */
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


Compiling and Execution::

    javac FirstProgramWithSystemInfo.java
    java FirstProgramWithSystemInfo

    My first program with System Information!

    Today is: 2015/01/01 18:54:10
    Username is: albert
    Hostname is: bigdata-host

Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download FirstProgramWithSystemInfo.py::

    from datetime import datetime
    import getpass
    import socket
    # Run python FirstProgramWithSystemInfo.py
    print (’My first program with System Information!’)
    print ("Today is: " + str(datetime.now()))
    print ("Username is: " + getpass.getuser())
    print ("Hostname is: " + socket.gethostname())
    Execution
    python FirstProgramWithSystemInfo.py
    My first program with System Information!
    Today is: 2015-01-01 18:58:10.937227
    Username is: albert
    Hostname is: bigdata-host


Submission of HW4
----------------------

Java
------

• FirstProgram.class or a screenshot image of the ‘FirstProgram’
  execution (25%)
• FirstProgramWithSystemInfo.class or a screenshot image of the
  ‘FirstProgramWithSystemInfo’ execution (25%)

Python
--------

• FirstProgram.pyc or a screenshot image of the ‘FirstProgram’
  execution (25%). Run::

     python -m compileall FirstProgram.py

  to generate FirstProgram.pyc

• FirstProgramWithSystemInfo.pyc or a screenshot image of the
  ‘FirstProgramWithSystemInfo’ execution (25%). Run

  – run python -m compileall FirstProgramWithSystemInfo.py

  to generate FirstProgramWithSystemInfo.pyc

• Submit these files or image files to IU Canvas

4.3. Submission of HW4 11
----------------------------------------------------------------------

Homework HW4 and Sample Software Projects

Challenge tasks
----------------------------------------------------------------------

• Run any Java or Python on a FutureSystems OpenStack instance
  
  * Submit screenshot images of your terminal executing Java or Python code on FutureSystems

• Run NumPyTutorial Python on IPython Notebook

  * Submit screentshot images of your web browser executing NumPyTutorial on FutureSystems

• Tips: See tutorials for Big Data Applications and Analytics Shell on FutureSystems

Preview Course Examples
----------------------------------------------------------------------

• The Elusive Mr.Higgs [Java][Python]
• Number Theory [Python]
• Calculated Dice Roll [Java][Python]
• KNN [Java][Python]
• PageRank [Java][Python]
• KMeans [Java][Python]

HADOOP CLUSTER ACCESS
----------------------------------------------------------------------

This document describes getting access to the Hadoop cluster for the course.

Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will need

1. An a account with FutureSystems
2. To be a member of FutureSystems project 475
3. Have uploaded an ssh key to the portal

Access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The cluster frontend is located at <IP_ADDRESS> Login using ssh::

  ssh -i $PATH_TO_SSH_PUBLIC_KEY $PORTAL_USERNAME@$HADOOP_IP

In the above:

• $PATH_TO_SSH_PUBLIC_KEY is the location of the public key that has
  been added to the futuresystems portal
• $PORTAL_USERNAME is the username on the futuresystems portal
• $HADOOP_IP is the IP address of the hadoop frontend node

Usage
---------

Hadoop is installed under /opt/hadoop, and you can refer to this
location using $HADOOP_HOME. See::

  hadoop fs

and::

  hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples*.jar

for more details.
