echo '========================='
echo '  Running testing suite'
echo '========================='
echo 'Service tests'
python -m tests.run_service_tests -quiet
echo 'Unit tests'
python -m tests.run_unit_tests -quiet
echo 'DONE'
echo ''