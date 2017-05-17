import MySQLHelper

db_helper = MySQLHelper.MySQLHelper()


def user_account_table():
    user_id = []
    user_name = []
    phone = []
    role = []
    display_query = '''select * from USER_ACCOUNT'''
    cnx = db_helper.get_connection()
    cursor = cnx.cursor(buffered=True)
    cursor.execute(display_query)
    cnx.commit()
    result = cursor.fetchall()
    for row in result:
        user_id.append(int(row[0]))
        user_name.append(str(row[1]))
        phone.append(str(row[2]))
        role.append(str(row[3]))
    return user_id, user_name, phone, role


def user_role_table():
    role_name = []
    role_desc = []
    role_privilege_id = []
    display_query = '''select * from USER_ROLE'''
    cnx = db_helper.get_connection()
    cursor = cnx.cursor(buffered=True)
    cursor.execute(display_query)
    cnx.commit()
    result = cursor.fetchall()
    for row in result:
        role_name.append(str(row[0]))
        role_desc.append(str(row[1]))
        role_privilege_id.append(str(row[2]))
    return role_name, role_desc, role_privilege_id


def user_table():
    table_name = []
    owner_id = []
    display_query = '''select * from DBTABLE'''
    cnx = db_helper.get_connection()
    cursor = cnx.cursor(buffered=True)
    cursor.execute(display_query)
    cnx.commit()
    result = cursor.fetchall()
    for row in result:
        table_name.append(str(row[0]))
        owner_id.append(int(row[1]))
    return table_name, owner_id


def account_privilege_table():
    acc_privilege_id = []
    create_table = []
    create_schema = []
    create_view = []
    add_column = []
    remove_column = []
    drop_table = []
    drop_view = []
    rename_column = []
    rename_table = []
    display_query = '''select * from ACCOUNT_PRIVILEGE'''
    cnx = db_helper.get_connection()
    cursor = cnx.cursor(buffered=True)
    cursor.execute(display_query)
    cnx.commit()
    result = cursor.fetchall()
    for row in result:
        acc_privilege_id.append(str(row[0]))
        create_table.append(int(row[1]))
        create_schema.append(int(row[2]))
        create_view.append(int(row[3]))
        add_column.append(int(row[4]))
        remove_column.append(int(row[5]))
        drop_table.append(int(row[6]))
        drop_view.append(int(row[7]))
        rename_column.append(int(row[8]))
        rename_table.append(int(row[9]))
    return acc_privilege_id, create_table, create_schema, create_view, add_column, remove_column, drop_table, drop_view, rename_column, rename_table


def relation_privilege_table():
    rel_privilege_id = []
    update_row = []
    delete_row = []
    insert_row = []
    select_table = []
    reference_table = []
    display_query = '''select * from RELATION_PRIVILEGE'''
    cnx = db_helper.get_connection()
    cursor = cnx.cursor(buffered=True)
    cursor.execute(display_query)
    cnx.commit()
    result = cursor.fetchall()
    for row in result:
        rel_privilege_id.append(str(row[0]))
        update_row.append(int(row[1]))
        delete_row.append(int(row[2]))
        insert_row.append(int(row[3]))
        select_table.append(int(row[4]))
        reference_table.append(int(row[5]))
    return rel_privilege_id, update_row, delete_row, insert_row, select_table, reference_table


def maps_table():
    map_role_name = []
    map_rel_privilege_id = []
    map_table_name = []
    display_query = '''select * from MAPS'''
    cnx = db_helper.get_connection()
    cursor = cnx.cursor(buffered=True)
    cursor.execute(display_query)
    cnx.commit()
    result = cursor.fetchall()
    for row in result:
        map_role_name.append(str(row[0]))
        map_rel_privilege_id.append(str(row[1]))
        map_table_name.append(str(row[2]))
    return map_role_name, map_rel_privilege_id, map_table_name


