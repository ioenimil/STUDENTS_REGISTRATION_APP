import mysql.connector
db = mysql.connector.connect(host='127.0.0.1',
                             user='root',
                             password='ioenimil',
                             database='testdatabase')

my_cursor = db.cursor()
my_cursor.execute(f'''
    INSERT INTO students (FULL_NAME, DOB,GENDER,CLASS ,RELIGION,AGE)
    VALUES('fha', 'ghs', 'e8e', 20, 'gh', '23');

''')