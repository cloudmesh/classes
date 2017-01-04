.. _slurmcluster:

Virtual SLURM Cluster 
=================================

You will be using cloudmesh and ansible to build a virtual SLURM
cluster on cloud resources.  You wil be identifying a number of
parameters that are useful for the deployment.
Important is also that the software of the cluster can be updated,
while for example shutting down the cluster, updating the cluster and
than restart the queuing system.

A benchmark is to be conducted to compare performance to a real
cluster. This project may use resources from XSEDE comet, a cluster
with over 15000 cores, and will need special permissions. You will
need to showcase the SLURM deployment on an opesntack cloud before you
can use the comet resource. Restrictions in the number of cores will
be employed.

The SLURM cluster shoudl also use Open XDMOD to report on usage whcih
will make benchmarking easier and provide a lot of details.

