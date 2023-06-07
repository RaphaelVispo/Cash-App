CREATE DATABASE 127project;

USE 127project;

CREATE TABLE USER (
	user_id VARCHAR (22) NOT NULL,
	user_name VARCHAR (30),
	CONSTRAINT user_userid_pk PRIMARY KEY (user_id)
);

CREATE TABLE USER_FRIEND (
	user_id VARCHAR (22) NOT NULL,
	friend VARCHAR (22) NOT NULL,
	CONSTRAINT user_friend_pk PRIMARY KEY (user_id, friend)
);

CREATE TABLE USER_HAS_GROUP_EXPENSE (
	user_id VARCHAR (22) NOT NULL,
	group_id VARCHAR (22) NOT NULL,
	expense_id VARCHAR (22) NOT NULL,
CONSTRAINT user_has_group_expense_pk PRIMARY KEY (user_id, group_id, expense_id)
);

CREATE TABLE HAS_GROUP (
	group_id VARCHAR (22) NOT NULL,
	group_name VARCHAR (30),
	CONSTRAINT group_group_id_pk PRIMARY KEY (group_id)
);

CREATE TABLE EXPENSE (
	expense_id VARCHAR (22) NOT NULL,
	creditor VARCHAR (22),
	amount INT (10),
	is_settled BOOLEAN,
	expense_date DATE,

	CONSTRAINT expense_expense_id_pk PRIMARY KEY (expense_id)
);
