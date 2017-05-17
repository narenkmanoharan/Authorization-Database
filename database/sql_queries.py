import MySQLHelper

db_helper = MySQLHelper.MySQLHelper()


def insert_new_user(new_user_id, new_user_name, new_phone):
    insert_query = '''insert into USER_ACCOUNT(user_id,user_name,phone)VALUES(%s ,%s ,%s )''', (
        new_user_id, new_user_name, new_phone)
    db_helper.insert_data(query=insert_query)


def insert_new_role(new_role_name, new_role_description):
    insert_query = '''insert into USER_ROLE(role_name,description) VALUES(%s ,%s)''', (
        new_role_name, new_role_description)
    db_helper.insert_data(query=insert_query)


def insert_new_table(new_table_name, new_owner_id):
    insert_query = '''insert into DBTABLE(table_name,owner_id) VALUES(%s,%s)''', (new_table_name, new_owner_id)
    db_helper.insert_data(query=insert_query)


def insert_account_privilege(acc_privilege_id, create_table, create_schema, create_view, add_column, remove_column,
                             drop_table, drop_view, rename_column, rename_table):
    insert_query = '''insert into ACCOUNT_PRIVILEGE(acc_privilege_id,create_table,create_schema,create_view,add_column,remove_column,drop_table,drop_view,rename_column,rename_table) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
        acc_privilege_id, create_table, create_schema, create_view, add_column, remove_column, drop_table, drop_view,
        rename_column, rename_table)
    db_helper.insert_data(query=insert_query)


def insert_relation_privilege(rel_privilege_id, update_row, delete_row, insert_row, select_table, reference_table):
    insert_query = '''insert into RELATION_PRIVILEGE(rel_privilege_id,update_row,delete_row,insert_row,select_table,reference_table) VALUES(%s,%s,%s,%s,%s,%s)''', (
        rel_privilege_id, update_row, delete_row, insert_row, select_table, reference_table)
    db_helper.insert_data(query=insert_query)


def insert_relation_privilege_for_user_role(new_role_id, table_name):
    insert_query = '''insert into MAPS(map_role_name,map_rel_privilege_id,map_table_name) values(%s,%s,%s)''', (
        new_role_id, new_role_id, table_name)
    db_helper.insert_data(query=insert_query)


def set_role_for_user_account(new_role_id, new_user_id):
    update_query = '''update USER_ACCOUNT set role_name = %s where user_id = %s''', (new_role_id, new_user_id)
    db_helper.update_data(query=update_query)


def set_account_privilege_for_user_role(new_role_id):
    update_query = '''update USER_ROLE set role_privilege_id = %s where role_name = %s''', (new_role_id, new_role_id)
    db_helper.update_data(query=update_query)

