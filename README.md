
# Python-SQLite
## Full-flagged Python database based on built-in SQLite package.


**DISCLAIMER: this program is not 100% done, there's still a lot of errors and warnings**
+ The program is based on [SQLite-Python Tutorial](https://www.sqlitetutorial.net/sqlite-python/) and my teacher's editing skill.
+ This program is intended for Databases module in Saxion University of Applied Sciences, Applied Computer Science major.
+ When will I continue to fix this? no fucking clue.

---
**ERRORS & WARNINGS**
``` shell
unknown column "project_id" in foreign key definition False
Traceback (most recent call last):
  File "d:/Files/Assignment/School/Databases/Week 6/databaseTest.py", line 49, in create_table
    c.execute(create_table_sql)
sqlite3.OperationalError: unknown column "project_id" in foreign key definition

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "d:/Files/Assignment/School/Databases/Week 6/databaseTest.py", line 178, in <module>
    main()
  File "d:/Files/Assignment/School/Databases/Week 6/databaseTest.py", line 151, in main
    create_table(conn, sql_create_tasks_table)
  File "d:/Files/Assignment/School/Databases/Week 6/databaseTest.py", line 52, in create_table
    print(e.__class__.__name__ + ": " + e.message)
AttributeError: 'OperationalError' object has no attribute 'message'
PS D:\Files\Assignment\School\Databases\Week 6> & "d:/Files/Assignment/School/Databases/Week 6/newPyTest/Scripts/python.exe" "d:/Files/Assignment/School/Databases/Week 6/databaseTest.py"
2.6.0
unknown column "project_id" in foreign key definition False
Traceback (most recent call last):
  File "d:/Files/Assignment/School/Databases/Week 6/databaseTest.py", line 49, in create_table
    c.execute(create_table_sql)
sqlite3.OperationalError: unknown column "project_id" in foreign key definition

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "d:/Files/Assignment/School/Databases/Week 6/databaseTest.py", line 178, in <module>
    main()
  File "d:/Files/Assignment/School/Databases/Week 6/databaseTest.py", line 151, in main
    create_table(conn, sql_create_tasks_table)
  File "d:/Files/Assignment/School/Databases/Week 6/databaseTest.py", line 52, in create_table
    print(e.__class__.__name__ + ": " + e.message)
AttributeError: 'OperationalError' object has no attribute 'message'
```
