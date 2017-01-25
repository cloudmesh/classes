.. add info about DataFu

The Apache DataFu project was created out of the need for stable ,
well-tested libraries for large scale data processing in Hadoop.
As detailed in :cite:`www-DataFu` Apache DatFu consists of two
libraries Apache DataFu Pig and Apache DataFu Hourglass.  Apache
DataFu Pig is a collection of useful user-defined functions for
data analysis in Apache Pig. The functions are in areas of
Statistics, Bag Operations, Set Operations, Sessions, Sampling,
Estimation, Hashing and Link Analysis.  Apache DataFu Hourglass is
a library for incrementally processing data using Hadoop
MapReduce. It is designed to make computations over sliding windows
more efficient. For these types of computations, the input data is
partitioned in some way, usually according to time, and the range
of input data to process is adjusted as new data arrives.
Hourglass works with input data that is partitioned by day, as
this is a common scheme for partitioning temporal data.

