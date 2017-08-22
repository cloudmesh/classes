Basic Emacs
===========

One of the most useful short manuals for emacs is the following
refrence card. It takes some time to use this card efficiently, but
the most important commands are written on it. Generations of students
have litterally been just presented with this card and they learned
emacs from it.

* https://www.gnu.org/software/emacs/refcards/pdf/refcard.pdf

There is naturally also additional material available and a great
manual. You could also look at
  
* https://www.gnu.org/software/emacs/tour/

From the last page we have summarized the most useful and **simple**
features. And present them here. One of the hidden gems of emacs is
the ability to recreate replay able macros which we include here also.
You ought to try it and you will find that for data science and the
cleanup of data emacs (applied to smaller datasets) is a gem.

Notation
  
========  =====================
Key       Description
========  =====================
C         Control
M         Esc  (meta character)
========  =====================

In the event of an emergency…

Here's what to do if you've accidentally pressed a wrong key:

If you executed a command and Emacs has modified your buffer, use C-/
to undo that change.  If you pressed a prefix key (e.g. C-x) or you
invoked a command which is now prompting you for input (e.g. Find
file: …), type C-g, repeatedly if necessary, to cancel.  C-g also
cancels a long-running operation if it appears that Emacs has frozen.


Moving around in buffers can be done with cursor keys, or with the
following key combinations:

======  =====================
Key     Description
======  =====================
C-f	Forward one character
C-n	Next line
C-b	Back one character
C-p	Previous line
======  =====================

Here are some ways to move around in larger increments:

======  =====================
Key     Description
======  =====================
C-a	Beginning of line
M-f	Forward one word
M-a	Previous sentence
M-v	Previous screen
M-<	Beginning of buffer
C-e	End of line
M-b	Back one word
M-e	Next sentence
C-v	Next screen
M->	End of buffer
======  =====================

You can jump directly to a particular line number in a buffer:

======  =======================
Key     Description
======  =======================
M-g g	Jump to specified line
======  =======================

Searching is easy with the following commands

======  ============================
Key     Description
======  ============================
C-s	Incremental search forward
C-r	Incremental search backward
======  ============================

Replace


======  ============================
Key     Description
======  ============================
M-%	Query replace
======  ============================

Killing ("cutting") text

======  ============================
Key     Description
======  ============================
C-k	Kill line
======  ============================

Yanking

======  ============================
Key     Description
======  ============================
C-y	Yanks last killed text
======  ============================

Macros

Keyboard Macros

Keyboard macros are a way to remember a fixed sequence of keys for
later repetition. They're handy for automating some boring editing
tasks.

=========  =================================
Key        Description
=========  =================================
M-x (	   Start recording macro
M-x )	   Stop recording macro
M-x e	   Play back macro once
M-5 M-x-e  Play back macro 5 times
=========  =================================

Modes

"Every buffer has an associated major mode, which alters certain
behaviors, key bindings, and text display in that buffer. The idea is
to customize the appearance and features available based on the
contents of the buffer."  modes are typically activated by ending such
as .py, .java, .rst, ...

==================  ========================================================================
Key                 Description
==================  ========================================================================
M-x python-mode     Mode for editing Python files
M-x auto-fill-mode  Wraps your lines automatically when they get longer than 70 characters.
M-x flyspell-mode   Highlights misspelled words as you type.
==================  ========================================================================
