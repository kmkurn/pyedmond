# from distutils.core import setup, Extension
import os
import sys
from setuptools import setup, Extension

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
    sources=['pyedmond/_core.cpp']
)

setup(name='pyedmond',
      version='0.1',
      description='Edmond optimal branching algorithm in C++ wrapped by Python',
      url='http://github.com/xiaohan2012/pyedmond',
      author='Han Xiao',
      author_email='xiaohan2012@gmail.com',
      license='MIT',
      packages=['pyedmond'],
      ext_modules=[core_module],
      setup_requires=['pytest-runner'],
      tests_require=['pytest']
)
