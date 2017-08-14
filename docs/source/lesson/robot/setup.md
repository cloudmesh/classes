# Setup

    sudo xcode-select --install
    sudo xcode-select -p

you will see

    /Applications/Xcode.app/Contents/Developer

In an administrative account do the following:

    sudo easy_install pip
    sudo ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install pycrypto
    sudo pip install ansible
    sudo pip install ansible --upgrade




## Linux

	mkdir github
  	cd github
  	git clone https://github.com/cloudmesh/cloudmesh.robot.git
  	ssh-keygen
  	sudo apt-get install -y emacs
	sudo apt-get install -y cmake
	sudo apt-get install -y libqt4-dev
  	git config --global user.name "Gregor von Laszewski"
  	git config --global user.email laszewski@gmail.com
  	git config --global core.editor emacs
	git config --global push.default matching

The linux instalation istructions are incomplete

## Installation of tools

Once you have installed cloudmesh robots you well be able to install a
numebr of tools automatically with the command

	$ cms robot osx install
	
This will install for you a number of tools including xcode, homebrew,
macdown, pycharm, and aquaemacs. If you have some these tools already
installed it will skip the instalation process for a particular tool.

If you do not like this automatic install or you have a differnt
operating system, please find alternative ways to install these
tools. Let us know how you installed the tools on Linux or Windows and
we will integrate it into our instalation.

Please note that some of the tools require root access and thus you
must be able to have ccess to sudo to run them from our tool.


## OSX

For OSX we have created a

* [system.sh](http://cloudmesh.github.io/get/robot/osx/system/)

and a

* [user.sh](http://cloudmesh.github.io/get/robot/osx/user)

The **system** script
must be ran on an **Administrator** account and the **user** script must be ran on a **User** account.


To easily execute the  **system** script, type in the Administrator account terminal

    curl -fsSL http://cloudmesh.github.io/get/robot/osx/system | sh

To easily execute the  **user** script, type in the User account terminal

     curl -fsSL http://cloudmesh.github.io/get/robot/osx/user | sh


These scripts allow you to install in a simple way development tools
that you may find useful for the activities reported on in this
repository. First we must install a number of tools on the machine
connecting to the board.

Some setup options

* https://github.com/ricbra/dotfiles/blob/master/bin/setup_osx
*
https://blog.vandenbrand.org/2016/01/04/how-to-automate-your-mac-os-x-setup-with-ansible/

### OSX

In our guide we will focus on OSX, however, there should not be any
issues with modifying our installations to work with other operating
systems, such as Linux or even Windows. If you have improvements in
regards to our code, please let us know.

On OSX we will be using homebrew and pyenv to leverage existing
libraries and to allow the use of a user managed Python environment.

#### XCode

OSX provides a number of useful extensions for developers with
*xcode*. Please install it with

	$ xcode-select --install
	
#### Homebrew

Homebrew is a program and package manager that makes it easy to uninstall
precompiled programs on your computer.

To install it you need to open a terminal and run the following command

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

#### Install pyenv

Next we install a program called pyenv that will help us managing multiple
versions of python. This is done with the commands

    $ brew update
    $ brew install pyenv pyenv-virtualenv pyenv-virtualenvwrapper
	 
As we later may want to benefit from readline, lest just install it also
	 
	 $ brew install readline xz


#### Install Aquamacs

You will need an editor to make some modifications to files and write
programs. Certainly you can use `vi` or `emacs`. As we are on OSX we
can also use an editor such as `aquamacs`. To install this easy to use editor we use

	 brew cask install aquamacs
	 
We recommend to add a shortcut so you can call it from the commandline. This can be done by editing the
`~/.bash_profile` and add the following to it.

	####################################################################### 
	# PYENV
	######################################################################
	open_emacs() {
    	# open -na Aquamacs $*
    	open -a Aquamacs $*    
	}

	alias emacs=open_emacs

Once done you can start the editor while using the command

	emacs FILENAME
	
where FILENAME is the name of the file you like to edit.


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
