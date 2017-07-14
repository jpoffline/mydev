@echo OFF
echo * running unit tests
python -m unittest discover %1 -p "utests_*.py"
echo * running service tests
python -m unittest discover %1 -p "stests_*.py"