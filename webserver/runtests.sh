echo ""
echo '* running service and unit tests together'
python -m unittest discover -p "*tests_*.py"
python -m unittest discover -p "stests_*.py"
echo '* done'
echo ''