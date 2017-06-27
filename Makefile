.PHONY: run

run:
	python3 src/main.py -e ${e}

lint:
	pycodestyle src

clean:
	find . -name \*.pyc -o -name \*.pyo -o -name __pycache__ -exec rm -rf {} +
