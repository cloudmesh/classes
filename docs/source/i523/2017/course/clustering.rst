
.. _S10:

Technology Training - kNN & Clustering
----------------------------------------------------------------------

This section is meant to provide a discussion on the kth Nearest
Neighbor (kNN) algorithm and clustering using K-means. Python version
for kNN is discussed in the video and instructions for both Java and
Python are mentioned in the slides. Plotviz is used for generating 3D
visualizations.


Recommender Systems - K-Nearest Neighbors (Python & Java Track)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We discuss simple Python k Nearest Neighbor code and its
application to an artificial data set in 3 dimensions. Results are
visualized in Matplotlib in 2D and with Plotviz in 3D. The concept of
training and testing sets are introduced with training set
pre-labelled.

.. todo:: The slides or videos are going to be updated

          Slides: https://iu.app.box.com/s/i9et3dxnhr3qt5gn14bg

Files:

* :download:`kNN.py </files/python/knn/kNN.py>`
* :download:`kNN_Driver.py </files/python/knn/kNN_Driver.py>`
* :download:`DatingTesting2.txt  </files/python/knn/dating_test_set2.txt>`
* :download:`clusterFinal-M3-C3Dating-ReClustered.pviz </files/python/knn/clusterFinal-M3-C3Dating-ReClustered.pviz>`
* :download:`DatingRating-OriginalLabels.pviz </files/python/knn/dating_rating_original_labels.pviz>`
* :download:`clusterFinal-M30-C28.pviz </files/python/knn/clusterFinal-M30-C28.pviz>`


Python k'th Nearest Neighbor Algorithms I
"""""""""""""""""""""""""""""""""""""""""

This lesson considers the Python k Nearest Neighbor code found on the
web associated with a book by Harrington on Machine Learning. There
are two data sets. First we consider a set of 4 2D vectors divided
into two categories (clusters) and use k=3 Nearest Neighbor algorithm
to classify 3 test points. Second we consider a 3D dataset that has
already been classified and show how to normalize. In this lesson we
just use Matplotlib to give 2D plots.

.. todo:: The slides or videos are going to be updated
          
          Video 1: https://youtu.be/o16L0EqsQ_g

          Video 2: https://youtu.be/JK5p24mnTjs


3D Visualization
""""""""""""""""

The lesson modifies the online code to allow it to produce files
readable by PlotViz. We visualize already classified 3D set and rotate
in 3D.

.. todo:: The slides or videos are going to be updated
          
          Video: https://youtu.be/fLtH-ZI1Jqk


Testing k'th Nearest Neighbor Algorithms
""""""""""""""""""""""""""""""""""""""""

The lesson goes through an example of using k NN classification
algorithm by dividing dataset into 2 subsets. One is training set with
initial classification; the other is test point to be classified by
k=3 NN using training set. The code records fraction of points with a
different classification from that input. One can experiment with
different sizes of the two subsets. The Python implementation of
algorithm is analyzed in detail.

.. todo:: The slides or videos are going to be updated
          
          Video https://youtu.be/zLaPGMIQ9So

Clustering and heuristic methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use example of recommender system to discuss clustering. The
details of methods are not discussed but k-means based clustering
methods are used and their results examined in Plotviz. The original
labelling is compared to clustering results and extension to 28
clusters given. General issues in clustering are discussed including
local optima, the use of annealing to avoid this and value of
heuristic algorithms.


.. todo:: The slides or videos are going to be updated

          Slides: https://iu.app.box.com/s/70qn6d61oln9b50jqobl


Files:

* :download:`Fungi_LSU_3_15_to_3_26_zeroidx.pviz </files/python/plotviz/fungi_lsu_3_15_to_3_26_zeroidx.pviz>`
* :download:`DatingRating-OriginalLabels.pviz </files/python/plotviz/datingrating_originallabels.pviz>`
* :download:`clusterFinal-M30-C28.pviz </files/python/plotviz/clusterFinal-M30-C28.pviz>`
* :download:`clusterFinal-M3-C3Dating-ReClustered.pviz </files/python/plotviz/clusterfinal_m3_c3dating_reclustered.pviz>`



Kmeans Clustering
"""""""""""""""""

We introduce the k means algorithm in a gentle fashion and
describes its key features including dangers of local minima. A simple
example from Wikipedia is examined.


.. todo:: The slides or videos are going to be updated
          
          Video: https://youtu.be/3KTNJ0Okrqs


Clustering of Recommender System Example
""""""""""""""""""""""""""""""""""""""""

Plotviz is used to examine and compare the original classification
with an ''optimal'' clustering into 3 clusters using a fancy
deterministic annealing method that is similar to k means. The new
clustering has centers marked.

.. todo:: The slides or videos are going to be updated
          
          Video: https://youtu.be/yl_KZ86NT-A


Clustering of Recommender Example into more than 3 Clusters
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The previous division into 3 clusters is compared into a clustering
into 28 separate clusters that are naturally smaller in size and
divide 3D space covered by 1000 points into compact geometrically
local regions.

.. todo:: The slides or videos are going to be updated
          
          Video: https://youtu.be/JWZmh48l0cw



Local Optima in Clustering
""""""""""""""""""""""""""

This lesson introduces some general principles. First many important
processes are ''just'' optimization problems. Most such problems are
rife with local optima. The key idea behind annealing to avoid local
optima is described. The pervasive greedy optimization method is
described.

.. todo:: The slides or videos are going to be updated
          
          Video: https://youtu.be/Zmq8O_axCmc


Clustering in General
"""""""""""""""""""""

The two different applications of clustering are described. First find
geometrically distinct regions and secondly divide spaces into
geometrically compact regions that may have no ''thin air'' between
them. Generalizations such as mixture models and latent factor methods
are just mentioned. The important distinction between applications in
vector spaces and those where only inter-point distances are defined
is described. Examples are then given using PlotViz from 2D clustering
of a mass spectrometry example and the results of clustering genomic
data mapped into 3D with Multi Dimensional Scaling MDS.

.. todo:: The slides or videos are going to be updated
          
          Video: https://youtu.be/JejNZhBxjRU



Heuristics
""""""""""

Some remarks are given on heuristics; why are they so important why
getting exact answers is often not so important?

.. todo:: The slides or videos are going to be updated
          
          Video: https://youtu.be/KT22YuX8ZMY


Resources
"""""""""

-  https://en.wikipedia.org/wiki/Kmeans
-  http://grids.ucs.indiana.edu/ptliupages/publications/DACIDR_camera_ready_v0.3.pdf
-  http://salsahpc.indiana.edu/millionseq/
-  http://salsafungiphy.blogspot.com/
-  https://en.wikipedia.org/wiki/Heuristic
