import os
import subprocess
from setuptools import setup

os.environ["CHPL_LIB_PIC"] = "pic"

subprocess.run("git", "clone", "https://github.com/chapel-lang/chapel.git")
os.chdir("chapel")
subprocess.run("./configure")
subprocess.run("make")
subprocess.run("make install")

os.chdir("..")

subprocess.run("chpl betaDiversity.chpl -lnetcdf --fast --library --library-python --library-dir=chapel-beta-diversity", shell=True)

setup()
