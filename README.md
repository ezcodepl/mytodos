# mytodos

A simple application that saves tasks into a database written in ***Python + Flask + MySql + Bootstrap 5***

If you want to store tasks in the Postgres database you must change the port in ***todo_dao.py*** file 
from ***3306(MySQL) on 5432(Postrgres)***. <br>
The library for ***Postgres - psycopg2*** is already imported into the ***todo_dao.py*** file.

If you run mytodos on Windows 10 or Windows 11 you must use this command in PyCharm terminal: <br>
***Set-ExecutionPolicy Unrestricted -Scope Process***

**How it run mytodos localy on Windows 10 or Window 11**
1. ***Set-ExecutionPolicy Unrestricted -Scope Process***<br>
2. ***./venv/Scripts/activate***
3. ***python ./app.py***

**How it run mytodos localy on Linux**
1. ***source .\venv\Scripts\activate***
2. ***python .\app.py***

**Database file database.sql make table todos**
