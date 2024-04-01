'''
Creating backend for the frontend

Here, we create functions for each 
of the button variable to perform a 
specific task .

We call that function in the frontend to
be executed by the command parameter

The backend is created with sqlite3 to store
databases
Database Interaction
'''


import sqlite3

class Database:
    
    
    
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur =  self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text , author text, year integer, isbn integer)')
        self.conn.commit()
        

    
    def add_entry(self,title,author,year,isbn):
        self.cur.execute('INSERT INTO book VALUES(NULL,?,?,?,?)',(title,author,year,isbn))
        self.conn.commit()
        
        
        
    def view_all(self):
        self.cur.execute('SELECT * FROM book')
        rows = self.cur.fetchall()
        return rows    


    def search_entry(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,author))
        rows = self.cur.fetchall()
        return rows
    
    def delete(self,id): 
        self.cur.execute('DELETE FROM book WHERE id=?',(id,))
        self.conn.commit()


    def update(self,id,title,author,year,isbn):   
        self.cur.execute('UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?',(title,author,year,isbn,id))
        self.conn.commit() 
    
    
    def __del__(self):
        self.conn.close()
    

#update(1,'The universe','Lewis Smooth',1998,85426947) 
#add_entry('Jump','chris',2000 ,87986564908)
# delete(4)
#print(view_all())
#print(search_entry(author='chris'))

   
    