'''
A program that stores this book information
Title , Author
Year, ISBN

User can:
1. view all records 
2. Search an entry
3. Add entry
4. Update entry
5. Delete
6. Close

'''


from tkinter import *
from backend import Database

database =  Database('books.db')

class Window(object):
    
    def __init__(self,window):
        self.window = window
        self.window.wm_title('BookStorage')
        
        
        #Label
        
        l1 = Label(window, text='Title')
        l1.grid(row=0,column=0)

        l2 = Label(window, text='Author')
        l2.grid(row=0, column=2)

        l3 = Label(window, text='Year')
        l3.grid(row=1, column=0)

        l4 = Label(window,  text='ISBN')
        l4.grid(row=1, column=2)




        #Entry
        self.title_text = StringVar()
        self.e1 = Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text = StringVar() 
        self.e2 = Entry(window,textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text = StringVar()
        self.e3 = Entry(window,textvariable=self.year_text)
        self.e3.grid(row=1 ,column=1)

        self.isbn_text = StringVar()
        self.e4 = Entry(window,textvariable=self.isbn_text)
        self.e4.grid(row=1,column=3)


        #listbox

        self.list1 = Listbox(window,height=6,width=35)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)


        #scrollbar
        sb1 = Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6)

        #configure sb1 and list1 to respond to each other
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        #bind
        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)


        #Button

        b1 = Button(window,text= 'View All', width= 12 , command = self.view_command)
        b1.grid(row=2,column=3)

        b2 = Button(window,text= 'Search Entry', width= 12 , command = self.search_command)
        b2.grid(row=3,column=3)

        b3 = Button(window,text= 'Add Entry', width= 12 , command = self.addentry_command)
        b3.grid(row=4,column=3)

        b4 = Button(window,text= 'Update', width = 12 , command = self.update_command)
        b4.grid(row=5,column=3)

        b5 = Button(window,text= 'Delete', width= 12 , command = self.delete_command ) 
        b5.grid(row=6,column=3)

        b6 = Button(window,text= 'Close' , width = 12 , command = window.destroy)
        b6.grid(row=7,column=3)







    def get_selected_row(self,event):
        try:
            global selected_tuple
            index = self.list1.curselection()[0]
            selected_tuple = self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,selected_tuple[4])
        except IndexError:
            pass    
        



#fucntion that grabs data from backend.py , and insert those
# data in the listbox

    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view_all():
            self.list1.insert(END,row)


    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search_entry(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
            self.list1.insert(END,row)
        
        
  
  
    def addentry_command(self):
        database.add_entry(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()) 
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))     
    
    

    def delete_command(self):
        database.delete(selected_tuple[0])


    def update_command(self):
        database.update(self.selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())

window = Tk()
Window(window)
window.mainloop()