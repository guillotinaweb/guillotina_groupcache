Introduction
============

`guillotina_groupcache` implements https://github.com/golang/groupcache
in python, for guillotina--to provide caching for objects.


But how?
--------

We embed golang into python. Yup.


How to run this...
------------------

Make sure to have golang installed

Do something like this::

    virtualenv .
    ./bin/pip install zc.buildout
    ./bin/buildout
    make init
    make go
