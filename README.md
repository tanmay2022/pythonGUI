### How to use?

* This script depends on gnome-terminal. So, make sure you have it installed from the package repository of your linux distribution.

* You can use a package manager like Miniconda or Anaconda to avoid issues with system python. Miniconda is enough for this specific purpose.

* Install Miniconda package manager from https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-Linux-x86_64.sh

* Now create a virtual environment with python 3.9 (version previous to this are also compatible with the packages required) and pip:

> conda create --name msenv python=3.9 pip

* Activate virtual environment msenv:

> conda activate msenv

* Install the packages below using pip (group them together to avoid dependency issue):

> pip install pyqt5 scikit-image vtk tinydb sympy==1.8 pycalphad==0.9.2 pymks yt

* To convert h5 to VTK, pvpython (or ParaView) must be added to the $PATH

* Launch MicroSim:

> python MicroSim.py

### Do you want to modify the GUI as a developer?

* You can switch to some other environment like base:

> conda activate base

* Install pyqt to have access to QT designer:

> conda install pyqt

* Launch QT designer:

> designer

* Open resources/mainscreen.ui
