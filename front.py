from flask import Flask, render_template, request
from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime
from database import sql_queries, sql_display

# Starting the flask app
app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)

# Index page
@app.route('/')
@app.route('/index', methods=['POST'])
def index():
    return render_template('index.html')


@nocache
@app.route('/values', methods=['POST'])
def get_value():
    value = int(request.form['operations'])
    if value is 1:
        return render_template("insert_new_user.html")
    elif value is 2:
        return render_template("insert_new_role.html")
    elif value is 3:
        return render_template("insert_new_table.html")
    elif value is 4:
        return render_template("insert_new_acc_privilege.html")
    elif value is 5:
        return render_template("insert_new_rel_privilege.html")
    elif value is 6:
        return render_template("relate_role_account.html")
    elif value is 7:
        return render_template("relate_role_acc.html")
    elif value is 8:
        return render_template("relate_rel_role_table.html")
    elif value is 9:
        return render_template("disp_acc_role.html")
    elif value is 10:
        return render_template("disp_rel_role.html")
    elif value is 11:
        return render_template("disp_acc_acc.html")
    elif value is 12:
        return render_template("disp_rel_acc.html")
    elif value is 13:
        return render_template("check_acc_privilege_user_account.html")
    elif value is 14:
        return render_template("check_rel_privilege_user_account.html")


@nocache
@app.route('/tables', methods=['POST'])
def get_tables():
    value = int(request.form['tables'])
    if value is 1:
        user_id, user_name, phone, role = sql_display.user_account_table()
        return render_template('display_new_user.html', user_id=user_id, user_name=user_name, phone=phone, role=role)
    elif value is 2:
        role_name, role_desc, role_privilege_id = sql_display.user_role_table()
        return render_template('display_new_role.html', role_name=role_name, role_desc=role_desc,
                               role_privilege_id=role_privilege_id)
    elif value is 3:
        table_name, owner_id = sql_display.user_table()
        return render_template('display_new_table.html', table_name=table_name, owner_id=owner_id)
    elif value is 4:
        acc_privilege_id, create_table, create_schema, create_view, add_column, remove_column, drop_table, drop_view, rename_column, rename_table = sql_display.account_privilege_table()
        return render_template('display_new_acc_privilege.html', acc_privilege_id=acc_privilege_id,
                               create_table=create_table,
                               create_schema=create_schema, create_view=create_view, add_column=add_column,
                               remove_column=remove_column, drop_table=drop_table, drop_view=drop_view,
                               rename_column=rename_column, rename_table=rename_table)
    elif value is 5:
        rel_privilege_id, update_row, delete_row, insert_row, select_table, reference_table = sql_display.relation_privilege_table()
        return render_template('display_new_rel_privilege.html', rel_privilege_id=rel_privilege_id,
                               update_row=update_row, delete_row=delete_row, insert_row=insert_row,
                               select_table=select_table, reference_table=reference_table)

    elif value is 6:
        map_role_name, map_rel_privilege_id, map_table_name = sql_display.maps_table()
        return render_template('display_maps.html', map_role_name=map_role_name,
                               map_rel_privilege_id=map_rel_privilege_id, map_table_name=map_table_name)


@nocache
@app.route('/display_table', methods=['POST'])
def insert_table_record():
    table_name = str(request.form['table_name'])
    owner_id = int(request.form['owner_id'])
    sql_queries.insert_new_table(table_name, owner_id)
    table_name, owner_id = sql_display.user_table()
    return render_template('display_new_table.html', table_name=table_name, owner_id=owner_id)


@nocache
@app.route('/display_role', methods=['POST'])
def insert_role_record():
    role_name = str(request.form['role_name'])
    role_desc = str(request.form['role_desc'])
    sql_queries.insert_new_role(role_name, role_desc)
    role_name, role_desc, role_privilege_id = sql_display.user_role_table()
    return render_template('display_new_role.html', role_name=role_name, role_desc=role_desc,
                           role_privilege_id=role_privilege_id)