def display_role_account_privilege(roleid):
    acc_privilege_id = []
    create_table = []
    create_schema = []
    create_view = []
    add_column = []
    remove_column = []
    drop_table = []
    drop_view = []
    rename_column = []
    rename_table = []
    cnx = db_helper.get_connection()
    cursor = cnx.cursor(buffered=True)
    cursor.execute('''select * from ACCOUNT_PRIVILEGE where acc_privilege_id = %s''', (roleid,))
    cnx.commit()
    result = cursor.fetchall()
    for row in result:
        acc_privilege_id.append(str(row[0]))
        create_table.append(int(row[1]))
        create_schema.append(int(row[2]))
        create_view.append(int(row[3]))
        add_column.append(int(row[4]))
        remove_column.append(int(row[5]))
        drop_table.append(int(row[6]))
        drop_view.append(int(row[7]))
        rename_column.append(int(row[8]))
        rename_table.append(int(row[9]))
    return acc_privilege_id, create_table, create_schema, create_view, add_column, remove_column, drop_table, drop_view, rename_column, rename_table


def display_role_relation_privilege(roleid):
    map_rel_privilege_id = []
    map_table_name = []
    update_row = []
    delete_row = []
    insert_row = []
    select_table = []
    reference_table = []
    cnx = db_helper.get_connection()
    cursor = cnx.cursor(buffered=True)
    cursor.execute(''' select map_rel_privilege_id,map_table_name,update_row,delete_row,insert_row,select_table,reference_table from RELATION_PRIVILEGE,MAPS where rel_privilege_id = %s and map_rel_privilege_id = %s''',
        (roleid, roleid))
    cnx.commit()
    result = cursor.fetchall()
    for row in result:
        map_rel_privilege_id.append(str(row[0]))
        map_table_name.append(str(row[1]))
        update_row.append(int(row[2]))
        delete_row.append(int(row[3]))
        insert_row.append(int(row[4]))
        select_table.append(int(row[5]))
        reference_table.append(int(row[6]))
    return map_rel_privilege_id, map_table_name, update_row, delete_row, insert_row, select_table, reference_table


def display_account_privilege_user_account(uid):
    acc_privilege_id = []
    create_table = []
    create_schema = []
    create_view = []
    add_column = []
    remove_column = []
    drop_table = []
    drop_view = []
    rename_column = []
    rename_table = []
    cnx = db_helper.get_connection()
    cursor = cnx.cursor(buffered=True)
    cursor.execute('''select * from ACCOUNT_PRIVILEGE where acc_privilege_id in (select role_name from USER_ACCOUNT where user_id = %s)''',
        (uid,))
    cnx.commit()
    result = cursor.fetchall()
    for row in result:
        acc_privilege_id.append(str(row[0]))
        create_table.append(int(row[1]))
        create_schema.append(int(row[2]))
        create_view.append(int(row[3]))
        add_column.append(int(row[4]))
        remove_column.append(int(row[5]))
        drop_table.append(int(row[6]))
        drop_view.append(int(row[7]))
        rename_column.append(int(row[8]))
        rename_table.append(int(row[9]))
    return acc_privilege_id, create_table, create_schema, create_view, add_column, remove_column, drop_table, drop_view, rename_column, rename_table


def display_relation_privilege_user_account(uid):
    user_id = []
    map_rel_privilege_id = []
    map_table_name = []
    update_row = []
    delete_row = []
    insert_row = []
    select_table = []
    reference_table = []
    cnx = db_helper.get_connection()
    cursor = cnx.cursor(buffered=True)
    cursor.execute(
        '''select USER_ACCOUNT.user_id,map_rel_privilege_id,map_table_name,update_row,delete_row,insert_row,select_table,reference_table from RELATION_PRIVILEGE,MAPS,USER_ACCOUNT where rel_privilege_id in (select role_name from USER_ACCOUNT where user_id = %s) and map_rel_privilege_id in (select role_name from USER_ACCOUNT where user_id = %s) and USER_ACCOUNT.user_id = %s ''',
        (uid, uid, uid))
    cnx.commit()
    result = cursor.fetchall()
    for row in result:
        user_id.append(int(row[0]))
        map_rel_privilege_id.append(str(row[1]))
        map_table_name.append(str(row[2]))
        update_row.append(int(row[3]))
        delete_row.append(int(row[4]))
        insert_row.append(int(row[5]))
        select_table.append(int(row[6]))
        reference_table.append(int(row[7]))
    return user_id, map_rel_privilege_id, map_table_name, update_row, delete_row, insert_row, select_table, reference_table
