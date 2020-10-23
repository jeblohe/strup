API tokens provide an alternative way (instead of username and password) to authenticate 
when uploading packages to PyPI.

Go to https://test.pypi.org/manage/account/#api-tokens and create a new API token; 
don’t limit its scope to a particular project, since you are creating a new project.

-1) type: "python -m pip install --user --upgrade twine" (if not installed)
0) After successfull testing and CI reports:
1) Check that the version number in strup/__init__.py is correct for the new release
   - Push to github if you need to modify the version number.
2) Goto the root of the repository in a Python command line.
3) Type: "python setup.py sdist bdist_wheel --universal"   (drop --universal when dropping py27 support)
   - Check that dist/* includes a version for all Python versions, all platforms
4) Type: "twine upload --repository testpypi dist/*"
   - Enter username and password for TestPyPI (not the same as for PyPI)
5) After a minute or two check out: https://test.pypi.org/project/strup
6) type: "pip uninstall strup"
7) type: "pip install --index-url https://test.pypi.org/simple/ strup"
8) Check it out running pytest

If OK install on PyPI (see instructions in other folder)
