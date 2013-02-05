.PHONY: all docs

all: docs

docs: *.py
	doxygen doxy-config