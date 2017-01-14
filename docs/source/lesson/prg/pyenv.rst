pyenv
=====

Install pyenv on OSX
--------------------

Install xcode
^^^^^^^^^^^^^

Install xcode and activate command tools

::
  
   xcode-select --install


Install pyenv via homebrew
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   brew update
   brew install pyenv pyenv-virtualenv pyenv-virtualenvwrapper
   brew install readline xz


Install different python versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   pyenv install 2.7.13
   pyenv install 3.6.0

   pyenv global 2.7.13
   pyenv version
   pyenv virtualenv 2.7.13 ENV2
   pyenv virtualenv 3.6.0 ENV3


Switching environments
----------------------

::

  Last login: Sat Jan 14 09:44:44 on ttys005
  (2.7.13) laptop~ gregor$ pyenv activate ENV2
  (ENV2) laptop~ gregor$ pyenv activate ENV3
  (ENV3) laptop~ gregor$ pyenv activate ENV2
  (ENV2) laptop~ gregor$ pyenv deactivate ENV2
  (2.7.13) laptop~ gregor$ 


Make sure pip is up to date
^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   pip install pip -U