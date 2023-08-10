#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3 as sq
import datetime


# In[3]:


con = sq.connect("contactmanagementsystem.db")


# In[4]:


cur = con.cursor()


# In[5]:


cur.execute("""create table if not exists contact
               ( cid int primary key,
                 fname text,
                 lname text,
                 contact number,
                 email text,
                 city text
                 check ( email like '%_@_%._%')
                );""")


# In[6]:


cur.execute("""create table if not exists details_log
                (
                    
                    fname text,
                    lname text,
                    newcontact number,
                    oldcontact number,
                    datetime text,
                    operation text
                    
                )""")


# In[7]:


cur.execute("""create trigger if not exists insertdata
               after insert on contact
               begin
                   insert into details_log
                   values(new.fname,new.lname,new.contact,'NULL',datetime('now'),'insert');
               end;
                   """)


# In[8]:


cur.execute("""create trigger if not exists deletedata
               after delete on contact
               begin
                   insert into details_log
                   values(old.fname,old.lname,'NULL',old.contact,datetime('now'),'delete');
               end;
                   """)


# In[9]:


cur.execute("""create trigger if not exists updatedata
               after update on contact
               begin
                   insert into details_log
                   values(new.fname,new.lname,new.contact,old.contact,datetime('now'),'update');
               end;
                   """)


# In[10]:


def updaterecord(cd):
    newcon=int(input("Enter new Contact Number:"))
    cur.execute(f"Update contact set contact={newcon} where cid={cd};")


# In[11]:


def deleterecord(cd):
    cur.execute(f"delete from contact where cid={cd}")


# In[12]:


def searchrecord(cd):
    cur.execute(f"select * from contact where cid={cd}")
    row=cur.fetchall()
    print(row)


# In[13]:


cur.execute("""insert into contact values
                (1,'parth','rathod',9874553750,'parth@gmail.com','mahuva'),
                (2,'dhrumin','rathod',2431656622,'dhrumin@gmail.com','surat'),
                (3,'dev','patel',8525842023,'dev@gmail.com','mandvi'),
                (4,'fenil','patil',8453860101,'fenil@gmail.com','vyara'),
                (5,'jenil','shah',74867357452,'jenil@gmail.com','madhi');""")


# In[14]:


updaterecord(2)


# In[15]:


deleterecord(3)


# In[16]:


cur.execute("select * from contact")
row=cur.fetchall()
for i in row:
    print(f"\nID:{i[0]}\nFname:{i[1]}\nLname:{i[2]}\nContact:{i[3]}\nEmail:{i[4]}\ncity:{i[5]}")


# In[17]:


cur.execute("select * from details_log")
row1=cur.fetchall()
print(row1)
for i in row1:
    print(f"\nFname:{i[0]}\nLname:{i[1]}\nNew-contact:{i[2]}\nOld-Contact:{i[3]}\nDatetime:{i[4]}\nOperation:{i[5]}")


# In[ ]:




