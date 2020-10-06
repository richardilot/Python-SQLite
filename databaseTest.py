import sqlite3


# Creating new database
def create_connection(db_file):
    """ create a databae connection to the SQLite datababase
        specified by db_file
        :param db_file: database file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Exception as e:
        print(e, False)
        print(e.__class__.__name__ + ": " + e.message)
    finally:
        if conn:
            conn.close()

# Creating new table - part 1


def create_and_return_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
        :param db_file: database file
        :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e, False)
        print(e.__class__.__name__ + ": " + e.message)
    return conn

# Creating new table - part 2


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e, False)
        print(e.__class__.__name__ + ": " + e.message)

# Inserting data - part 1


def create_project(conn, project):
    """ Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
    """
    sql = '''INSERT INTO projects(name, begin_date, end_date) VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

# Inserting data - part 2


def create_task(conn, task):
    """ Create a new task
        :param conn:
        :param task:
        :return:
    """
    sql = ''' INSERT INTO
              tasks(name, priority, status_id, project_id, begin_date, end_date)
              VALUES(?,?,?,?,?,?)
          '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

# Updating data


def update_task(conn, task):
    """ Update priority, begin_date, and end_date of a task
        :param conn:
        :param task:
        :return:
    """
    sql = ''' UPDATE tasks
              SET priority = ?, begin_date = ?, end_date = ?
              WHERE id = ?
          '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

# Deleting data


def delete_task(conn, id):
    """ Delete a task by task id
        :param conn: Connection to the SQLite database
        :param id: id of the task
        :return:
    """
    sql = 'DELETE FROM tasks WHERE id = ?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

# Selecting data


def select_task_by_priority(conn, priority):
    """ Query tasks by priority
        :param conn: the Connection object
        :param priority:
        :return:
    """
    cur = conn.cursor()
    cur.execute()
    rows = cur.fetchall()
    for row in rows:
        print(row)


def main():
    database = "D:\\Files\\Assignment\\School\\Databases\\Week 6\\database.db"
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
            id integer PRIMARY KEY, 
            name text NOT NULL,
            begin_date text,
            end_date text ); """
    sql_create_tasks_table = """ CREATE TABLE IF NOT EXISTS tasks (
            id integer PRIMARY KEY,
            name text NOT NULL,
            priority integer,
            status_id integer NOT NULL,
            begin_date text NOT NULL,
            end_date text NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects (id) ); """
    conn = create_and_return_connection(database)
    if conn is not None:
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_tasks_table)
        conn.close()
    else:
        print("ERROR! cannot create the database connection.")

    with conn:
        project = ('App with SQLite & Python', '2015-01-01', '2015-01-30')
        project_id = create_project(conn, project)

        task_1 = ('Analyze the requirements of the app', 1,
                  1, project_id, '2015-01-01', '2015-01-02')
        task_2 = ('Confirm with user about the top requirements',
                  1, 1, project_id, '2015-01-03', '2015-01-05')
        create_task(conn, task_1)
        create_task(conn, task_2)

        update_task(conn, (2, '2015-01-04', '2015-01-06', 2))

        delete_task(conn, 2)

        print("Query task by priority:")
        select_task_by_priority(conn, 1)


if __name__ == '__main__':
    database = "D:\\Files\\Assignment\\School\\Databases\\Week 6\\database.db"
    create_connection(database)
    main()
