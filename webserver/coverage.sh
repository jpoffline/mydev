
python -m coverage run --branch --source=app -m unittest discover -p "*tests_*.py"
python -m coverage html -d docs/coverage