@nocache
@app.route('/role_to_acc', methods=['POST'])
def relate_role_acc():
    role_name = str(request.form['role_name'])
    sql_queries.set_account_privilege_for_user_role(role_name)
    role_name, role_desc, role_privilege_id = sql_display.user_role_table()
    return render_template('display_new_role.html', role_name=role_name, role_desc=role_desc,
                           role_privilege_id=role_privilege_id)


@nocache
@app.route('/display_user', methods=['POST'])
def insert_user_record():
    user_id = int(request.form['user_id'])
    user_name = str(request.form['user_name'])
    phone = str(request.form['phone'])
    sql_queries.insert_new_user(user_id, user_name, phone)
    user_id, user_name, phone, role = sql_display.user_account_table()
    return render_template('display_new_user.html', user_id=user_id, user_name=user_name, phone=phone, role=role)


@nocache
@app.route('/role_to_user', methods=['POST'])
def relate_role_user():
    role_name = str(request.form['role_name'])
    user_id = int(request.form['user_id'])
    sql_queries.set_role_for_user_account(role_name, user_id)
    user_id, user_name, phone, role = sql_display.user_account_table()
    return render_template('display_new_user.html', user_id=user_id, user_name=user_name, phone=phone, role=role)


@nocache
@app.route('/display_acc_privilege', methods=['POST'])
def insert_account_privilege():
    acc_privilege_id = str(request.form['acc_privilege_id'])
    create_table = int(request.form['create_table'])
    create_schema = int(request.form['create_schema'])
    create_view = int(request.form['create_view'])
    add_column = int(request.form['add_column'])
    remove_column = int(request.form['remove_column'])
    drop_table = int(request.form['drop_table'])
    drop_view = int(request.form['drop_view'])
    rename_column = int(request.form['rename_column'])
    rename_table = int(request.form['rename_table'])
    print acc_privilege_id, create_table, create_schema, create_view, add_column, remove_column, drop_table, drop_view, rename_column, rename_table
    sql_queries.insert_account_privilege(acc_privilege_id, create_table, create_schema, create_view, add_column,
                                         remove_column, drop_table, drop_view, rename_column, rename_table)
    acc_privilege_id, create_table, create_schema, create_view, add_column, remove_column, drop_table, drop_view, rename_column, rename_table = sql_display.account_privilege_table()
    return render_template('display_new_acc_privilege.html', acc_privilege_id=acc_privilege_id,
                           create_table=create_table,
                           create_schema=create_schema, create_view=create_view, add_column=add_column,
                           remove_column=remove_column, drop_table=drop_table, drop_view=drop_view,
                           rename_column=rename_column, rename_table=rename_table)


@nocache
@app.route('/display_rel_privilege', methods=['POST'])
def insert_relation_privilege():
    rel_privilege_id = str(request.form['rel_privilege_id'])
    update_row = int(request.form['update_row'])
    delete_row = int(request.form['delete_row'])
    insert_row = int(request.form['insert_row'])
    select_table = int(request.form['select_table'])
    reference_table = int(request.form['reference_table'])
    sql_queries.insert_relation_privilege(rel_privilege_id, update_row, delete_row, insert_row, select_table,
                                          reference_table)
    rel_privilege_id, update_row, delete_row, insert_row, select_table, reference_table = sql_display.relation_privilege_table()
    return render_template('display_new_rel_privilege.html', rel_privilege_id=rel_privilege_id, update_row=update_row,
                           delete_row=delete_row, insert_row=insert_row, select_table=select_table,
                           reference_table=reference_table)


@nocache
@app.route('/rel_role_table', methods=['POST'])
def relate_rel_role_table():
    role_id = str(request.form['role_id'])
    table_name = str(request.form['table_name'])
    sql_queries.insert_relation_privilege_for_user_role(role_id, table_name)
    map_role_name, map_rel_privilege_id, map_table_name = sql_display.maps_table()
    return render_template('display_maps.html', map_role_name=map_role_name, map_rel_privilege_id=map_rel_privilege_id,
                           map_table_name=map_table_name)


