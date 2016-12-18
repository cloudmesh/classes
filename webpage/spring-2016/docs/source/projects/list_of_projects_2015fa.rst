.. _ref-2015-fall-list-of-projects:

List of Project 2015 Fall (In Progress)
===============================================================================

Note that these are some of students projects from one of Big Data courses.
These are reference only.

.. csv-table:: 2015 Fall Suggested Projects
   :header: Title, Data set, Software, Category

        "`NIST Fingerprint <http://www.nist.gov/itl/iad/ig/nbis.cfm>`_ (a subset of): NFIQ PCASYS MINDTCT BOZORTH3 NFSEG SIVV",NIST Special Database 27A `[4GB] <http://www.nist.gov/itl/iad/ig/sd27a.cfm>`_,NIST Biometric Image Software (NBIS) `v5.0 <http://nigos.nist.gov:8080/nist/nbis/nbis_v5_0_0.zip>`_ [`userguide <http://www.nist.gov/customcf/get_pdf.cfm?pub_id=51097>`_],Batch Data Analytics
        Hadoop Benchmark (each) - TeraSort Suite,Teragen,hadoop-examples.jar,Batch Data Analytics
        Hadoop Benchmark (each) - DFSIO (HDFS Performance),,hadoop-mapreduce-client-jobclient,Batch Data Analytics
        Hadoop Benchmark (each) - NNBench (NameNode Perf.),,hadoop-mapreduce-client-jobclient,Batch Data Analytics
        Hadoop Benchmark (each) - MRBench (MapReduce Perf.),,src/test/org/apache/hadoop/mapred/MRBench.java,Batch Data Analytics
        Stock Data Analysis with MPI,"`CRSP <https://wrds-web.wharton.upenn.edu/wrds/>`_",`Stock Analysis <https://github.com/iotcloud/stock-analysis>`_,Streaming Data Analytics

.. csv-table:: 2015 Fall
   :header: Id,Title,Technology*,User Interface Language,Backend Environment**,Dataset
   :widths: 5 10 10 5 10 10

        1,Time series visualization of stock data,MPI,Java,"MPI, SLURM",CRSP US Stock from WRDS
        2,San Francisco’s Most Dangerous Crime Areas,scikit-learn,Python,SQL (pandasql),SF OpenData - SFPD Incidents
        3,"Houston, TX Crime Data Analysis 2014",Postgresql,Python,SQL (Postgres),"Crime Statistics - City of Houston, Texas"
        4,Twitter Live Feed Analysis and Storage in MongoDB,IPython Notebook; seaborn,Python,NoSQL (MongoDB),Twitter
        5,Twitter Sentiment Analysis of US Presidential Election,Hadoop; Datumbox; Tableau ,Python,"Hadoop; HBase",Twitter
        6,Amazon movie reviews,"IPython Notebook; Spark",Python,Spark,Amazon Movie Data
        7,Stock Market Analysis,scikit-learn;hadoop ,Python, hadoop ,WRDS CRSP data
        8,Twitter User Data Analysis,"MongoDB;D3;jQuery",javascript,NoSQL (MongoDB),Twitter
        9,Twitter Dataset Analysis and Modeling,"MongoDB;pymongo",Python,NoSQL (MongoDB),Twitter


