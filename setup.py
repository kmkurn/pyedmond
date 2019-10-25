# from distutils.core import setup, Extension
import os
from setuptools import setup, Extension

os.environ["CC"] = "g++"
os.environ["CXX"] = "g++"

core_module = Extension(
    'pyedmond/_core',
    include_dirs=['/usr/include/python3.5/'],
    libraries=['boost_python-py35', 'boost_graph'],
    library_dirs=['/usr/lib/x86_64-linux-gnu/'],
    extra_compile_args=['-std=c++11', '-O2', '-Wall'],
    extra_link_args=['-Wl,--export-dynamic'],
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
