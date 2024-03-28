from tkinter import *


class Conversion:
    
    def __init__(self,window):
        self.window = window
        self.window.wm_title('Conversion')
        
        '''Labels'''
        label = Label(window,text='Kilogram')
        label.grid(row=0,column=0)
        
        label_1 = Label(window,text = 'Gram')
        label_1.grid(row=3 ,column=0)
        
        label_2 = Label(window,text = 'Pound')
        label_2.grid(row=3 ,column=1)
        
        label_3 = Label(window,text = 'Ounce')
        label_3.grid(row=3 ,column=2)
        
        '''Button'''
        button = Button(window,text='Convert',command = self.conversion)
        button.grid(row=2,column=1)
        

        '''Entry'''  
        self.entry_value = StringVar()
        self.entrywidget = Entry(window,textvariable =  self.entry_value)
        self.entrywidget.grid(row=0,column=1)
         
        '''Text'''  
        self.textwidget = Text(window,height=1 , width=20)
        self.textwidget.grid(row=4,column=0)

        self.textwidget_1 = Text(window,height=1 , width=20)
        self.textwidget_1.grid(row=4,column=1)

        self.textwidget_2 = Text(window,height=1 , width=20)
        self.textwidget_2.grid(row=4,column=2)




    def conversion(self):
        gram=float(self.entry_value.get())*1000
        pound=float(self.entry_value.get())*2.20462
        ounce=float(self.entry_value.get())*35.274  
        self.textwidget.delete("1.0", END)
        self.textwidget.insert(END,gram)
        self.textwidget_1.delete("1.0", END)
        self.textwidget_1.insert(END,pound)
        self.textwidget_2.delete("1.0", END)
        self.textwidget_2.insert(END,ounce)



window = Tk()
Conversion(window)
window.mainloop()
