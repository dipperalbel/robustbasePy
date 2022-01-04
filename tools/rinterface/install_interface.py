import tarfile
import os
import subprocess
import shutil
os.chdir('tools/rinterface')
destination = os.path.realpath('../../lmrob')

tf = tarfile.open('rinterface.tar.gz')
tf.extractall()
basepath = os.path.realpath('rpy2-2.9.5')

os.chdir(basepath)
p = subprocess.Popen("python setup.py build",
                shell=True,
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)

p.wait()
os.chdir('build/lib.linux-x86_64-3.6/rpy2')
if os.path.exists(destination + '/rinterface'):
    shutil.rmtree(destination + '/rinterface')
shutil.copytree('rinterface', destination + '/rinterface')
os.chdir(basepath)
os.chdir('..')
shutil.rmtree('rpy2-2.9.5')

