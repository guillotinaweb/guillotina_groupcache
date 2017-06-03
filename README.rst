Warning!!!
==========

WARNING: This project was proof of concept. This is not working for anything useful
in guillotina right now.

https://onna.com/ has open sourced it after we realized it wasn't going to work
for our use-case.

The hope is that others will be able to utilize this and develop the use of
embedding groupcache into python.


Introduction
------------

`guillotina_groupcache` implements https://github.com/golang/groupcache
in python.


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
