# How to use?

* You can use a package manager like Miniconda or Anaconda to avoid issues with system python. Miniconda is enough for this specific purpose.

* Install Miniconda package manager from https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-Linux-x86_64.sh

* Now create a virtual environment with python 3.9 (this version and previous are compatible with the packages required) and pip:

> conda create --name msenv python=3.9 pip

* Activate virtual environment msenv:

> conda activate msenv

* Install the packages below using pip (group them together to avoid dependency issue):

> pip install pyqt5 scikit-image vtk tinydb sympy==1.8 pycalphad==0.9.2 pymks yt

* Launch MicroSim:

> python MicroSim.py
