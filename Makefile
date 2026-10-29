all:
	@echo "Pick a target"

dist:
	rm -rf dist/
	mkdir -p dist
	cp index.html dist/
	# Menus Propos
	mkdir -p dist/menus-propos
	make -C menus-propos
	cp menus-propos/index.html dist/menus-propos
	# Kanuni i Lekë Dukagjinit
	make -C kanuni-i-leke-dukagjinit
	mkdir -p dist/kanuni-i-leke-dukagjinit/sq dist/kanuni-i-leke-dukagjinit/en dist/kanuni-i-leke-dukagjinit/fr
	cp kanuni-i-leke-dukagjinit/index.html kanuni-i-leke-dukagjinit/cover.jpeg dist/kanuni-i-leke-dukagjinit/
	cp kanuni-i-leke-dukagjinit/sq/index.html dist/kanuni-i-leke-dukagjinit/sq/
	cp kanuni-i-leke-dukagjinit/en/index.html dist/kanuni-i-leke-dukagjinit/en/
	cp kanuni-i-leke-dukagjinit/fr/index.html dist/kanuni-i-leke-dukagjinit/fr/

venv:
	python3 -m venv venv
	./venv/bin/pip3 install -r requirements.txt

clean:
	rm -rf dist
	make -C menus-propos clean
	make -C kanuni-i-leke-dukagjinit clean
