PY = python

test:
	$(PY) -m unittest discover
	make clean

install:
	$(PY) -m pip install --upgrade pip
	pip install -r requirements.txt
	$(PY) setup.py install

upload:
	$(PY) -m pip install --upgrade pip
	pip install setuptools wheel twine
	$(PY) setup.py sdist bdist_wheel
	twine upload dist/*

clean:
	pyclean .
