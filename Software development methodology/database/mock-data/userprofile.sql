PRAGMA foreign_keys = ON;

create table userprofile (
	role_id INTEGER PRIMARY KEY AUTOINCREMENT,
	role_name VARCHAR(50),
	description TEXT,
	status boolean
);
insert into userprofile (role_id, role_name, description, status) values (1, 'User Admin', 'A User Admin manages all the user accounts', true);
insert into userprofile (role_id, role_name, description, status) values (2, 'Platform Manager', 'A Platform Manager manages all the volunteer categories', true);
insert into userprofile (role_id, role_name, description, status) values (3, 'Person In Need (PIN)', 'A PIN manages all their requests', true);
insert into userprofile (role_id, role_name, description, status) values (4, 'CSR Rep', 'A CSR Rep manages volunteer opportunities', true);