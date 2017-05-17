# Authorization Database

### Technical specification:

- Python 2.7
- MySQL 5.7.17
- Flask 0.12.1
- Jinja2 2.9.8
- mysql-connector-python-cext 2.1.5

### EER Schema

![Screen Shot 2017-05-16 at 21.42.41](http://i.imgur.com/4Vt3Jtt.png)


### Database Schema

![Screen Shot 2017-05-16 at 21.43.40](http://i.imgur.com/B2R8Bsw.png)

	

### Execution Gudelines:

0. Install the dependencies (MySQL, Python, etc) and Create the Schema
1. Create the database using the create table statements 
2. Load initial data into the database using SQL INSERT command
3. Modify the config.py(flask app -> database -> config.py) file to update the database authorization details
4. Execute the flask application using "python2 front.py" command and go to the specified URL (http://127.0.0.1:5000/)
5. Choose the table contents to be specified from the 'table drop down list box' and press 'submit'
6. Choose the transaction you wish to perform from the 'query drop down list' and press 'submit'
7. Enter the data required for the transaction and press 'submit'

