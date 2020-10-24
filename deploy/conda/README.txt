These steps assume that the new version of strup is available on PyPI.
======================================================================

-1) Remove eventual strup directory in this folder.
0) Open conda python in this folder
1) conda install m2-patch (if not installed)
2) conda skeleton pypi strup (Download package from pypi and prepare stuff)
3) cd strup
4) check that meta.yaml has been created and contain metadata from PyPI about strup
5) Insert in meta.yaml:  
      build: noarch: python
6) conda build .  (This step creates a noarch package)
Installable on any architecture and Python version (that the package itself supports):)
This feature was introduced in Anaconda 4.3  (ca 2017)

7) pip uninstall strup
8) conda uninstall strup
9) conda install --use-local strup   (will install the *.tar.bz2 file created in step 6)
10) conda list (scroll to see strup)
11) run pytest

Upload to anaconda.org
======================

0) Create free anaconda.org account with username and password
1) conda install anaconda-client   (and enter username and password)
2) anaconda login   (from terminal: logs into the account)
3) anaconda upload *.tar.bz2
4) anaconda logout
