import os, os.path
import subprocess
from setuptools import setup

os.environ["CHPL_LIB_PIC"] = "pic"
os.environ["CHPL_LLVM"] = "none"

# only install Chapel once
if not os.path.exists("${PWD}/chapel"):
  subprocess.run(["git", "clone", "https://github.com/chapel-lang/chapel.git"])
  os.chdir("chapel")
  subprocess.run("./configure")
  subprocess.run("make")
  subprocess.run(["make", "install"])

  print("Finished installing Chapel")

  os.chdir("..")

subprocess.run("chpl betaDiversity.chpl -lnetcdf --fast --library --library-python --library-dir=chapel-beta-diversity", shell=True)

print("Finished building the python library")

setup()
