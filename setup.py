import os, os.path
import subprocess
from setuptools import setup, find_packages

os.environ["CHPL_LIB_PIC"] = "pic"
os.environ["CHPL_LLVM"] = "none"

p = subprocess.run(["which", "chpl"])
# only install Chapel once
if p.returncode == 1:
  subprocess.run(["git", "clone", "https://github.com/chapel-lang/chapel.git"])
  os.chdir("chapel")
  subprocess.run(["./configure", "--prefix=" + os.path.dirname(os.path.realpath(__file__))])

  # make it run faster so I don't have to task switch
  numProcs = subprocess.run("./util/buildRelease/chpl-make-cpu_count",
                            capture_output=True, text=True).stdout.strip()
  subprocess.run(["make", "-j" + numProcs])
  subprocess.run(["make", "install"])

  # sanity check printing
  subprocess.run("echo $PATH", shell=True)
  subprocess.run(["ls", os.path.dirname(os.path.realpath(__file__)) + "/bin"])

  print("Finished installing Chapel")

  os.chdir("..")

subprocess.run("chpl betaDiversity.chpl -lnetcdf --fast --library --library-python --library-dir=chapelBetaDiversity", shell=True)

print("Finished building the python library")

# sanity check to see the state of the directory after the majority of this script
subprocess.run("ls")

setup()
