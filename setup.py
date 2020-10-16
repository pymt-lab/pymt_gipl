#! /usr/bin/env python
import os
import sys
import subprocess
import contextlib
import numpy as np

import versioneer
from setuptools import find_packages, setup

from distutils.extension import Extension
from model_metadata.utils import get_cmdclass, get_entry_points

from setuptools.command.build_ext import build_ext as _build_ext
from numpy.distutils.fcompiler import new_fcompiler


common_flags = {
    "include_dirs": [
        np.get_include(),
        os.path.join(sys.prefix, "include"),
    ],
    "library_dirs": [
    ],
    "define_macros": [
    ],
    "undef_macros": [
    ],
    "extra_compile_args": [
    ],
    "language": "c",
}

libraries = [
]

ext_modules = [
    Extension(
        "pymt_gipl.lib.gipl",
        ["pymt_gipl/lib/gipl.pyx"],
        libraries=libraries + ["bmigiplf"],
        extra_objects=['pymt_gipl/lib/bmi_interoperability.o'],
        **common_flags
    ),
]

packages = find_packages()
pymt_components = [(
        "GIPL=pymt_gipl.bmi:GIPL",
        "meta/GIPL",
    ),
]


def build_interoperability():
    compiler = new_fcompiler()
    compiler.customize()

    cmd = []
    cmd.append(compiler.compiler_f90[0])
    cmd.append(compiler.compile_switch)
    cmd.append('-fPIC')
    for include_dir in common_flags['include_dirs']:
        if os.path.isabs(include_dir) is False:
            include_dir = os.path.join(sys.prefix, "include", include_dir)
        cmd.append('-I{}'.format(include_dir))
    cmd.append('bmi_interoperability.f90')

    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        raise


@contextlib.contextmanager
def as_cwd(path):
    prev_cwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(prev_cwd)


class build_ext(_build_ext):

    def run(self):
        with as_cwd('pymt_gipl/lib'):
            build_interoperability()
        _build_ext.run(self)


cmdclass = get_cmdclass(pymt_components, cmdclass=versioneer.get_cmdclass())
cmdclass["build_ext"] = build_ext

setup(
    name="pymt_gipl",
    author="Mark Piper",
    description="PyMT plugin for gipl",
    version=versioneer.get_version(),
    setup_requires=["cython"],
    ext_modules=ext_modules,
    packages=packages,
    cmdclass=cmdclass,
    entry_points=get_entry_points(pymt_components),
)
