#!/usr/bin/env python

import os
from os.path import join
import sys
import subprocess
import shutil
import tarfile
import distutils.dir_util as dir_util
from time import sleep


env = os.environ
wineprefix = join(os.getcwd(),'wine-folder')
env['WINEPREFIX'] = wineprefix
builddir = 'pyCharGen'
pyinstaller = os.path.expanduser('~/pymisc/pyinstaller-2.0/pyinstaller.py')

def make_wine_tarball():
    #Install python
    python_msi = 'python-2.7.3.msi'
    subprocess.call(['wineboot','-i'],env=env)
    subprocess.call(['wget','http://www.python.org/ftp/python/2.7.3/'+python_msi])
    subprocess.call(['wine','msiexec','/i',python_msi,'/qb'],env=env)
    os.remove(python_msi)
    #Install pygtk
    pygtk_msi = 'pygtk-all-in-one-2.24.2.win32-py2.7.msi'
    subprocess.call(['wget','http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.24/'+pygtk_msi])
    subprocess.call(['wine','msiexec','/i',pygtk_msi,r'TARGETDIR=C:\Python27','/qb'],env=env)
    os.remove(pygtk_msi)
    #Install pywin32
    pywin32_exe = 'pywin32-218.win32-py2.7.exe'
    subprocess.call(['wget','http://downloads.sourceforge.net/pywin32/'+pywin32_exe])
    subprocess.call(['winetricks','vcrun2008','vcrun2010'],env=env)
    subprocess.call(['wine',pywin32_exe],env=env)
    os.remove(pywin32_exe)
    #Install pyparsing
    pyparsing_exe = 'pyparsing-2.0.1.win32-py2.7.exe'
    subprocess.call(['wget','http://downloads.sourceforge.net/project/pyparsing/pyparsing/pyparsing-2.0.1/'+pyparsing_exe])
    subprocess.call(['wine',pyparsing_exe],env=env)
    os.remove(pyparsing_exe)
    #Make tarball
    subprocess.call(['tar','-czf','wine-frozen.tar.gz','wine-folder'])
    dir_util.remove_tree(wineprefix)

def make_base_folder():
    try:
        dir_util.remove_tree(builddir)
    except OSError:
        pass
    dir_util.copy_tree('../tables',join(builddir,'tables'))
    dir_util.copy_tree('../resources',join(builddir,'resources'))


def make_linux_exe():
    make_base_folder()
    dir_util.copy_tree('../resources-linux',join(builddir,'resources'))
    try:
        os.remove('pyCharGen.tar.gz')
    except OSError:
        pass
    #Make the exe
    subprocess.call(['python',pyinstaller,'pyinst_linux.spec'])
    #Bundle everything together
    shutil.copy(join('dist','pyCharGen'),builddir)
    subprocess.call(['tar','-czf','pyCharGen.tar.gz',builddir])
    dir_util.remove_tree(builddir)

def make_windows_exe():
    if not os.path.exists('wine-frozen.tar.gz'):
        make_wine_tarball()
    make_base_folder()
    dir_util.copy_tree('../resources-windows',join(builddir,'resources'))
    try:
        os.remove('pyCharGen.zip')
    except OSError:
        pass
    #Make the exe.
    subprocess.call(['tar','-xzf','wine-frozen.tar.gz'])
    subprocess.call(['wine',r'C:\Python27\python.exe',pyinstaller,'pyinst_windows.spec'],env=env)
    shutil.rmtree(wineprefix)
    #Bundle everything together
    shutil.copy(join('dist','pyCharGen.exe'),builddir)
    subprocess.call(['zip','-9','-r','pyCharGen.zip',builddir])
    dir_util.remove_tree(builddir)

def name_exes(name='unstable'):
    os.rename('pyCharGen.zip','pyCharGen-win-{0}.zip'.format(name))
    os.rename('pyCharGen.tar.gz','pyCharGen-linux-{0}.tar.gz'.format(name))



if __name__=='__main__':
    make_linux_exe()
    make_windows_exe()
    name_exes(sys.argv[1] if len(sys.argv)>=2 else 'unstable')
