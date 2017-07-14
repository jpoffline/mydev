@ECHO OFF
python -m coverage run --branch --source=app -m unittest discover
python -m coverage html -d docs/coverage