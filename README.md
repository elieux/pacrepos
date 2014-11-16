pacrepos
========

A tool to install/uninstall pacman repositories from command line.

Warning
-------

Installing packages from unofficial repositories is unsupported and discouraged and could partially or completely break your system. You probably won't get much technical support if that happens, so do it only if you know how to repair your system.

Usage
-----

`pacrepos.py -I` to install (ensures pacrepos.conf exists and modifies pacman.conf to include it)

`pacrepos.py -U` to uninstall from pacman.conf

`pacrepos.py -L` to list all repositories and their servers (only those installed with this tool)

`pacrepos.py -A --name NAME --url URL` to enable repository NAME with server URL

`pacrepos.py -R --name NAME` to disable repository NAME (its section is deleted completely)
