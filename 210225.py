#!/usr/bin/env python
# coding: utf-8

# # import module

# In[1]:


import math


# In[3]:


dir(math)


# In[4]:


math.exp(2)


# In[7]:


print(math.floor(3.49)) #내림
print(math.ceil(3.49)) #올림
print(round(3.49)) #반올림


# In[8]:


import turtle


# In[10]:


ls = ['cat','dog', 'monkey','cat','dog','cat']
d={}
for word in ls:
    if word not in d:
        d[word] = 0
    d[word] += 1
print(d)


# In[11]:


d = {}
for word in ls:
    d[word] = d.get(word,0)+1
d


# In[ ]:





# In[12]:


from collections import Counter


# In[16]:


counts = Counter(ls)
counts


# In[17]:


counts['cat']


# In[18]:


import sys


# In[19]:


sys.path.append('./path_test') #path 임의 추가


# In[20]:


sys.path


# In[24]:


import sys
sys.path.append('../')


# In[25]:


import boilerplate


# In[27]:


boilerplate.hello('ㅠ')


# # 객체지향개발 (OOP - Object Oriented Programming)

# In[29]:


print(type('sting aaa'))
print(type('100.1'))


# In[30]:


x = 'sting aaa'
x.upper()


# In[54]:


class Car:
    def __init__(self, color, size, price):

        self.color = color
        self.size = size
        self.price = price
        self.output()
        
    def output(self):
        print(self.color)
        print(self.size)
        
    def speedCheck(self,speed):
        self.speed = speed
        if speed > 100:
            print('과속')
        else:
            print('good speed')


# In[56]:


# car1 = Car('sonata')
# car1.output()
# car1.speedCheck(130)


# In[57]:


print(type(car1))


# In[58]:


car2 = Car('blue',100,10000)


# In[65]:


class Sonata(Car):
    def __init__(self, color, size, price, maker):
        super().__init__(color,size,price)
        self.maker = maker
        
        


# In[67]:


car4.speedCheck(200)


# In[66]:


car4 = Sonata('red',200, 15000,'Hyundai')


# In[72]:


class Korean:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("나 {}는 한국말을 한다".format(self.name))
    
    def sex(self):
        print("성별은 남녀")
        
    def __call__(self, x):
        x+=1
        print(x)
        
    
    
    
class Man(Korean):
    def sex(self):
        print("{}는 한국남자".format(self.name))
        
class Woman(Korean):
    def sex(self):
        print("{}는 한국여자".format(self.name))


# In[70]:


A = Man('철수')
A.sex()


# In[71]:


B = Woman('영희')
B.sex()


# In[74]:


a = Korean('calltest')
a(10)


# In[78]:


# class Korean: #parent class
#     def speak(self):
#         print("I can speak Korean")
#     def __str__(self):
#         return "Print using"
#     def __repr__(self):
#         return "object using"
    
# A.Korean()


# In[ ]:


class Person:   
    
    class_var = '클라스변수'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show_salary(self):
        print("Salary is unknown")

class Employee(Person):
    def __init__(self, name, age, salary):   # Person 의 __init__() override
        super().__init__(name, age)          # Person 의 __init__() 내용을 상속
        self.salary = salary
        
    def show_salary(self):          # Person 의 show_salary() override
        print( "{}'s salary is {} and age is {}"
                  .format(self.name, self.salary, self.age))
        
A = Person('Tom', 30)
A.show_salary()

B = Employee('Tom', 30, 10000)
B.show_salary()


# # 다중 상속

# In[79]:


class Person:
    def greeting(self):
        print('안녕')
    
class University:
    def manage_grade(self):
        print('학점관리')
        


# In[80]:


class Student(Person, University):
    def study(self):
        print("열공")


# In[81]:


s= Student()
s.study()
s.greeting()
s.manage_grade()


# In[90]:


class Employee:
    
    raise_rate = 1.0
    
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
        
    def apply_raise(self):
        self.pay = self.pay * self.raise_rate
        print(self.pay)
        
    @classmethod
    def change_rate(cls, rate): #()안의 변수는 노상관
        cls.raise_rate = rate
        print(cls.raise_rate)
        
    @staticmethod
    def calc_tax(amount, tax_rate):
        print(amount * tax_rate)
        


# In[92]:


employee1 = Employee('YJ', 5000)
employee1.apply_raise()


# In[93]:


employee1.calc_tax(10000,0.1)


# In[ ]:





# In[88]:


employee2 = Employee('CS', 5500)
employee2.change_rate(3.0)
employee2.apply_raise()


# # 연습문제

# In[103]:


