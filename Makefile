

create-admin:
	echo 'Creating user'
	sudo mysql < scripts/create-admin.sql
	echo 'Creating '

create-database: 
	echo 'Creating the database...'
	sudo mysql  < scripts/create-database.sql
	echo 'Creating database DONE: !!!'

delete-database:
	echo 'Delete the database ... '
	sudo mysql < scripts/delete-database.sql
	echo 'Deleting the database: DONE!!'

populate-tables:
	echo 'Populating the tables ...'

	echo 'Populating the tables: DONE !!'