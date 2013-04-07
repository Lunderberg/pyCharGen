.PHONY: all docs clean

all: docs

docs: *.py
	doxygen doxy-config

clean:
	rm -rf docs *.pyc