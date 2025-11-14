import os
from py_compile import compile as comp

cwd = os.getcwd()


def ccdir(folder):
    for f in os.listdir(folder):
        pathf = folder+"\\"+f
        if os.path.isdir(pathf):
            ccdir(pathf)
        elif f.endswith(".py"):
            try:
                comp(pathf,doraise=True)
                print ".",
                os.remove(pathf)
            except Exception,e:
                print e
            



for f in os.listdir(cwd):
    pathf = cwd+"\\"+f
    if os.path.isdir(pathf):
        ccdir(pathf)