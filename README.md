# AMR Question & Answering
ASLN 2016: Question Answering with a AMR knowledge base.

Ask question about the Little Prince and get the answer. Implemented using [AMR](http://amr.isi.edu/index.html) and the Little Prince corpus from the [Linguistic Data Consortium](https://www.ldc.upenn.edu/).

## Instalation
Tested with Python 2.7.12 (CAMR is still not ported to Python 3) and Ubuntu.

Before prociding make sure _CAMR: A transition-based AMR Parser_ is working on your computer (https://github.com/c-amr/camr). A requirements.txt file is provided to help you install dependencies of CAMR, but is not necesarry if is already installed. Apart from CAMR, this project doesn't have any dependency.

**Important:** Clone CAMR Github repository in the root folder (_AMR-QA/camr_).
Then place the model file (as describe in CAMR repository) inside the carm folder with the name 'LDC2014T12.m' (_AMR-QA/camr/LDC2014T12.m_)

Finally, run it:
```
$ python QA.py
```

**Notice:** python 2 path should be accessible through python, not python2 command. If not use Virtualenv or Pyenv and make sure that when calling:
```
python --version
```
you get the output:
```
Python 2.7.*** 