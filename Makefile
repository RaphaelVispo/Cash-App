

create-admin:
	echo 'Creating user ...'
	sudo mysql < scripts/local/create-admin.sql
	echo 'Creating '

create-database: 
	echo 'Creating the database ...'
	sudo mysql  < scripts/local/create-database.sql
	echo 'Creating database DONE: !!!'

delete-database:
	echo 'Delete the database ... '
	sudo mysql < scripts/local/delete-database.sql
	echo 'Deleting the database: DONE!!'

populate-database:
	echo 'Populating the tables ...'
	python scripts/local/populate-database.py
	echo 'Populating the tables: DONE !!'

run:
	python3 src/main.py

clean:
	yapf -i ./src/*.py