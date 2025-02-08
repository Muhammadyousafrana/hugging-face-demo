install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vvv --cov=hello --cov=greeting \
		--cov=smath --cov=web tests
	python -m pytest --nbval notebook.ipynb # test our jupyter notebook
	python -m pytest -v tests/test_web.py # if you want to test test_web

debug:
	python -m pytest -vv --pdb #debuger is Invoked

one_test:
	python -m pytest -vv tests/test_greeting.py::test_my_name4

debug_three:
	#not working the way i expected
	python -m pytest -vv --pdb --maxfail=4 #drop the pdb for first three failure

format:
	black *.py

lint:
	pylint --disable=R,C *.py
all:
	install lint test format