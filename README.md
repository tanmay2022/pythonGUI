#How to use?

You can use a package manager like Miniconda or Anaconda to avoid issues with system python. Miniconda is enough for this specific purpose.

Install Miniconda package manager from https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-Linux-x86_64.sh

Now create a virtual environment with python 3.8 and pip:

conda create --name micros python=3.8 pip

Activate virtual environment micros:

conda activate micros

Install the packages below using pip (group them together to avoid dependency issue):

pip install pyqt5 scikit-image vtk tinydb sympy==1.8 pycalphad==0.9.2

Launch MicroSim:

python MicroSim.py
