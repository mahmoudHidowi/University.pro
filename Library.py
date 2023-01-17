from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb
from tkcalendar import Calendar
from DateTime import *
from datetime import date
from main import book 
from UniversityInfo import universityinfo
class library:
    
    def __init__(self,bf):
             
        self.libraryFrame = Frame(bf, pady=0, padx=20)
        self.libraryFrame.grid(row=1, column=0, sticky='senw')
        self.img4 = Image.open('images/open-book.png')
        self.img4.thumbnail((180, 180))
        self.new_img4 = ImageTk.PhotoImage(self.img4)
        self.imgLibrary = Label(self.libraryFrame, image=self.new_img4, padx=10, pady=10)
        self.imgLibrary.pack()
        self.buttonLibrary = Button(self.libraryFrame, command=self.openlibrarywindow, font=('tahoma', "11", 'bold'),
                                    text='Library Management',fg="#242423",bg="#F5CB5C", padx=10, pady=10)
        self.buttonLibrary.pack()
        
    def openlibrarywindow(self):
        libw = libraryWindow()
        
class libraryWindow:
   
    def __init__(self,password,id,libraryname,floornumber,sectionnumber,uniname,craetdate,presencecity,bookname,author,pagenambers):
        
        self.adminpassword=password
        self.adminid=id 
         
        self.Uuniname=uniname
        self.Ucreatdate=craetdate
        self.Upresencecity=presencecity
        
        self.Bookbookname=bookname
        self.Bookauthor=author
        self.Bookpagenambers=pagenambers
        self.Bookid=id
        
        self.Llibraryname=libraryname
        self.lfloornumber=floornumber
        self.lsectionnumber=sectionnumber
        self.lid=id
        
        self.b=book()
        self.u=universityinfo()
        
    def __init__(self):
         
        self.master = Toplevel()
        self.master.title('Library Management System')
        self.master.geometry("1200x800+80+0")
        
        self.frameleft = Frame(self.master,bg="#CFDBD5", width=400)
        self.frameleft.pack(side=LEFT, fill=BOTH)
       
        self.nameLabel=Label(self.frameleft,text='Student Name :',bg="#CFDBD5",fg="#242423",font=('tahoma',12,'bold'))
        self.nameLabel.place(x=15,y=20,width=130,height=40)
        self.phoneLabel = Label(self.frameleft, text='Phone :',bg="#CFDBD5",fg="#242423", font=('tahoma', 12, 'bold'))
        self.phoneLabel.place(x=15, y=80, width=120, height=40)
        self.NameBookLabel = Label(self.frameleft, text='Book Name :',bg="#CFDBD5",fg="#242423", font=('tahoma', 12, 'bold'))
        self.NameBookLabel.place(x=15, y=140, width=120, height=40)
        self.datedLabel = Label(self.frameleft, text='Delivery Date :',bg="#CFDBD5",fg="#242423", font=('tahoma', 12, 'bold'))
        self.datedLabel.place(x=15, y=200, width=130, height=40)
        self.daterLabel = Label(self.frameleft, text='Return Date :',bg="#CFDBD5",fg="#242423", font=('tahoma', 12, 'bold'))
        self.daterLabel.place(x=15, y=415, width=120, height=40)
        self.name=StringVar()
        self.phone = StringVar()
        self.book = StringVar()
        self.delivery=StringVar()
        self.returnn = StringVar()

        self.nameStudent = Entry(self.frameleft,bg="white",fg="#515A5A",font=('tahoma',12,'bold'),textvariable=self.name)
        self.nameStudent.place(x=170,y=20,width=200,height=40)
        self.phoneStudent = Entry(self.frameleft,bg="white",fg="#515A5A", font=('tahoma', 12, 'bold'), textvariable=self.phone)
        self.phoneStudent.place(x=170, y=80, width=200, height=40)
        self.bookname = Entry(self.frameleft,bg="white",fg="#515A5A", font=('tahoma', 12, 'bold'), textvariable=self.book)
        self.bookname.place(x=170, y=140, width=200, height=40)
        self.DeliveryDate=Calendar(self.frameleft)
        self.DeliveryDate.place(x=170, y=200,width=200,height=200)
        self.ReturnDate = Calendar(self.frameleft)
        self.ReturnDate.place(x=170, y=415, width=200, height=200)

        self.buttonAdd=Button(self.frameleft,text="ADD", command=self.addlibrary,fg="#242423",bg="#F5CB5C"  ,font=('tahoma',11,'bold'))
        self.buttonAdd.place(x=10,y=630,width=60,height=60)
        self.buttonUpdate = Button(self.frameleft,command=self.updatelibrary,fg="#242423",bg="#F5CB5C" , text="UPDATE",font=('tahoma',11,'bold'))
        self.buttonUpdate.place(x=90, y=630,width=60,height=60)
        self.buttonDelete = Button(self.frameleft,command=self.deletelibrary,fg="#242423",bg="#F5CB5C" , text="DELETE",font=('tahoma',11,'bold'))
        self.buttonDelete.place(x=170, y=630,width=60,height=60)
        self.buttonRead = Button(self.frameleft, command=self.readlibrary,fg="#242423",bg="#F5CB5C" , text="SHOW", font=('tahoma', 11, 'bold'))
        self.buttonRead.place(x=250, y=630, width=60, height=60)
        self.buttonReset = Button(self.frameleft,command=self.resetlibrary,fg="#242423",bg="#F5CB5C" , text="RESET", font=('tahoma', 11, 'bold'))
        self.buttonReset.place(x=330, y=630, width=60, height=60)

        self.frameright = Frame(self.master, bg="#E8EDDF", width=800)
        self.frameright.pack(side=LEFT, fill=Y)
    
        self.framerighttop=Frame(self.frameright, bg="#E8EDDF",height=50,pady=5,padx=5)

        self.searchstudent = Entry(self.framerighttop, fg="#515A5A", font=('tahoma', 12, 'bold'),width=110)
        self.searchstudent.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        self.buttonsearch = Button(self.framerighttop,command=self.searchlibrary, text='Search',fg="#242423",bg="#F5CB5C", font=('tahoma', 12, 'bold'),width=50)
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        self.framerighttop.pack(fill=X)
        
        self.frameView=Frame(self.frameright,bg='blue')
        self.frameView.pack(fill=Y)
        self.scrollbar=Scrollbar(self.frameView,orient=VERTICAL)
        self.table=ttk.Treeview(self.frameView,columns=("ID","StudentName","Phone","BookName","DeliveryDate","ReturnDate"),show='headings',yscrollcommand=self.scrollbar.set,height=300)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID",text="ID")
        self.table.heading("StudentName", text="StudentName")
        self.table.heading("Phone", text="Phone")
        self.table.heading("BookName", text="BookNme")
        self.table.heading("DeliveryDate", text="DeliveryDate")
        self.table.heading("ReturnDate", text="ReturnDate")

        self.table.column("ID", anchor=W,width=7)
        self.table.column("StudentName", anchor=W)
        self.table.column("Phone",anchor=W)
        self.table.column("BookName", anchor=W)
        self.table.column("DeliveryDate",anchor=W)
        self.table.column("ReturnDate",anchor=W)
        self.readlibrary()
        self.table.bind("<ButtonRelease>",self.showlibrary)
    def addlibrary(self):
        mydb=mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="insert into library(StudentName,Phone,BookName,DeliveryDate,ReturnDate) values (%s,%s,%s,%s,%s)"
        if (len(self.nameStudent.get())==0 or len(self.phoneStudent.get())==0 or len(self.bookname.get())==0 or len(self.DeliveryDate.get_date())==0 or  len(self.ReturnDate.get_date())==0 ) :
            mb.showerror('Error', 'all data should be required')
        else:
            val=(self.nameStudent.get(),self.phoneStudent.get(),self.bookname.get(),self.DeliveryDate.get_date(),self.ReturnDate.get_date())
            mycursor.execute(sql,val)
            mydb.commit()
            mydb.close()
            mb.showinfo('Successfully added', 'Data inserted Successfully',parent=self.master)
            self.nameStudent.delete(0,'end')
            self.phoneStudent.delete(0, 'end')
            self.bookname.delete(0, 'end')
            self.DeliveryDate.selection_clear()
            self.ReturnDate.selection_clear()
            self.readlibrary()
            
    def readlibrary(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="select * from library"
        mycursor.execute(sql)
        myresults=mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        for res in myresults:
            self.table.insert('','end',iid=res[0],values=res)
            mydb.commit()
        mydb.close()
        
    def showlibrary(self,ev):
        self.iid=self.table.focus()
        alldata=self.table.item(self.iid)
        val=alldata['values']
        self.name.set(val[1])
        self.phone.set(val[2])
        self.book.set(val[3])
        self.delivery.set(val[4])
        self.returnn.set(val[5])
        
    def resetlibrary(self):
        self.nameStudent.delete(0, 'end')
        self.phoneStudent.delete(0, 'end')
        self.bookname.delete(0, 'end')
        self.DeliveryDate.selection_clear()
        self.ReturnDate.selection_clear()

    def deletelibrary(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("delete from library where id="+self.iid)
        mycursor.execute(sql)
        mydb.commit()
        mb.showinfo('Delete','this student deleted',parent=self.master)
        self.readlibrary()
        self.resetlibrary()
        
    def updatelibrary(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("update library set StudentName=%s,Phone=%s,BookName=%s,DeliveryDate=%s,ReturnDate=%s where id=%s")
        val=(self.name.get(),self.phone.get(),self.book.get(),self.DeliveryDate.get_date(),self.ReturnDate.get_date(),self.iid)
        mycursor.execute(sql,val)
        mydb.commit()
        mb.showinfo('update','this student is updated',parent=self.master)
        self.readlibrary()
        self.resetlibrary()
        
    def searchlibrary(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        print(self.searchstudent.get())
        sql = ("select * from library where id="+self.searchstudent.get())
        mycursor.execute(sql)
        myresults = mycursor.fetchone()
        self.table.delete(*self.table.get_children())
        self.table.insert('', 'end', iid=myresults[0], values=myresults)
        mydb.commit()
        mydb.close()        