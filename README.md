### Material Request Form
This program runs a sql query based on user input to fill out a material request form.

It first uses pyodbc and SQL with python variable injection to query an item. The program parses the information accordingly. Depending on user input, the program will write the information to an excel document, view the information in the command line, or just quit the program. 

#####DEPENDENCIES:
	* This program requires MS Excel
	* This program requires [MS ODBC driver](https://go.microsoft.com/fwlink/?linkid=2137027)
	* This program will only run within the network of Cascade Engineering Services

#####INSTALLATION:
	* To install on your computer you must first install [python](https://www.python.org/)
	* Run `pip install -r requirements.txt` to install necessary packages.
