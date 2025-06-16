# HEP Tools Tutorial
This tutorial provides a quick introduction to data analysis in high energy physics using modern, Python-centric tools.

# Links
Relevant HEP tools:
- [ROOT](https://root.cern.ch/install/)
- [pyHEP](https://hepsoftwarefoundation.org/activities/pyhep.html) - developers and users of Python in Particle Physics
- [pyHEP resources](https://github.com/hsf-training/PyHEP-resources)
- [awkward](https://awkward-array.org/doc/main/) - data manipulation library, used in uproot 
- [uproot](https://uproot.readthedocs.io/en/latest/) - read and write `.root` files
Relevant general tools:
- [pandas](https://pandas.pydata.org/docs/index.html) - data structures and data analysis. The most popular DataFrame interface.
- [jupyter](https://jupyter.org/) - web-based interactive for scripting, grate for working with plots  

The main difference between PyROOT and uproot is the dependency on the ROOT package. PyROOT is a wrapper around ROOT, which is a C++ program. Uproot operates as an independent tool and uses its own standard to interpret `.root` files. While using PyROOT, one can expect perfect compatibility with the program and the `.root` files. Uproot, on the other hand, may not be 100% compatible with all aspects of the `.root` file format but is lightweight and nicely integrated with NumPy and pandas.


![abstraction-layers](https://raw.githubusercontent.com/scikit-hep/uproot5/main/docs-img/diagrams/abstraction-layers.svg)

# Environment Setup
The easiest way to prepare the environment is to install everything using conda. This is the recommended method, as ROOT can be quite tricky to install and use inside a Jupyter notebook.

## Install packages and ROOT with Conda
All needed packages are listed in `environment.yml`. Make sure the python version in the `environment.yml` matches the python version on your machine. To create a conda environment:  
```bash
conda env create -f environment.yml
```
The name of the new environment is set in the 'environment.yml' file. In our case it it `cenv2`. To activate the environment use:
```bash
conda activate cenv2
```
Last step is to make sure we can use this environment with a jupyter notebook or jupyter lab. To do that we need to export the kernel by:
```bash
ipython kernel install --user --name=cenv2-kernel 
```

## Install packages with uv
**Skip this part if you can use conda based setup.** 
  
This is my preferred way of setting up an environment, but unfortunately ROOT is not installable via pip, so it's harder to make it work. This section assumes that you have ROOT installed and know how to run PyROOT in a Jupyter notebook.

**UV setup**

> **Tip**: uv is a modern and fast tool, but if you prefer you can also just use pip.

First install [uv](https://docs.astral.sh/uv): 
```bash
pip install --user uv
```
If you get `This environment is externally managed` error, try to install uv with your package manager, or explore a different installation method from [here](https://docs.astral.sh/uv/getting-started/installation/). To verify the installation, run:
```bash
uv --version
```
> **Tip**: If the uv installation with pip completed without errors, but the command `uv` is not recognized, it may be that you have to add the `~/.local/bin` to the PATH variable using: `PATH=$PATH:/home/$USER/.local/bin` command.

**Setting up the virtual environment with uv**

Now, let's create an virtual environment. It is useful to have separate environments for most project, to keep the package versions in order. Make sure that the python version matches the one your ROOT installation is using. Run: 
```bash
uv venv --relocatable --managed-python --python python3.10
```
Activate the new environment by running: 
```bash
source ./.venv/bin/activate
```

There are many useful tools we would like to install, lets start with the packages listed in the `requirements.txt` file:
```bash
uv pip install -r requirements.txt
```

To validate if everything is working, try running: 
```bash
python -c "import uproot; print(uproot.__version__)"
```

---
# Run tutorial
The tutorial contains Jupyter notebooks (`.ipynb` files). They can be run in an IDE like VSCode or PyCharm, or via a Jupyter notebook server. To start a Jupyter Notebook server in the activated environment:
```bash
jupyter lab
```     

It should print a link in the terminal with a token, something like: http://localhost:8888/lab?token=6e28ee0d05cf9f942f229b2389de00989011bfc611f81149. Open it in a browser. If you're working on a remote server, substitute "localhost" with the server IP. If the remote server has a firewall, you may need to set up port forwarding.