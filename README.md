# CASH APP
Hello! This is a Cash App clone! 

# Running App
In running the app is separated by the remote and local database. But first installing the environment and the requirements
1. Installation of `python (v.3.9)` or creating an environment
2. Installing the requirements
```
pip install -r ./requirements.txt
```

## Remote Database
The remote database uses the the remote database using railway app. Thus, only needed to run the main app

3. Running the app
``` bash
make run
```

## Local Database
The local database uses the scripts to generate the new database and populating it.

3. Populating the database
``` bash
make create-database
make populate-database
make create-admin
```
4. Accessing the database
``` bash
mysql -uadmin -padmin --database=127project
```
5. Running the main app
```
make run
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
|   - deletes the database 
|_ make run
    - run the app
```