@nocache
@app.route('/disp_table_acc_role', methods=['POST'])
def display_account_user_role():
    role_id = str(request.form['role_name'])
    acc_privilege_id, create_table, create_schema, create_view, add_column, remove_column, drop_table, drop_view, rename_column, rename_table = sql_display.display_role_account_privilege(
        role_id)
    return render_template('display_new_acc_privilege.html', acc_privilege_id=acc_privilege_id,
                           create_table=create_table,
                           create_schema=create_schema, create_view=create_view, add_column=add_column,
                           remove_column=remove_column, drop_table=drop_table, drop_view=drop_view,
                           rename_column=rename_column, rename_table=rename_table)


@nocache
@app.route('/disp_table_rel_role', methods=['POST'])
def display_relation_user_role():
    role_id = str(request.form['role_name'])
    map_rel_privilege_id, map_table_name, update_row, delete_row, insert_row, select_table, reference_table = sql_display.display_role_relation_privilege(
        role_id)
    return render_template('disp_table_relation_role.html', map_rel_privilege_id=map_rel_privilege_id,
                           map_table_name=map_table_name, update_row=update_row,
                           delete_row=delete_row, insert_row=insert_row, select_table=select_table,
                           reference_table=reference_table)


@nocache
@app.route('/disp_acc_privilege_user_acc', methods=['POST'])
def disp_acc_privilege_user_acc():
    uid = int(request.form['user_id'])
    acc_privilege_id, create_table, create_schema, create_view, add_column, remove_column, drop_table, drop_view, rename_column, rename_table = sql_display.display_account_privilege_user_account(
        uid)
    return render_template('display_new_acc_privilege.html', acc_privilege_id=acc_privilege_id,
                           create_table=create_table,
                           create_schema=create_schema, create_view=create_view, add_column=add_column,
                           remove_column=remove_column, drop_table=drop_table, drop_view=drop_view,
                           rename_column=rename_column, rename_table=rename_table)


@nocache
@app.route('/disp_rel_privilege_user_acc', methods=['POST'])
def disp_rel_privilege_user_acc():
    uid = int(request.form['user_id'])
    user_id, map_rel_privilege_id, map_table_name, update_row, delete_row, insert_row, select_table, reference_table = sql_display.display_relation_privilege_user_account(
        uid)
    return render_template('display_relation_privilege_user_account.html', user_id=user_id,
                           map_rel_privilege_id=map_rel_privilege_id, map_table_name=map_table_name,
                           update_row=update_row, delete_row=delete_row, insert_row=insert_row,
                           select_table=select_table, reference_table=reference_table)


@nocache
@app.route('/check_acc_pri_user_account', methods=['POST'])
def check_acc_pri_user_account():
    header = str(request.form['pri_name'])
    uid = int(request.form['user_id'])
    acc_privilege_id, create_table, create_schema, create_view, add_column, remove_column, drop_table, drop_view, rename_column, rename_table = sql_display.display_account_privilege_user_account(
        uid)
    data = []
    if header == 'create_table':
        data = create_table
    elif header == 'create_schema':
        data = create_schema
    elif header == 'create_view':
        data = create_view
    elif header == 'add_column':
        data = add_column
    elif header == 'remove_column':
        data = remove_column
    elif header == 'drop_table':
        data = drop_table
    elif header == 'drop_view':
        data = drop_view
    elif header == 'rename_column':
        data = rename_column
    elif header == 'rename_table':
        data = rename_table
    return render_template('display_check_acc_pri_user_account.html', header=header, data=data)


@nocache
@app.route('/check_rel_pri_user_account', methods=['POST'])
def check_rel_pri_user_account():
    header = str(request.form['pri_name'])
    uid = int(request.form['user_id'])
    data = []
    user_id, map_rel_privilege_id, map_table_name, update_row, delete_row, insert_row, select_table, reference_table = sql_display.display_relation_privilege_user_account(
        uid)
    if header == 'update_row':
        data = update_row
    elif header == 'delete_row':
        data = delete_row
    elif header == 'insert_row':
        data = insert_row
    elif header == 'select_table':
        data = select_table
    elif header == 'reference_table':
        data = reference_table
    return render_template('display_check_rel_pri_user_account.html', user_id=user_id, map_table_name=map_table_name,
                           header=header, data=data)


# Running the application
if __name__ == '__main__':
    app.run(debug=True)
