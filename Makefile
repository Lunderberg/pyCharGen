PYINSTALLER = ~/pylib/pyinstaller-2.0/pyinstaller.py
ARGS = --onefile
LIN_ARGS = 
WIN_ARGS = --windowed

.PHONY: all docs clean linux-exe

all: docs linux-exe

docs: *.py
	doxygen doxy-config

linux-exe: *.py
	$(PYINSTALLER) MainWindow.py $(ARGS) $(LIN_ARGS)

windows-exe: *.py
	wine C:\\Python27\\python.exe $(PYINSTALLER) MainWindow.py $(ARGS) $(WIN_ARGS)

clean:
	rm -rf docs *.pyc build dist logdict*.log *.spec