class Car:
    def __init__(self, color='red', power=2000):
        self.color = color
        self.power = power
        self.speed = 0

    def forward(self, speed):
        self.speed += speed
        return '앞으로 전진 : 시속 {} km'.format(self.speed)

    def backward(self):
        pass

class Sonata(Car):
    def __init__(self, color, power, size):
        super().__init__(color,power)
        self.size = size
        
    def backward(self, speed):
        self.speed = self.speed - speed
        return '뒤로 후진 : {} km/hour'.format(self.speed)
        
class Volvo(Car):
    def __init__(self, color, power, size, price):
        super().__init__(color,power)
        self.size = size
        self.price = price

    def forward(self, speed):
        self.speed = self.speed + speed + 100
        return '앞으로 전진 : 시속 {} km'.format(self.speed)
        
        
    def backward(self):
        print("후진 불가")
        
        
sonata = Sonata('black', 1800, 5)
volvo = Volvo('white', 2500, 7, 5000000)

print(sonata.color)
print(sonata.forward(100))
print(sonata.backward(30))

print(volvo.color)
print(volvo.price)
print(volvo.forward(100))
print(volvo.backward())


# # file open

# In[106]:


fh = open("testworks.txt","w", encoding = "utf-8")
fh.write("첫번째 RECORD\n")
fh.write("2nd record\n")
fh.write("last line")
fh.close()


# In[108]:


f = open("testworks.txt","r", encoding = "utf-8") #encoding = "utf-8"은 windows에서 꼭 필요, mac에선 불필요
text = f.read()
print(text)


# In[111]:


f = open("testworks.txt","rb")
text2 = f.read()
text2


# In[116]:


f = open("testworks.txt","rt", encoding = "utf-8")
lines = f.readlines() #list로 읽기
# for line in f:
#     print(line)
# 와 동일한 형태로 출력

lines #list 형태

for line in lines:
    print(line.strip())


# In[117]:


dir("aaa")


# In[121]:


f = open("emailbox-short.txt", "r")
count = 0
for line in f:
    if line.startswith("From:"):
        print(line.strip())  #줄바꿈 줄이기위해 line대신 line.strip()
        count+=1
print(count)


# In[122]:


import os
os.listdir()


# In[123]:


get_ipython().system('pip install beautifulsoup4')


# In[126]:


os.path.abspath('testworks.txt') #절대 경로!!


# In[130]:


dir_name = os.path.dirname(os.path.abspath('testworks.txt'))
dir_name


# In[140]:


sub_dir_name = os.path.join(dir_name, "boilerplate.py")
sub_dir_name


# In[141]:


os.path.exists(sub_dir_name)


# In[143]:


try:
    with open('testworks.txt','r', encoding = 'utf-8') as f:
        data = f.read()
except Exception as e:
    print("error= ", e)
    
    # encoding = 'utf-8' 누락 에러구나~ 확인용


# # 특정 에러

# In[147]:


try:
    with open('testworks.txt','r', encoding = 'utf-8') as f:
        data = f.read()
        #x=10/0
        y = int(input("숫자 입력"))
except ZeroDivisionError:
    print("0으로 나눔")
except ValueError:
    print("value error")


# In[ ]:





# # assert 

# In[148]:


x = 5
assert x%3 ==0, '3의 배수 아님'


# In[149]:


try:
    os.remove("testworks.txt")
except Exception as e:
    print (e)
    


# In[166]:


counts={}
with open('poet.txt','r') as f:
    for line in f:
        for word in line.split():
            counts[word] = counts.get(word,0)+1
            
sorted(counts.items(), key = lambda kv:kv[1], reverse = True)[:10]


# In[ ]:





# ### 밑에는 연습용 

# In[159]:


f = open('poet.txt', 'r')  # text mode

lines = f.readlines()
count = {}
for line in lines:
    sent = line.rstrip()
    word = sent.split()
    count[word]=Counter(word)

count ={}

#print(lines)
#Counter(lines)


# # list comprehension

# In[174]:


x=[]
for i in range(10):
    x.append(i)
    
x


# In[176]:


x = [i for i in range(10)]
x #더빠르고 간단


# In[178]:


x = [i**2 for i in range(10)]
x


# In[180]:


strs = ['hello','good','bye']
shout = [s.upper()+'!!!' for s in strs]
shout


# In[181]:


nums = [2,4,6,8,10]
small = [x for x in nums if x<5]
small


# In[185]:


fruits = ['apple','banna','cherry','lemon']
[fruit for fruit in fruits if 'a' in fruit]


# In[184]:


ls = [i for i in range(10)]
[x if x>5 else x**2 for x in ls]


# In[186]:


d = {'a':1, 'b':2, 'c':3}
id = {}
for k, v in d.items():
    id[v] = k
id


# In[189]:


id = {v: k for k, v in d.items()}
id


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

