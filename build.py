#!/usr/bin/env python

import os
from os.path import join
import sys
import subprocess
import shutil


env = os.environ
wineprefix = join(os.getcwd(),'wine-folder')
env['WINEPREFIX'] = wineprefix
builddir = 'pyCharGen'
pyinstaller = os.path.expanduser('~/pylib/pyinstaller-2.0/pyinstaller.py')

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
    #Make tarball
    subprocess.call(['tar','-czf','wine-frozen.tar.gz','wine-folder'])
    shutil.rmtree(wineprefix)

def make_base_folder():
    try:
        shutil.rmtree(builddir)
    except OSError:
        pass
    os.mkdir(builddir)
    shutil.copytree('tables',join(builddir,'tables'))
    os.mkdir(join(builddir,'glade'))
    shutil.copy(join('glade','MainWindow.ui'),join(builddir,'glade'))
                    
def make_linux_exe():
    make_base_folder()
    try:
        os.remove('pyCharGen.tar.gz')
    except OSError:
        pass
    #Make the exe
    subprocess.call(['python',pyinstaller,'MainWindow.py','--onefile','--name=pyCharGen'])
    #Bundle everything together
    shutil.copy(join('dist','pyCharGen'),builddir)
    subprocess.call(['tar','-czf','pyCharGen.tar.gz',builddir])
    shutil.rmtree(builddir)

def make_windows_exe():
    if not os.path.exists('wine-frozen.tar.gz'):
        make_wine_tarball()
    make_base_folder()
    try:
        os.remove('pyCharGen.zip')
    except OSError:
        pass
    #Make the exe.
    subprocess.call(['tar','-xzf','wine-frozen.tar.gz'])
    subprocess.call(['wine',r'C:\Python27\python.exe',pyinstaller,'MainWindow.py',
                     '--onefile','--windowed','--name=pyCharGen'],env=env)
    shutil.rmtree(wineprefix)
    #Bundle everything together
    shutil.copy(join('dist','pyCharGen.exe'),builddir)
    subprocess.call(['zip','-9','-r','pyCharGen.zip',builddir])
    shutil.rmtree(builddir)

def name_exes():
    try:
        os.mkdir('downloads')
    except OSError:
        pass
    os.rename('pyCharGen.zip',join('downloads','pyCharGen.zip'))
    os.rename('pyCharGen.tar.gz',join('downloads','pyCharGen.tar.gz'))

    

def upload_build():
    subprocess.call(['rsync -e ssh -r downloads/* eldritchcheese@frs.sourceforge.net:/home/frs/project/pychargen'],shell=True)
    #subprocess.call(['scp','pyCharGen.zip','eldritchcheese@frs.sourceforge.net:/home/frs/project/pychargen'])
    #subprocess.call(['scp','pyCharGen.tar.gz','eldritchcheese@frs.sourceforge.net:/home/frs/project/pychargen'])

if __name__=='__main__':
    make_linux_exe()
    make_windows_exe()
    name_exes()
    upload_build()
