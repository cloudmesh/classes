# OSX Dev Setup

   



#### Install python 3.6.1

As we want to develop our programs in python we will install it with `pyenv` as follows

    $ pyenv install 3.6.1
    $ pyenv virtualenv 3.6.1 ENV3

To not forget that you are using python 3 and automatically loading it
we simply add it to our `~/.bash_profile` file.

    $ emacs ~/.bash_profile

Add the following lines at the end of the file

    ########################################################
    # PYENV
    ########################################################
    export PYENV_VIRTUALENV_DISABLE_PROMPT=0
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

    alias ENV3="pyenv activate ENV3"

    ENV3


The above steps have to be done only once. Now every time you start a
new terminal it will activate ENV3 and with it python 3.6.1.

**Please now close all previously started terminals that do not use
  yet ENV3**

To further improve your python environment you need to make sure *pip*
and *setuptools* are up to date. After you have started a new terminal
window you will by default activate Python 3. To make sure pip and
setup tools are up to date, you can once call

	$ pip install pip -U
	$ pip install setuptools -U
