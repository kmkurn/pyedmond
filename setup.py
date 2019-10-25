import os
import sys
from setuptools import find_packages, setup, Extension

os.environ["CC"] = "g++"
os.environ["CXX"] = "g++"

extra_link_args = []
if sys.platform.startswith('linux'):
    extra_link_args.append('-Wl,--export-dynamic')

core_module = Extension(
    'pyedmond/_core',
    libraries=['boost_python', 'boost_graph'],
    extra_compile_args=['-std=c++11', '-O2', '-Wall'],
    extra_link_args=extra_link_args,
    sources=['pyedmond/_core.cpp'])

setup(
    name='pyedmond',
    version='0.1',
    description='Edmond optimal branching algorithm in C++ wrapped by Python',
    url='http://github.com/kmkurn/pyedmond',
    author='Kemal Kurniawan',
    author_email='kemal@kkurniawan.com',
    license='MIT',
    packages=find_packages(),
    ext_modules=[core_module],
    python_requires='>=3.7,<4')
