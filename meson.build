project(
    'pymt_gipl',
    'c', 'cython', 'fortran',
    version: 'v0.2',
    license: 'MIT',
)

py = import('python').find_installation(pure: false)
fc = meson.get_compiler('fortran')

python_inc = py.get_path('data') / 'include'
numpy_inc = run_command(
    py,
    [
        '-c',
        'import numpy; print(numpy.get_include())'
    ],
    check: true
).stdout().strip()
incs = include_directories(
    [
        'pymt_gipl/lib',
        python_inc,
        numpy_inc,
    ]
)

deps = [
    fc.find_library('bmif'),
    fc.find_library('bmigiplf'),
    py.dependency(),
]

# Files get copied to <python directory>/site-packages/<subdir>
install_pkg_srcs = [
    'pymt_gipl/__init__.py',
    'pymt_gipl/_bmi.py',
    'pymt_gipl/_version.py',
]
py.install_sources(
    install_pkg_srcs,
    subdir: 'pymt_gipl',
)

install_lib_srcs = [
    'pymt_gipl/lib/__init__.py',
    'pymt_gipl/lib/gipl.pyx',
]
py.install_sources(
    install_lib_srcs,
    subdir: 'pymt_gipl/lib',
)
py.extension_module(
    'gipl',
    [
        'pymt_gipl/lib/bmi_interoperability.f90',
        'pymt_gipl/lib/gipl.pyx',
    ],
    dependencies: deps,
    include_directories: incs,
    install: true,
    subdir: 'pymt_gipl/lib',
)

install_subdir(
    'meta/GIPL',
    install_dir: py.get_install_dir() / 'pymt_gipl/data',
)

# This is a temporary fix for editable installs.
run_command('cp', '-r', 'pymt_gipl/data', 'build', check: false)
