PYTHON ?= ../venv/bin/python

all: index.html sq/index.html en/index.html fr/index.html

index.html: index.md template.html build.py
	$(PYTHON) build.py index

sq/index.html: sq/kanuni.md sq/front.md template.html build.py
	$(PYTHON) build.py sq

en/index.html: en/kanuni.md en/front.md en/glossary.md template.html build.py
	$(PYTHON) build.py en

fr/index.html: fr/kanuni.md fr/front.md fr/glossary.md template.html build.py
	$(PYTHON) build.py fr

clean:
	rm -f index.html */index.html
