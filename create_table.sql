create table USER_ACCOUNT (
    user_id int,
    user_name varchar(25) not null,
    phone varchar(12),
    role_name varchar(30),
    PRIMARY KEY(user_id),
    FOREIGN KEY(role_name) REFERENCES SECURITY_DATABASE.USER_ROLE(role_name));

create table DBTABLE (
    table_name varchar(25),
    owner_id int,
    PRIMARY KEY(table_name),
    FOREIGN KEY(owner_id) REFERENCES 
    SECURITY_DATABASE.USER_ACCOUNT(user_id));

create table USER_ROLE (
    role_name varchar(30),
    description varchar(50),
    role_privilege_id varchar(25),
    PRIMARY KEY(role_name),
    FOREIGN KEY(role_privilege_id) REFERENCES 
    SECURITY_DATABASE.ACCOUNT_PRIVILEGE(acc_privilege_id));

create table ACCOUNT_PRIVILEGE (
    acc_privilege_id varchar(25),
    create_table boolean,
    create_schema boolean,
    create_view boolean,
    add_column boolean,
    remove_column boolean,
    drop_table boolean,
    drop_view boolean,
    rename_column boolean,
    rename_table boolean,
    PRIMARY KEY(acc_privilege_id));

create table RELATION_PRIVILEGE (
    rel_privilege_id varchar(30),
    update_row boolean,
    delete_row boolean,
    insert_row boolean,
    select_table boolean,
    reference_table boolean,
    PRIMARY KEY(rel_privilege_id));

create table MAPS(

    map_role_name varchar(30),
    map_rel_privilege_id varchar(25),
    map_table_name varchar(25),
	
    FOREIGN KEY(map_role_name) REFERENCES 
    SECURITY_DATABASE.USER_ROLE(role_name),

    FOREIGN KEY(map_rel_privilege_id) REFERENCES 
    SECURITY_DATABASE.RELATION_PRIVILEGE(rel_privilege_id),

    FOREIGN KEY(map_table_name) REFERENCES SECURITY_DATABASE.DBTABLE  (table_name),

    PRIMARY KEY(map_role_name,map_rel_privilege_id,map_table_name));
