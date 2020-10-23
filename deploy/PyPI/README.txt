Only do these steps in case of successfully installation on TestPyPI:

0) - Check that dist/* includes the same version that you installed on TestPyPI
1) Type: "twine upload dist/*"
   - Enter username and password for PyPI (not the same as for TestPyPI)
5) After a minute or two check out: https://pypi.org/project/strup/
6) type: "pip uninstall strup"
7) type: "pip install strup"
8) Check it out running pytest

If OK install on Conda (see instructions in other folder)
