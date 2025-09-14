import pytest
import os, sys


cdir = os.path.dirname(os.path.abspath(__file__))
pdir = os.path.dirname(cdir)
sys.path.insert(0, pdir)

import src.pip.main as pi 
pip = pi.pip()

def test1():
    # test for basic install/uninstall
    pip.install('requests')
    pip.uninstall('sg_api.py', always_confirm=True)
    pip.install(from_filepath="requc.txt")

def test2():
    # test for basic freeze/show
    call = pip.freeze()
    print(f'{call}')

    pip.freeze(to_file=True)

    coll = pip.show('requests')
    print(f'{coll}')
    
    cll = pip.list()
    print(f'{cll}')

def test3():
    # other generic commands
    pip.debug()    
    pip.inspect()

