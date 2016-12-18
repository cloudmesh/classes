Github
======

Github is a code repository that allows the development of code in a
distributed fashion. There are many good tutorials about github.

Some of them can be found on the github Web page. An interactive
tutorial is for example available at

* https://try.github.io/

A more extensive list of tutorials can be found at 

* https://help.github.com/articles/what-are-other-good-resources-for-learning-git-and-github

Important is that you always want to make sure that you want to use
the git init command and add your Name and e-mail. Do it consistent in
the machines you use, or your checkins in git (if you do them) do not
show up in a consistant fashion as a single user. This is done with
the following commands::

  $ git config --global user.name "John Doe"
  $ git config --global user.email johndoe@example.com

You can set also the editor with::

  $ git config --global core.editor emacs

More information about a first time setup is documented at::

  $ http://git-scm.com/book/en/Getting-Started-First-Time-Git-Setup

To check your setup you can say::

  $ git config --list
