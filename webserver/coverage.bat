@ECHO OFF
python -m coverage run --source=app -m unittest discover
python -m coverage html -d docs/coverage