.. comment::

        22,Hibench,Hadoop,Java,Hadoop,
        23,Design of a NoSQL Database using MongoDB and Cassandra for Big Data,"MongoDB
        Cassandra",Java,"NoSQL (MongoDB, Cassandra)",
        24,"Kaggle Titanic Survivor Prediction: Comparison of
        Machine Learning Methods
        ","dplyr
        ggplot2
        glm2
        caret
        rpart
        rattle
        rpart.plot
        RColorBrewer
        randomForest",R,csv (text file),Kaggle.com
        25,Chicago Crime,"Tableau
        Google Earth API
        Google Geolocation API",xml,csv (text file),City of Chicago
        26,Sentiment Analysis in Movie Reviews using Naive Bayes Algorithm,"IPython Notebook
        Numpy
        Pandas
        scikit-learn
        matplotlib",Python,csv (text file),Movie Reviews - Rotten Tomatos
        27,Final project: Crimes of Chicago,"IPython Notebook
        Pandas
        Matplotlib
        Folium
        sqlite",Python,csv (text file),City of Chicago
        28,Designing Perfrect Wine,"numpy
        scipy
        pandas
        sklearn
        seaborn
        matplotlib ",Python,csv (text file),"University of California, Irvine"
        29,From LAS to DEM: Large-scale lidar terrain processing,"LAStools : las2txt and mergelas
        Numpy
        Karst at IU
        laspy",Python,"TORQUE,
        LAStools (C++)",Indiana Lidar from SDSC
        30,"Predictive Analysis of Stock Price Using
        Random Forest Algorithm",Tableau,Python,csv (text file),"LIBOR Rates from St. Louis, 
        VIX from Quandl.com, 
        Stock Price from Yahoo Finance"
        31,Final project: Evaluation of Spark/MLLib ,"Spark
        MLLib 

        Hortonworks Sandbox with Spark
        Oracle Virtualbox on laptop",Python,Spark / Scala,"Hubway Bike, 
        Titanic survival data from Kaggle, 
        Movie reviews from MovieLens 1m"
        32,Twitter Social Media Analytics,RStudio,R,rdata file,Twitter from rdatamining.com
        33,Analysis of Malware Connections to Command and Control Servers,"Splunk for PCAP analyzer
        pygeoip - Pure Python GeoIP API
        dpkt - Python TCP/IP tool
        Hadoop
        Cloudera",Python,Hadoop,GeoIP from maxmind.com
        34,Movie and Product Reviews,"matplotlib
        NLTK
        Numpy
        gSplit",Python,"txt (text file)
        ",SNAP - Stanford Network Analysis Project
        35,"Prediction of whether a
        Customer would get a new credit card
        ","corrplot
        mlbench
        caret
        class
        randomforest
        MASS
        Deducer
        C50
        e1071
        ggplot2",R,csv (text file),
        36,Recommendation Algorithm on Yelp,"NLTK
        sklearn - svm","Python, R",csv (text file),Yelp Dataset
        37,Twitter Sentiment Analysis using Cloudmesh,"Cloudmesh
        Hadoopy: Hadoopy: Python wrapper for Hadoop using Cython
        Indico API - IndicoIo: machine learning toolkits including sentiment analysis
        Bootstrap.js
        Google Charts",Python,Hadoop,Twitter
        38,Final project: Tennis Data,"Apache POI
        JFreeChart",Java,xlsx (MS Excel file),ATP Tennis Data
        39,Analysis of baseball data for performance measure and prediction,"Plotly
        ggplot2",R,"csv (text file)
        Hadoop (planned)","Lahman’s data set, 
        PITCHfx data set, 
        Retrosheet"
        40,Final project: Network among Chinese Foundations,NetworkX: complex networks,SPSS 22,csv (text file),China Foundations
        41,"Restaurant Recommendation System
        ","MongoDB
        Tkinter
        pymongo",Python,csv (text file),Yelp Dataset
        42,Airline Delays,"Matplotlib
        Numpy
        Seaborn
        Pandas",Python,csv (text file),Statistical Computing
        43,"Online News Popularity
        ","RStudio
        Eclipse IDE","Java,
        R",csv (text file),UCI Machine Learning Repository
        44,Analysis of Yelp Dataset Review,"MongoDB
        Eclipse IDE
        Apache Lucene
        Apache Commons",Java,NoSQL (MongoDB),Yelp Dataset
        45,Flight Delay Prediction,"Pig
        scikit-learn",Python,Pig,"bts.gov, 
        noaa.gov"
        ,,,,,
        ,"* Technology includes Tools, Libraries, APIs
        ** Backend environment includes job scheduler, dabase or framework for Big Data Processing",,,,
        ,,,,,
        ,"* These technologies and datasets are surveyed:
        1) from students written report
        2) from students source code (import packages)",,,,
