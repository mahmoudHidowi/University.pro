
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import PIL.Image
import  mysql.connector as mc
import tkinter.messagebox as mb
from Person import person


class staff:
    def __init__(self,cf):
        
        self.StaffFrame=Frame(cf,pady=10 ,padx=10)
        self.StaffFrame.grid(row=0,column=2,sticky="senw")
        self.img3= PIL.Image.open('images/staff.png')
        self.img3.thumbnail((180,181))
        self.new_img3= ImageTk.PhotoImage(self.img3)
        self.imgstaff=Label(self.StaffFrame, image=self.new_img3,padx=10,pady=10)
        self.imgstaff.pack()
        self.buttonstaff=Button(self.StaffFrame,command=self.openstaffwindow,font=("tahoma","11","bold"),text="Staff Management",fg="#242423",bg="#F5CB5C",padx=10,pady=11)
        self.buttonstaff.pack()
   
     
    def openstaffwindow(self):
       stfw=staffwindow()
     
class staffwindow(person):
    def __init__(self,specialization,college,lessonName,id,password,Firstname,Lastname,Email,phone,Birthdate,Gender):
        self.adminpassword=password
        self.adminid=id
        
        self._Firstname=Firstname
        self._Lastname=Lastname
        self._Email=Email
        self._Phone=phone
        self._Birthdate=Birthdate
        self._Gender=Gender
        
        self.Sspecialization=specialization
        self.Scollege=college
        self.SlessonName=lessonName
        self.Sid=id
    def __init__(self):
       
        self.master = Toplevel()
        self.master.title('Staff Management System')
        self.master.geometry("1200x600+70+60")
        
        self.frameleft = Frame(self.master,bg="#CFDBD5", width=400)
        self.frameleft.pack(side=LEFT, fill=BOTH)
        
        self.firstName=Label(self.frameleft,text='FirstName :',bg="#CFDBD5",fg="#242423",font=('tahoma',12,'bold'))
        self.firstName.place(x=10,y=20,width=100,height=40)
        self.lastName = Label(self.frameleft, text='LastName :',bg="#CFDBD5",fg="#242423",font=('tahoma',12,'bold'))
        self.lastName.place(x=10,y=70,width=100,height=40)
        self.CIN = Label(self.frameleft, text='CIN :',bg="#CFDBD5",fg="#242423",font=('tahoma',12,'bold'))
        self.CIN.place(x=10,y=120,width=100,height=40)
        self.Email = Label(self.frameleft, text='Email :',bg="#CFDBD5",fg="#242423",font=('tahoma',12,'bold'))
        self.Email.place(x=10,y=170,width=100,height=40)
        self.Phone = Label(self.frameleft, text='Phone :',bg="#CFDBD5",fg="#242423", font=('tahoma', 12, 'bold'))
        self.Phone.place(x=10, y=220, width=100, height=40)
        self.Job= Label(self.frameleft, text='Job :',bg="#CFDBD5",fg="#242423", font=('tahoma', 12, 'bold'))
        self.Job.place(x=10, y=290, width=100, height=40)
        
        self.name=StringVar()
        self.last = StringVar()
        self.email = StringVar()
        self.cin = StringVar()
        self.phone=StringVar()
        self.job=StringVar()
        
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
        self.JobEntry = ttk.Combobox(self.frameleft, values=["","Employee","Professor","Technician"],state='readonly',textvariable=self.job)
        self.JobEntry.place(x=120, y=290, width=200, height=40)

        self.buttonAdd=Button(self.frameleft,text="ADD", command=self.addstaff,fg="#242423",bg="#F5CB5C" ,font=('tahoma',11,'bold'))
        self.buttonAdd.place(x=10,y=400,width=60,height=60)
        self.buttonUpdate = Button(self.frameleft,command=self.updatestaff,fg="#242423",bg="#F5CB5C", text="UPDATE",font=('tahoma',11,'bold'))
        self.buttonUpdate.place(x=90, y=400,width=60,height=60)
        self.buttonDelete = Button(self.frameleft,command=self.deletestaff,fg="#242423",bg="#F5CB5C", text="DELETE",font=('tahoma',11,'bold'))
        self.buttonDelete.place(x=170, y=400,width=60,height=60)
        self.buttonRead = Button(self.frameleft, command=self.readstaff,fg="#242423",bg="#F5CB5C", text="SHOW", font=('tahoma', 11, 'bold'))
        self.buttonRead.place(x=250, y=400, width=60, height=60)
        self.buttonReset = Button(self.frameleft,command=self.resetstaff,fg="#242423",bg="#F5CB5C", text="RESET", font=('tahoma', 11, 'bold'))
        self.buttonReset.place(x=330, y=400, width=60, height=60)

        self.frameright = Frame(self.master,bg="#E8EDDF", width=800)
        self.frameright.pack(side=LEFT, fill=Y)
   
        self.framerighttop=Frame(self.frameright,bg="#E8EDDF",height=50,pady=5,padx=5)

        self.searchstudent = Entry(self.framerighttop, fg="#515A5A", font=('tahoma', 12, 'bold'),width=110)
        self.searchstudent.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        self.buttonsearch = Button(self.framerighttop,command=self.searchstaff, text='Search',fg="#242423",bg="#F5CB5C", font=('tahoma', 12, 'bold'),width=50)
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        self.framerighttop.pack(fill=X)
        
        self.frameView=Frame(self.frameright,bg='blue')
        self.frameView.pack(fill=Y)
        self.scrollbar=Scrollbar(self.frameView,orient=VERTICAL)
        self.table=ttk.Treeview(self.frameView,columns=("ID","FirstName","LastName","CIN","Email","Phone","Job"),show='headings',yscrollcommand=self.scrollbar.set,height=300)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID",text="ID")
        self.table.heading("FirstName", text="FirstName")
        self.table.heading("LastName", text="LastName")
        self.table.heading("CIN", text="CIN")
        self.table.heading("Email", text="Email")
        self.table.heading("Phone", text="Phone")
        self.table.heading("Job", text="Job")

        self.table.column("ID", anchor=W,width=7)
        self.table.column("FirstName", anchor=W,width=130)
        self.table.column("LastName",anchor=W,width=130)
        self.table.column("CIN",anchor=W,width=130)
        self.table.column("Email",anchor=W,width=130)
        self.table.column("Phone", anchor=W,width=130)
        self.table.column("Job", anchor=W,width=130)
        self.readstaff()
        self.table.bind("<ButtonRelease>",self.showstaff)
    
    
    
    def addstaff(self):
            
        mydb=mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="insert into staff(FirstName,LastName,CIN,Email,Phone,Job) values (%s,%s,%s,%s,%s,%s)"
        if (len(self.firstNameEntry.get())==0 or len(self.PhoneEntry.get())==0 or len(self.JobEntry.get())==0  or len(self.lastNameEntry.get())==0 or len(self.CINentry.get())==0 or len(self.EmailEntry.get())==0 ) :
            mb.showerror('Error', 'all data should be required')
        else:
            val=(self.firstNameEntry.get(),self.lastNameEntry.get(),self.CINentry.get(),self.EmailEntry.get(),self.PhoneEntry.get(),self.JobEntry.get())
            mycursor.execute(sql,val)
            mydb.commit()
            mydb.close()
            mb.showinfo('Successfully added', 'Data inserted Successfully',parent=self.master)
            self.resetstaff()
            self.readstaff()
            
    def readstaff(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="select * from staff"
        mycursor.execute(sql)
        myresults=mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        for res in myresults:
            self.table.insert('','end',iid=res[0],values=res)
            mydb.commit()
        mydb.close()
        
    def showstaff(self,ev):
        self.iid=self.table.focus()
        alldata=self.table.item(self.iid)
        val=alldata['values']
        self.name.set(val[1])
        self.last.set(val[2])
        self.cin.set(val[3])
        self.email.set(val[4])
        self.phone.set(val[5])
        self.job.set(val[6])
        
    def resetstaff(self):
        
        
        self.firstNameEntry.delete(0, 'end')
        self.lastNameEntry.delete(0, 'end')
        self.CINentry.delete(0, 'end')
        self.EmailEntry.delete(0, 'end')
        self.PhoneEntry.delete(0, 'end')
        self.JobEntry.current(0)

    def deletestaff(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("delete from staff where id="+self.iid)
        mycursor.execute(sql)
        mydb.commit()
        mb.showinfo('Delete','this student deleted',parent=self.master)
        self.readstaff()
        self.resetstaff()
        
    def updatestaff(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("update staff set FirstName=%s,LastName=%s,CIN=%s,Email=%s,Phone=%s,Job=%s where id=%s")
        val=(self.name.get(),self.last.get(),self.cin.get(),self.email.get(),self.phone.get(),self.job.get(),self.iid)
        mycursor.execute(sql,val)
        mydb.commit()
        mb.showinfo('update','this student is updated',parent=self.master)
        self.readstaff()
        self.resetstaff()
    def searchstaff(self):
        
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        print(self.searchstudent.get())
        sql = ("select * from staff where id="+self.searchstudent.get())
        mycursor.execute(sql)
        myresults = mycursor.fetchone()
        self.table.delete(*self.table.get_children())
        self.table.insert('', 'end', iid=myresults[0], values=myresults)
        mydb.commit()
        mydb.close()  
        
    