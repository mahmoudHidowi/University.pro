
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import PIL.Image
import  mysql.connector as mc
import tkinter.messagebox as mb
from Exam import examWindow
from Person import person


class student:
    def __init__(self,cf):
       
        self.studentFrame=Frame(cf,pady=10,padx=10)
        self.studentFrame.grid(row=0,column=1,sticky="senw")
        self.img2= PIL.Image.open('images/studenticon.png')
        self.img2.thumbnail((180,180))
        self.new_img2= ImageTk.PhotoImage(self.img2)
        self.imgStudent=Label(self.studentFrame, image=self.new_img2,padx=10,pady=10)
        self.imgStudent.pack()
        self.buttonStudent=Button(self.studentFrame,command=self.openstudentwindow,font=("tahoma","11","bold"),text="Student Management",fg="#242423",bg="#F5CB5C",padx=10,pady=12)
        self.buttonStudent.pack()
        
        
   
    def openstudentwindow(self):
        stdw=studentWindow()
       
class studentWindow(person):
    def __init__(self,college,studyDivision,joinDate,id,password,Firstname,Lastname,Email,phone,Birthdate,Gender,lessonName,examDay,examDate,examMark):
        
        self.adminpassword=password
        self.adminid=id
        
        self._Firstname=Firstname
        self._Lastname=Lastname
        self._Email=Email
        self._Phone=phone
        self._Birthdate=Birthdate
        self._Gender=Gender
        
        self.ElessonName=lessonName
        self.EexamDay=examDay
        self.EexamDate=examDate
        self.EexamMark=examMark
        self.Eid=id
        
        self.stcollege=college
        self.ststudyDivision=studyDivision
        self.stjoinDate=joinDate
        self.stid=id
        
        self.ex=examWindow()
    def __init__(self):
        
       
        self.master = Toplevel()
        self.master.title('Student Management System')
        self.master.geometry("1200x600+70+60")
        
        self.frameleft = Frame(self.master,bg="#CFDBD5", width=400)
        self.frameleft.pack(side=LEFT, fill=BOTH)
        
        self.firstName=Label(self.frameleft,text='First Name :',bg="#CFDBD5",fg="#242423",font=('tahoma',12,'bold'))
        self.firstName.place(x=10,y=20,width=100,height=40)
        self.lastName = Label(self.frameleft, text='Last Name :',bg="#CFDBD5",fg="#242423",font=('tahoma',12,'bold'))
        self.lastName.place(x=10,y=70,width=100,height=40)
        self.CIN = Label(self.frameleft, text='CIN :',bg="#CFDBD5",fg="#242423",font=('tahoma',12,'bold'))
        self.CIN.place(x=10,y=120,width=100,height=40)
        self.Email = Label(self.frameleft, text='Email :',bg="#CFDBD5",fg="#242423",font=('tahoma',12,'bold'))
        self.Email.place(x=10,y=170,width=100,height=40)
        self.Phone = Label(self.frameleft, text='Phone :',bg="#CFDBD5",fg="#242423", font=('tahoma', 12, 'bold'))
        self.Phone.place(x=10, y=220, width=100, height=40)
        
        self.name=StringVar()
        self.last = StringVar()
        self.email = StringVar()
        self.cin = StringVar()
        self.phone=StringVar()

        self.firstNameEntry = Entry(self.frameleft,bg="white",fg="#515A5A",font=('tahoma',12,'bold'),textvariable=self.name)
        self.firstNameEntry.place(x=120,y=20,width=200,height=40)
        self.lastNameEntry = Entry(self.frameleft,bg="white",fg="#515A5A",font=('tahoma',12,'bold'),textvariable=self.last)
        self.lastNameEntry.place(x=120,y=70,width=200,height=40)
        self.CINentry = Entry(self.frameleft,bg="white",fg="#515A5A",font=('tahoma',12,'bold'),textvariable=self.cin)
        self.CINentry.place(x=120,y=120,width=200,height=40)
        self.EmailEntry = Entry(self.frameleft,bg="white",fg="#515A5A",font=('tahoma',12,'bold'),textvariable=self.email)
        self.EmailEntry.place(x=120,y=170,width=200,height=40)
        self.PhoneEntry = Entry(self.frameleft,bg="white",fg="#515A5A", font=('tahoma', 12, 'bold'), textvariable=self.phone)
        self.PhoneEntry.place(x=120, y=220, width=200, height=40)

        self.buttonAdd=Button(self.frameleft,text="ADD", command=self.addstudent ,fg="#242423",bg="#F5CB5C" ,font=('tahoma',11,'bold'))
        self.buttonAdd.place(x=10,y=300,width=60,height=60)
        self.buttonUpdate = Button(self.frameleft,command=self.updatestudent,fg="#242423",bg="#F5CB5C", text="UPDATE",font=('tahoma',11,'bold'))
        self.buttonUpdate.place(x=90, y=300,width=60,height=60)
        self.buttonDelete = Button(self.frameleft,command=self.deletestudent, fg="#242423",bg="#F5CB5C",text="DELETE",font=('tahoma',11,'bold'))
        self.buttonDelete.place(x=170, y=300,width=60,height=60)
        self.buttonRead = Button(self.frameleft, command=self.readstudent,fg="#242423",bg="#F5CB5C", text="SHOW", font=('tahoma', 11, 'bold'))
        self.buttonRead.place(x=250, y=300, width=60, height=60)
        self.buttonReset = Button(self.frameleft,command=self.resetstudent,fg="#242423",bg="#F5CB5C", text="RESET", font=('tahoma', 11, 'bold'))
        self.buttonReset.place(x=330, y=300, width=60, height=60)

        self.frameright = Frame(self.master,bg="#E8EDDF", width=800)
        self.frameright.pack(side=LEFT, fill=Y)

        self.framerighttop=Frame(self.frameright,bg="#E8EDDF",height=50,pady=5,padx=5)

        self.searchstudent1 = Entry(self.framerighttop, fg="#515A5A", font=('tahoma', 12, 'bold'),width=110)
        self.searchstudent1.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        self.buttonsearch = Button(self.framerighttop,command=self.searchstudent, text='Search',fg="#242423",bg="#F5CB5C", font=('tahoma', 12, 'bold'),width=50)
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        self.framerighttop.pack(fill=X)

        self.frameView=Frame(self.frameright,bg='blue')
        self.frameView.pack(fill=Y)
        self.scrollbar=Scrollbar(self.frameView,orient=VERTICAL)
        self.table=ttk.Treeview(self.frameView,columns=("ID","First Name","Last Name","CIN","Email","Phone"),show='headings',yscrollcommand=self.scrollbar.set,height=300)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID",text="ID")
        self.table.heading("First Name", text="First Name")
        self.table.heading("Last Name", text="Last Name")
        self.table.heading("CIN", text="CIN")
        self.table.heading("Email", text="Email")
        self.table.heading("Phone", text="Phone")

        self.table.column("ID", anchor=W,width=7)
        self.table.column("First Name", anchor=W)
        self.table.column("Last Name",anchor=W)
        self.table.column("CIN",anchor=W)
        self.table.column("Email",anchor=W)
        self.table.column("Phone",anchor=W)
        self.readstudent()
        self.table.bind("<ButtonRelease>",self.showstudent)
      
        
    def addstudent(self):
        mydb=mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="insert into student(FirstName,LastName,CIN,Email,Phone) values (%s,%s,%s,%s,%s)"
        if (len(self.firstNameEntry.get())==0 or len(self.lastNameEntry.get())==0 or len(self.CINentry.get())==0 or len(self.EmailEntry.get())==0 or len(self.PhoneEntry.get())==0 ) :
            mb.showerror('Error', 'all data should be required')
        else:
            val=(self.firstNameEntry.get(),self.lastNameEntry.get(),self.CINentry.get(),self.EmailEntry.get(),self.PhoneEntry.get())
            mycursor.execute(sql,val)
            mydb.commit()
            mydb.close()
            mb.showinfo('Successfully added', 'Data inserted Successfully',parent=self.master)
            self.firstNameEntry.delete(0,'end')
            self.lastNameEntry.delete(0, 'end')
            self.CINentry.delete(0, 'end')
            self.EmailEntry.delete(0, 'end')
            self.PhoneEntry.delete(0, 'end')
            self.readstudent()
            self.resetstudent()
            
    def readstudent(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="select * from student"
        mycursor.execute(sql)
        myresults=mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        for res in myresults:
            self.table.insert('','end',iid=res[0],values=res)
            mydb.commit()
        mydb.close()
        
    def showstudent(self,ev):
        self.iid=self.table.focus()
        alldata=self.table.item(self.iid)
        val=alldata['values']
        self.name.set(val[1])
        self.last.set(val[2])
        self.cin.set(val[3])
        self.email.set(val[4])
        self.phone.set(val[5])
        
        
    def resetstudent(self):
        self.firstNameEntry.delete(0, 'end')
        self.lastNameEntry.delete(0, 'end')
        self.CINentry.delete(0, 'end')
        self.EmailEntry.delete(0, 'end')
        self.PhoneEntry.delete(0, 'end')

    def deletestudent(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("Delete from student where ID="+self.iid)
        mycursor.execute(sql)
        mydb.commit()
        mb.showinfo('Delete','this student deleted',parent=self.master)
        self.readstudent()
        self.resetstudent()
        
    def updatestudent(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("update student set FirstName=%s,LastName=%s,CIN=%s,Email=%s,Phone=%s where ID=%s")
        val=(self.name.get(),self.last.get(),self.cin.get(),self.email.get(),self.phone.get(),self.iid)
        mycursor.execute(sql,val)
        mydb.commit()
        mb.showinfo('update','this student is updated',parent=self.master)
        self.readstudent()
        self.resetstudent()
    def searchstudent(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        print(self.searchstudent.get())
        sql = ("select * from student where id="+self.searchstudent.get())
        mycursor.execute(sql)
        myresults = mycursor.fetchone()
        self.table.delete(*self.table.get_children())
        self.table.insert('', 'end', iid=myresults[0], values=myresults)
        mydb.commit()
        mydb.close()
    
        