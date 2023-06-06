# CASH APP
Hello! This is a Cash App clone! 

# Remote Database
The remote database uses the the remote database using railway app

# Local Database
The local database uses the scripts to generate the new database and populating it.
1. Installation of `python (v.3.9)` or creating an environment
2. Installing the requirements
```
pip install -r ./requirements.txt
```
3. Create the database, populating the database and creating an admin
``` bash
$ make create-database
$ make populate-database
$ make create-admin
```
4. Accessing the database
``` bash
$ mysql -uadmin -padmin --database=127project
```

## Makefile 
The make file automate the development of the database
```
|_ make create-database
|   - script that will create the database and the tables 
|        note: that it will  not populate the database  yet
|_ make populate-database
|   - after creating the database, populating the database is next. python script that will populate the tables in the database 
|_ make create-admin
|   -  create admin user for that is granted all priveleges for all tables in the databse 
|_ make delete-database 
    - deletes the database 
```