import random
import pyrebase
from tkinter import *
import math

#toothpicl size = 100
config = {
            "apiKey" : 'AIzaSyCYnqLsQHZK0d1QIKACc1NCvXSOWwfSDZM',
            'authDomain' : 'test-b438a.firebaseapp.com',
            'databaseURL' : "https://test-b438a-default-rtdb.firebaseio.com",
            'storageBucket' : 'test-b438a.appspot.com'
        }
firebase = pyrebase.initialize_app(config).database( )
class Mywindow:
    def __init__(self,win):
        #init
        self.alltime=0
        self.over= 0

        self.canva = Canvas(win,width=500,height=500,bg='white')
        self.canva.grid(row = 0,column = 0,rowspan = 5)

        self.lbl1 = Label(win,text='Number of random.',font = ('Courier',15))
        self.lbl1.grid(row = 0,column = 1)

        self.enumberofrandom = Entry(win,font = ('Courier',15))
        self.enumberofrandom.grid(row = 0,column = 2,padx = 10)

        self.btnenter = Button(win,text= 'Enter',font = ('Courier',15),command = self.btnclikced)
        self.btnenter.grid(row=0,column = 3,padx = 10)

        self.lbl3 = Label(win,text = 'You was random for',font = ('Courier',15))
        self.lbl3.grid(row=1,column = 1)

        self.lbl4 = Label(win,text = 'times.',font = ('Courier',15))
        self.lbl4.grid(row = 1,column = 3)

        self.lblalltimes = Label(win,text = '0',font = ('Courier',15))
        self.lblalltimes.grid(row = 1,column = 2)

        self.lbl2 = Label(win,text = 'Pi value ',font = ('Courier',15))
        self.lbl2.grid(row = 2,column = 1,)
        
        self.lblvaluepi = Label(win,text = 'INF',font = ('Courier',15),fg = 'red',anchor = W)
        self.lblvaluepi.grid(row = 2,column = 2,columnspan = 2)

        self.lbl4 = Label(win,text = 'Accuracy',font = ('Courier',15))
        self.lbl4.grid(row = 3,column = 1)

        self.lblacculate = Label(win,text = '0',font = ('Courier',15))
        self.lblacculate.grid(row = 3,column  = 2,columnspan = 2)

        self.btnloadvalue  = Button(win,text='Load data from data base.',font = ('Courier',15),padx = 100,command = self.load_data)
        self.btnloadvalue.grid(row = 4,column  =1,columnspan = 3)

        self.setline( )

    def load_data(self):
        self.alltime = int(firebase.child('/all').get( ).val( ))
        self.over = int(firebase.child('/over').get( ).val( ))
        self.lblalltimes.config(text = str(self.alltime))
        self.lblvaluepi.config(text = "%8.7f"%(2*self.alltime / self.over))
        self.lblacculate.config(text = str(100 - (abs(math.pi - 2*self.alltime / self.over))/math.pi*100))
    def btnclikced(self):
        number = int(self.enumberofrandom.get( ))
        self.enumberofrandom.delete(0,'end')
        for _ in range(number):
            x = 500 * random.random()
            y = 500 * random.random()
            h = math.pi * random.random( ) * random.choice([-1,1])
            x2 = x + math.sin(h) * 50
            y2 = y + math.cos(h) * 50
            if y//50 != y2//50:
                self.canva.create_line(x,y,x2,y2,fill = 'red')
                self.over +=1
            else:
                self.canva.create_line(x,y,x2,y2,fill = 'blue')
            self.alltime+=1
            if self.alltime %10000 == 0:
                self.canva.delete('all')
                self.setline( )
            self.lblalltimes.config(text = str(self.alltime),fg = 'red')
            if self.over != 0:
                self.lblvaluepi.config(text = "%6.5f"%(2*self.alltime / self.over))
                self.lblacculate.config(text = "%6.5f"%(100 - (abs(math.pi - 2*self.alltime / self.over))/math.pi*100))
            self.canva.update( )
        self.lblalltimes.config(fg = 'black')
    def setline(self):
        for i in range(1,11):
            self.canva.create_line(0,50*i,500,50*i)


window = Tk( )
mywindow = Mywindow(window)
window.mainloop( )
