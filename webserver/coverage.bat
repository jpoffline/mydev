@ECHO OFF
python -m coverage run --source=app -m unittest discover
python -m coverage report -m > docs/coverage_report.txt