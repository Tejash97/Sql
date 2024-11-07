import sqlite3


connection=sqlite3.connect("students.db")


cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)


cursor.execute('''Insert Into STUDENT values('Tejash','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sanket','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Ritesh','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vick','LLB','A',50)''')
cursor.execute('''Insert Into STUDENT values('Sandeep','DEVOPS','C',35)''')
cursor.execute('''Insert Into STUDENT values('Aanal','BCOM','D',35)''')
cursor.execute('''Insert Into STUDENT values('Yash','BBA','E',45)''')
cursor.execute('''Insert Into STUDENT values('Ritik','CS','B',67)''')
cursor.execute('''Insert Into STUDENT values('Sahil','12','A',76)''')
cursor.execute('''Insert Into STUDENT values('Mayank','PILOT','A',87)''')
cursor.execute('''Insert Into STUDENT values('Shivam','CA','C',45)''')



print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)


connection.commit()
connection.close()