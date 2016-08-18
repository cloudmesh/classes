Additional Programming Assignments
----------------------------------------------------------------------

Programming: Hadoop Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will be provided with a Hadoop cluster running MapReduce. Your
goal will be to use the Hadoop cluster to run a “Big Data”
computation. One possible approach is the Terabyte Sort procedure. The
components are:

* TeraGen: create the data
* TeraSort: analyze the data using MapReduce
* TeraValidate: validation of the output

Access to the cluster
~~~~~~~~~~~~~~~~~~~~~

.. todo:: HadoopClusterAccess.html


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

* 1 GB
* 10 GB
* 100 GB

For each component (tera{gen,sort,validate}), report the execution
time, data read and written (in GB) as well as the cumulative values.


Programming: Using futuresystems.org
----------------------------------------------------------------------

In this homework, you are expected to run Python or Java programs on
FutureSystems or on your local machine. A few examples for beginners
will help you to understand how to write and run Java or Python
programs on your environment.

We will print some elementary system information such as time, date,
user name or hostname (machine name) which will be important when you
report on your infrastructure in your program reports. You will likely
need to add more information such as processor type, core number, and
frequency.


Java
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is a simple program in Java.


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
~~~~~~

Let’s write a simple program in Python.

Create the following program: FirstProgram.py::

    ############################################
    # Run python FirstProgram.py
    ############################################
    from datetime import datetime
    import getpass
    import socket
    ############################################    
    # Run python FirstProgramWithSystemInfo.py
    ############################################    
    print (’My first program with System Information!’)
    print ("Today is: " + str(datetime.now()))
    print ("Username is: " + getpass.getuser())
    print ("Hostname is: " + socket.gethostname())

    
Execution:

    Compiling is not necessary in Python. You can run your code
    directly with python command.::

      python FirstProgram.py

What does the output look like?:
    ::
   
        python FirstProgramWithSystemInfo.py
        My first program with System Information!
        Today is: 2015-01-01 18:58:10.937227
        Username is: albert
        Hostname is: bigdata-host
  
  
Challenge tasks
----------------------------------------------------------------------

* Run any Java or Python on a FutureSystems OpenStack instance
* Run NumPyTutorial Python on IPython Notebook


Preview Course Examples
----------------------------------------------------------------------

.. todo:: The links are missing
	  
* The Elusive Mr.Higgs [Java][Python]
* Number Theory [Python]
* Calculated Dice Roll [Java][Python]
* KNN [Java][Python]
* PageRank [Java][Python]
* KMeans [Java][Python]

Hadoop Cluster Access
----------------------------------------------------------------------

This document describes getting access to the Hadoop cluster for the course.

You will need

1. An a account with FutureSystems
2. To be a member of a active project on FutureSystems (fg511) 
3. Have uploaded an ssh key to the portal

Access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The cluster frontend is located at <IP_ADDRESS> Login using ssh::

  ssh -i $PATH_TO_SSH_PUBLIC_KEY $PORTAL_USERNAME@$HADOOP_IP

In the above:

* $PATH_TO_SSH_PUBLIC_KEY is the location of the public key that has
  been added to the futuresystems portal
* $PORTAL_USERNAME is the username on the futuresystems portal
* $HADOOP_IP is the IP address of the hadoop frontend node

Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hadoop is installed under /opt/hadoop, and you can refer to this
location using $HADOOP_HOME. See::

  hadoop fs

and::

  hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples*.jar
