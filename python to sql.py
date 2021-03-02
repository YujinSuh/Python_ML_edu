# # Database & SQL

# In[190]:


get_ipython().system('pip install pymysql')


# In[197]:


import pymysql.cursors
con = pymysql.connect(host = 'localhost', user = 'YUJIN', password = '0523', db = 'world')
cur = con.cursor()


# In[199]:


cur.execute('SELECT * from city') #city : table name
cur.fetchone()


# # sqlite3 연결

# In[201]:


import sqlite3
con = sqlite3.connect('emaildb.db')
cur = con.cursor()


# In[204]:


try:        
    cur.execute("DROP TABLE IF EXISTS Counts")
    cur.execute("CREATE TABLE Counts (email TEXT, count INTEGER)")
    print ('table created successfully')
except Exception as e:
    print ('error in operation, ', e)
    con.rollback() #error 원위치 , rollback 안하면 데이터 날라가고 끝남
    con.close()


# In[210]:


f = open('emailbox-short.txt','r', encoding='utf-8')
for line in f:
    if not line.startswith("From: "):
        continue
    picies = line.split()
   # print(picies)
    email = picies[1]
   # print(email)
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email, )) #tuple이 되어야함, ?안에 email이 들어가게 됨
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts(email, count) VALUES(?,1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE email=?', (email,))
        
con.commit()
        
    
    


# In[212]:


sql = 'SELECT email, count FROM Counts'
for row in cur.execute(sql):
    print(row)


# In[213]:


sql = 'INSERT INTO Counts (email, count) VALUES (?, ?)'
emails = [('test1@gmail.com', 100), ('test2@hanmail.com',10), ('test3@naver.com',1)]

cur.executemany(sql, emails)


# In[230]:


createTable = "CREATE TABLE EMP2(id varchar(32), Name varchar(32), Age int, Grade int)"
cur.execute(createTable)


# In[231]:


sql2 = 'INSERT INTO EMP2 (id, Name, Age, Grade) VALUES(?, ?, ?, ?)'
data = [('A1', '홍', 20, 70),('A2', '유', 16, 80),('A3', '김', 29, 90)]
cur.executemany(sql2,data)


# In[232]:


cur.execute('SELECT * FROM EMP2')
cur.fetchall()


# In[233]:


d4 = ('A4', '박', 25, 86)


# In[235]:


cur.execute(sql2, d4)


# In[236]:


cur.execute('SELECT * FROM EMP2')
cur.fetchall()


# In[237]:


sql3 = "UPDATE EMP2 SET Age = 59 WHERE id=='A3'"


# In[238]:


sql4 = "DELETE FROM EMP2 WHERE id == 'A1'"


# In[239]:


cur.execute(sql3)


# In[240]:


cur.execute(sql4)


# In[241]:


cur.execute('SELECT * FROM EMP2')
cur.fetchall()

## 실습

# In[ ]:


createTable = "CREATE TABLE EMP2(id varchar(32), Name varchar(32), Age int, Grade int)"
cur.execute(createTable)

sql_insert = 'INSERT INTO EMP2 (id, Name, Age, Grade) VALUES(?, ?, ?, ?)'
data = [('A1', '홍', 20, 70),('A2', '유', 16, 80),('A3', '김', 29, 90)]
cur.executemany(sql_insert,data)

cur.execute('SELECT * FROM EMP2')
cur.fetchall()

d4 = ('A4', '박', 25, 86)
cur.execute(sql_insert, d4)

cur.execute('SELECT * FROM EMP2')
cur.fetchall()

sql_update = "UPDATE EMP2 SET Age = 59 WHERE id=='A3'"
cur.execute(sql_update)

sql_delete = "DELETE FROM EMP2 WHERE id == 'A1'"
cur.execute(sql_delete)

cur.execute('SELECT * FROM EMP2')
cur.fetchall()

