.. _projects:
Software Projects
=================

Project Objectives
------------------
In this project, you will choose a particular application of your interest, reserve cloud resources for your project, deploy your application and dataset to cloud resources and collect experiment benchmarks.

You will launch your project by submitting a research proposal, and complete it with a formal technical report, which present data and conclude your finds.

Deliverable Requirements
------------------------

#. Provide a report in the ``docs/report`` directory

   Use LaTeX to write your report. Submission should include the original sources as well as a PDF called ``report.pdf``
   (See :ref:`overview-software-project` for additional details on the
   report format. You will be using 2 column ACM format we have used before.)

#. Provide a properly formatted ``README.rst`` or ``README.md`` in the root directory, which contains the following sections:

   - Authors: list the authors
   - Problem: describe the task and/or problem
   - Requirements: describe your assumptions and requirements for deployment/running. This should include any software requirements with a link to their websites. Also indicate which versions you have developed/tested with.
   - Deployment/Running: describe the steps needed to deploy and run.
   - Acknowledgments: provide proper attribution to any websites, or code you may have used or adapted.
     
#. A ``LICENSE`` file (this should be the ``LICENSE`` for Apache License Version 2.0)

#. All figures should include labels with the following format: ``label (units)``. For example:

   - ``distance (meters)``
   - ``volume (liters)``
   - ``cost (USD)``

#. All figures should have a caption describing what the measurement is, and a summary of the conclusions drawn. For example:

    This shows how A changes with regards to B, indicating that under
    conditions X, Y, Z, Alpha is 42 times better than otherwise.

Detail Instructions
-------------------

#. Ansible Deployment

   You always need to make sure your project can be repeatedly deployed in a same environment. Student will use Ansible as the automated software deployments tool. Instructions of using Ansible is is illustrated in a separated lesson(s).

   Your deployment should handle the process of downloading and installing the required datasets and pushing the analysis code to the remote node.

#. Application Execution

   You should use the cluster you reserved on clouds to execute programs of your choice and show the utilization of your entire cluster. You should also benchmark the deployment and running of your demonstration on several sizes of a cluster (e.g. 1, 3, 6, 10 nodes) (Note that these numbers are for example only).

   You should provide instructions on how to run and interpret your analysis code in your README.

#. Data Analytics

   You need to analyze outputs of your application execution. The key here is to take the datasets and extract some meaningful information using tools such as ``scikit-learn``, ``mllib``, or others.

   You should be able to provide graphs, descriptions for your graphs, and argue for conclusions drawn from your analysis.

   For the graphs, we expect to see figures showing times for each (deployment, running) pair on for each cluster size, with error bars. This means that you need to run each benchmark multiple times (at least three times) in order to get the error bars. You should also demonstrate cluster utilization for each cluster size.