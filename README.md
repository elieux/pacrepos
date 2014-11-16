pacrepos
========

A tool to install/uninstall pacman repositories from command line.

Usage
-----

`pacrepos.py -I` to install (ensures pacrepos.conf exists and modifies pacman.conf to include it)

`pacrepos.py -A --name NAME --url URL` to enable repository NAME with server URL

`pacrepos.py -R --name NAME` to disable repository NAME (its section is deleted completely)
