import os
import subprocess
from setuptools import setup

os.environ["CHPL_LIB_PIC"] = "pic"
# TODO: install Chapel
# install netcdf?

subprocess.run("chpl betaDiversity.chpl -lnetcdf --fast --library --library-python --library-dir=chapel-beta-diversity", shell=True)

setup()
