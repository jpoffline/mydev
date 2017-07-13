# jpoffline's dev webserver in python

uses flask, sqlite, and homebrews a lot of APIs.

For funs.

# Running

## Running unit tests
Uses python's `unittest` framework. Also, uses the `coverage` to determine unit test coverage over the code base.

Depending on your OS, execute
```
./rununittests.bat
./coverage.bat
```
for Windows, or 
```
./rununittests.sh
./coverage.sh
```
for Unix-based systems.
## Running the app
```
python -m app.flaskserver
```