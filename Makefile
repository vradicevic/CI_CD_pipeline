setup:
	python3 -m venv ~/.udacity-devops

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python3 -m pytest -vv --test_hello.py

lint:
	pylint --disable=R,C,W1203 hello.py

all: install lint test