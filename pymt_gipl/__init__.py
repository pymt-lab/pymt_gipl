#! /usr/bin/env python

from .bmi import (GIPL,
)

__all__ = ["GIPL",
]

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
