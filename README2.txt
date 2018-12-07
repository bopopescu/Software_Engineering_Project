There are two options to run the unit tests, either hosting locally or using the instance that is being hosted on an Azure VM.
I recommend using the already running instance, installing the database drivers can be very tricky on some machines.

In either case:
1) Install Python3
2) Navigate to the Software_Engineering_Project folder
3) Run "pip install -r requirements.txt"

To host the backend API locally (Ubuntu):
1) Follow the instructions at https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017 for you OS to install the ODBC drivers
2) Navigate to the Software_Engineering_Project/Proximity-Flask folder
2) Navigate to the Software_Engineering_Project/Proximity-Flask folder
3) Run "flask run"


The API is now running locally on the flask development server. This may become stuck during some requests (known bug in the flask dev server). If the requests seem to hang for an unusually long period of time press enter and it should continue.

NOTE: Start from here if you do not want to host the server locally and instead want to use the instance running on Azure.


In a separate terminal:
1) Navigate to the unit_testing
2a) LOCAL HOSTING: run "python3 flask_unit_testing.py --local"
2b) REMOTE HOSTING: run "python3 flask_unit_testing.py --remote"
3) The results of the unit tests will print to the terminal