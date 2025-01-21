# pymt_gipl

[![Basic Model Interface](https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg)](https://bmi.readthedocs.io/)

[![Test](https://github.com/pymt-lab/pymt_gipl/actions/workflows/test.yml/badge.svg)](https://github.com/pymt-lab/pymt_gipl/actions/workflows/test.yml)

[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pymt_gipl.svg)](https://anaconda.org/conda-forge/pymt_gipl)

PyMT plugin for GIPL

- Free software: MIT license
- Documentation: <https://gipl.readthedocs.io>.

  | Component | PyMT
  | --------- | ----------------------------
  | GIPL      | from pymt.models import GIPL

## Installing pymt

Installing pymt from the conda-forge channel
can be achieved by adding conda-forge to your channels with:
``` 
conda config --add channels conda-forge
```

*Note*: Before installing pymt, you may want to create a
separate environment into which to install it. This can be done with,
``` 
conda create -n pymt python=3
conda activate pymt
```

Once the conda-forge channel has been enabled,
pymt can be installed with:
``` 
conda install pymt
```

It is possible to list all of the versions of pymt
available on your platform with:
``` 
conda search pymt --channel conda-forge
```

## Installing pymt_gipl

Once pymt is installed, the dependencies of
pymt_gipl can be installed with:
``` 
conda install bmi-fortran=1.2 gipl
```

To install pymt_gipl,
``` 
conda install pymt_gipl
```
