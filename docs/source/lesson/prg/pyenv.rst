pyenv
=====

pyenv allows users to switch between multiple versions of Python
[https://github.com/yyuu/pyenv].

pyenv allows:

* users to  change the global Python version on a per-user basis;
* users to enable support for per-project Python versions;
* easy version changes without complex environment variable
  management;
* to search installed commands accross different python versions;
* integrate with tox [https://tox.readthedocs.io/en/latest/].

Install pyenv on OSX
--------------------

We describe here a mechanism of installing pyenv with homebrew. Other
mechanisms can be found on the pyenv documentation page
[https://github.com/yyuu/pyenv-installer]. First, make sure you have
xcode installed::
  
   $ xcode-select --install

Next install homebrew, pyenv, pyenv-virtualenv and
pyenv-virtualwrapper. Additionally install readline and
some compression tools::

   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   brew update
   brew install pyenv pyenv-virtualenv pyenv-virtualenvwrapper
   brew install readline xz


Python Versions
---------------
In order to use pyenv, you need to have more than one python version
installed. We recommend you download and install python 2.7.13
and 3.6 from python.org [https://www.python.org/downloads/]

Install Different Python Versions
---------------------------------

You can now install different versions of python into your local
environment with the following commands::

   $ pyenv install 2.7.13
   $ pyenv install 3.6.0

You can set the global python defualt version with::

   $ pyenv global 2.7.13

Type the following to determine which versions you have available::

   $ pyenv version

Associate a specifc environment name with a certain python version,
use the following commands::
  
   $ pyenv virtualenv 2.7.13 ENV2
   $ pyenv virtualenv 3.6.0 ENV3

In the example above, `ENV2` would represent python 2.7.13 while `ENV3`
would represent python 3.6.0. Often it is easier to type the alias rather 
than the explicit version.
   
Set up the Shell
-----------------

To make all work smoothly from your terminal, you can 
include the follwowing in your .bashrc files::

   export PYENV_VIRTUALENV_DISABLE_PROMPT=1
   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"

   __pyenv_version_ps1() {
     local ret=$?;
     output=$(pyenv version-name)
     if [[ ! -z $output ]]; then
       echo -n "($output)"
     fi
     return $ret;
   }

   PS1="\$(__pyenv_version_ps1) ${PS1}"

   
Switching Environments
----------------------

After setting up the different environments, switching between them is now easy.
Simply use the following commands::

  
  (2.7.13) laptop~ gregor$ pyenv activate ENV2
  (ENV2) laptop~ gregor$ pyenv activate ENV3
  (ENV3) laptop~ gregor$ pyenv activate ENV2
  (ENV2) laptop~ gregor$ pyenv deactivate ENV2
  (2.7.13) laptop~ gregor$ 

To make it even easier, you can add the following lines to your `.bash_provild`
file::

  alias ENV2="pyenv activate ENV2"
  alias ENV3="pyenv activate ENV3"

If you start a new terminal, you can switch between the different
versions of python simply by typing::

  $ ENV2
  $ ENV3

Try it out.

Make sure pip is up to date
---------------------------

As you will want to install other packages, make sure pip is up to
date::

   pip install pip -U


Excersise
---------

pyenv.1:
   Write installation instructions for an operating system of your choice
   and add to this documentation.

pyenv.2:
   Replicate the steps above, so you can type in ENV2 and ENV3 in your
   terminals to switch between python 2 and 3.
   
