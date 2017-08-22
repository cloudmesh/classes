Technology for Big Data Applications and Analytics
----------------------------------------------------------------------

We use the K-means Python code in SciPy package to show real
code for clustering. After a simple example we generate 4 clusters of
distinct centers and various choice for sizes using Matplotlib tor
visualization. We show results can sometimes be incorrect and
sometimes make different choices among comparable solutions. We
discuss the ''hill'' between different solutions and rationale for
running K-means many times and choosing best answer. Then we introduce
MapReduce with the basic architecture and a homely example. The
discussion of advanced topics includes an extension to Iterative
MapReduce from Indiana University called Twister and a generalized Map
Collective model. Some measurements of parallel performance are
given. The SciPy K-means code is modified to support a MapReduce
execution style. This illustrates the key ideas of mappers and
reducers. With appropriate runtime this code would run in parallel but
here the *parallel* maps run sequentially. This simple 2 map version
can be generalized to scalable parallelism. Python is used to
Calculate PageRank from Web Linkage Matrix showing several different
formulations of the basic matrix equations to finding leading
eigenvector. The unit is concluded by a calculation of PageRank for
general web pages by extracting the secret from Google.


Technologypi: K-means 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use the K-means Python code in SciPy package to show real
code for clustering. After a simple example we generate 4 clusters of
distinct centers and various choice for sizes using Matplotlib tor
visualization. We show results can sometimes be incorrect and
sometimes make different choices among comparable solutions. We
discuss the *hill* between different solutions and rationale for
running K-means many times and choosing best answer.

.. todo:: The slides or videos are going to be updated

          Slides: https://iu.app.box.com/s/ltgbehfjwvgh40l5d3w8



Files:

* :download:`xmean.py </files/python/k_means/xmean.py>`
* :download:`sample.csv </files/python/k_means/sample.csv>`
* :download:`parallel_kmeans.py </files/python/k_means/parallel_kmeans.py>`
* :download:`kmeans_extra.py </files/python/k_means/kmeans_extra.py>`

K-means in Python
"""""""""""""""""

We use the K-means Python code in SciPy package to show real
code for clustering and applies it a set of 85 two dimensional vectors
-- officially sets of weights and heights to be clustered to find
T-shirt sizes. We run through Python code with Matplotlib displays to
divide into 2-5 clusters. Then we discuss Python to generate 4
clusters of varying sizes and centered at corners of a square in two
dimensions. We formally give the K means algorithm better than before
and make definition consistent with code in SciPy.

.. todo:: The slides or videos are going to be updated

          Video: https://youtu.be/I79ISV6XBbE



Analysis of 4 Artificial Clusters 
"""""""""""""""""""""""""""""""""""

We present clustering results on the artificial set of 1000 2D points
described in previous lesson for 3 choices of cluster sizes *small*
*large* and *very large*. We emphasize the SciPy always does 20
independent K means and takes the best result -- an approach to
avoiding local minima. We allow this number of independent runs to be
changed and in particular set to 1 to generate more interesting
erratic results. We define changes in our new K means code that also
has two measures of quality allowed. The slides give many results of
clustering into 2 4 6 and 8 clusters (there were only 4 real
clusters). We show that the *very small* case has two very different
solutions when clustered into two clusters and use this to discuss
functions with multiple minima and a hill between them. The lesson has
both discussion of already produced results in slides and interactive
use of Python for new runs.

.. todo:: The slides or videos are going to be updated
          
          Video 1: https://youtu.be/Srgq9VDg4C8

          Video 2: https://youtu.be/rjyAXjA_mOk

          Video 3: https://youtu.be/N6QKyrhNVAc



Technology: MapReduce
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


We describe the basic architecture of MapReduce and a homely
example. The discussion of advanced topics includes extension to
Iterative MapReduce from Indiana University called Twister and a
generalized Map Collective model. Some measurements of parallel
performance are given.

.. todo:: The slides or videos are going to be updated
          
          Slides: https://iu.app.box.com/s/hqykdx1bquez7ers3d1j


Introduction
""""""""""""

This introduction uses an analogy to making fruit punch by slicing and
blending fruit to illustrate MapReduce. The formal structure of
MapReduce and Iterative MapReduce is presented with parallel data
flowing from disks through multiple Map and Reduce phases to be
inspected by the user.

.. todo:: The slides or videos are going to be updated
          
          Video: https://youtu.be/67qFY64aj7g


Advanced Topics
"""""""""""""""""

This defines 4 types of MapReduce and the Map Collective model of
Qiu. The Iterative MapReduce model from Indiana University called
Twister is described and a few performance measurements on Microsoft
Azure are presented.

.. todo:: The slides or videos are going to be updated
          
          Video 1: https://youtu.be/lo4movzSyVw

          Video 2: https://youtu.be/wnanWncQBow


Technology: Kmeans and MapReduce Parallelism
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


We modify the SciPy K-means code to support a MapReduce
execution style and runs it in this short unit. This illustrates the
key ideas of mappers and reducers. With appropriate runtime this code
would run in parallel but here the *parallel* maps run
sequentially. We stress that this simple 2 map version can be
generalized to scalable parallelism.


.. todo:: The slides or videos are going to be updated

          Slides: https://iu.app.box.com/s/zc9pckhyehn0cog8wy19



Files:

* :download:`ParallelKmeans </files/python/k_means/parallel_kmeans.py>`

MapReduce Kmeans in Python 
""""""""""""""""""""""""""""

We modify the SciPy K-means code to support a MapReduce
execution style and runs it in this short unit. This illustrates the
key ideas of mappers and reducers. With appropriate runtime this code
would run in parallel but here the *parallel* maps run
sequentially. We stress that this simple 2 map version can be
generalized to scalable parallelism.

.. todo:: The slides or videos are going to be updated
          
          Video 1: https://youtu.be/2El1oL3gKpQ

          Video 2: https://youtu.be/LLrTWWdE3T0


Technology: PageRank 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use Python to Calculate PageRank from Web Linkage Matrix
showing several different formulations of the basic matrix equations
to finding leading eigenvector. The unit is concluded by a calculation
of PageRank for general web pages by extracting the secret from
Google.

.. todo:: The slides or videos are going to be updated
          
          Slides: https://iu.app.box.com/s/gwq1qp0kmwbvilo0kjqq

Files:

* :download:`pagerank1.py </files/python/page_rank/pagerank1.py>`
* :download:`pagerank2.py </files/python/page_rank/pagerank2.py>`


Calculate PageRank from Web Linkage Matrix I
""""""""""""""""""""""""""""""""""""""""""""

We take two simple matrices for 6 and 8 web sites respectively
to illustrate the calculation of PageRank.

.. todo:: The slides or videos are going to be updated
          
          Video 1: https://youtu.be/rLWUvvcHrCQ

          Video 2: https://youtu.be/UzQRukCFQv8



Calculate PageRank of a real page
"""""""""""""""""""""""""""""""""

This tiny lesson presents a Python code that finds the Page Rank that
Google calculates for any page on the web.

.. todo:: The slides or videos are going to be updated
          
          Video: https://youtu.be/8L_72bRLQVk


