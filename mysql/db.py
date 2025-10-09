import mysql.connector
from mysql.connector import IntegrityError

# connecting to a database
con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "test",
    port = 3306
)

print('Hey I think I am connected')

# cursor
cur = con.cursor()

# execute the query
cur.execute("select * from employees")

rows = cur.fetchall()

for r in rows:
    print(f"row is {r}\n")


cur.execute("select employee_id,first_name, last_name, email from employees where employee_id = %s", (1,))
rows2 = cur.fetchall()
for r in rows2:
    print(f"employee is {r}\n")


try:
    cur.execute("""
    INSERT INTO employees 
    (first_name, last_name, email, phone, hire_date, job_title, salary, department)
    VALUES ('David', 'Wilson', 'david.wilson@example.com', '555-1111', '2019-11-18', 'HR Specialist', 60000.00, 'Human Resources')
    """)
    con.commit()
except IntegrityError:
    print("Duplicate email found, ignoring insert.")

# commit the transaction
con.commit()

cur.execute("select count(*) from employees")
rows3 = cur.fetchall()

for r in rows3:
    print(f"employee count {r}\n")

cur.execute("select count(*) from employees")
count,  = cur.fetchone()
print(f"employee count {count}\n")

# close the cursor
cur.close()

# closing the connection
con.close()