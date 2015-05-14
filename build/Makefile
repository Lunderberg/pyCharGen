#sudo apt-get install wine1.6 winetricks

export WINEPREFIX = $(shell pwd)/wine-folder

WIN_PYTHON = python-2.7.9.msi
WIN_PYGTK = pygtk-all-in-one-2.24.2.win32-py2.7.msi
WIN_PYWIN32 = pywin32-218.win32-py2.7.exe

all: pyCharGen_windows.zip pyCharGen_linux.tar.gz

wine-frozen.tar.gz: $(WIN_PYTHON) $(WIN_PYGTK) $(WIN_PYWIN32)
	wineboot -i
	wine msiexec /i $(WIN_PYTHON) /qb
	wine msiexec /i $(WIN_PYGTK) TARGETDIR=C:\\Python27 /qb
	winetricks vcrun2008 vcrun2010
	wine $(WIN_PYWIN32)
	cd $(WINEPREFIX)/drive_c/Python27 && wine python.exe -m pip install pyparsing
	cd $(WINEPREFIX)/drive_c/Python27 && wine python.exe -m pip install pyinstaller
	sleep 10
	tar -czf wine-frozen.tar.gz wine-folder
	rm -rf $(WINEPREFIX)

.SECONDARY: $(WINEPREFIX)

$(WINEPREFIX): wine-frozen.tar.gz
	tar -xzf $<

dist/pyCharGen.exe: $(WINEPREFIX) pyinst_windows.spec
	wine $(WINEPREFIX)/drive_c/Python27/python.exe \
             $(WINEPREFIX)/drive_c/Python27/Scripts/pyinstaller-script.py \
             pyinst_windows.spec
	sleep 5
	touch $@

pyCharGen_windows.zip: dist/pyCharGen.exe
	rm -rf pyCharGen_windows
	mkdir pyCharGen_windows
	cp dist/pyCharGen.exe pyCharGen_windows
	cp -r ../tables pyCharGen_windows/tables
	mkdir pyCharGen_windows/resources
	cp -r ../resources/* pyCharGen_windows/resources
	cp -r ../resources-windows/* pyCharGen_windows/resources
	zip $@ pyCharGen_windows

.INTERMEDIATE: $(WIN_PYTHON) $(WIN_PYGTK) $(WIN_PYWIN32)

$(WIN_PYTHON):
	wget "http://www.python.org/ftp/python/2.7.9/$@"

$(WIN_PYGTK):
	wget "http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.24/$@"

$(WIN_PYWIN32):
	wget "http://downloads.sourceforge.net/pywin32/$@"

venv:
	virtualenv -p $(shell which python2) venv
	venv/bin/pip install pyparsing==2.0.1
	venv/bin/pip install pyinstaller
	cd venv/lib/python2.7/site-packages && \
	    ln -s /usr/lib/python2.7/dist-packages/{glib,gobject,gtk-2.0,pygtk.pth,cairo} .

dist/pyCharGen: venv pyinst_linux.spec
	venv/bin/pyinstaller pyinst_linux.spec

pyCharGen_linux.tar.gz: dist/pyCharGen
	rm -rf pyCharGen_linux
	mkdir pyCharGen_linux
	cp dist/pyCharGen pyCharGen_linux
	cp -r ../tables pyCharGen_linux/tables
	mkdir pyCharGen_linux/resources
	cp -r ../resources/* pyCharGen_linux/resources
	if [ -d ../resources-linux ]; then cp -r ../resources-linux/* pyCharGen_linux/resources; fi
	tar -czf $@ pyCharGen_linux

clean:
	rm -rf $(WIN_PYTHON) $(WIN_PYGTK) $(WIN_PYWIN32) $(WINEPREFIX)  \
               pyCharGen_windows pyCharGen_windows.zip \
               pyCharGen_linux pyCharGen_linux.tar.gz \
               build dist venv

cleaner: clean
	rm -rf wine-frozen.tar.gz