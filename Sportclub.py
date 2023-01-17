from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb
from tkcalendar import Calendar
from UniversityInfo import universityinfo


class sportclub:
    def __init__(self,bf):
             
        self.sportclubFrame = Frame(bf,pady=0, padx=20)
        self.sportclubFrame.grid(row=1, column=2, sticky='senw')
        self.img5 = Image.open('images/sport.png')
        self.img5.thumbnail((180, 180))
        self.new_img5 = ImageTk.PhotoImage(self.img5)
        self.imgsportclub = Label(self.sportclubFrame, image=self.new_img5, padx=10, pady=10)
        self.imgsportclub.pack()

        self.buttonsportclub = Button(self.sportclubFrame, command=self.opensportclubwindow, font=('tahoma', "11", 'bold'),
                                    text='Sport Club Management',fg="#242423",bg="#F5CB5C", padx=10, pady=10)
        self.buttonsportclub.pack()
    def opensportclubwindow(self):
        spow= sportclubWindow()
        
class sportclubWindow:
    
    def __init__(self,password,id,uniname,craetdate,presencecity,Subscribername,phone,sports,registrationDate,expiryDate):
        
        self.adminpassword=password
        self.adminid=id
            
        self.Uuniname=uniname
        self.Ucreatdate=craetdate
        self.Upresencecity=presencecity
        
        self.spSubscribername=Subscribername
        self.spphone=phone
        self.spsports=sports
        self.spregistrationDate=registrationDate
        self.spexpiryDate=expiryDate
        
        self.u=universityinfo()
   
    def __init__(self):
         
        self.master = Toplevel()
        self.master.title('Sport Club Management System')
        self.master.geometry("1200x800+80+0")
        
        self.frameleft = Frame(self.master,bg="#CFDBD5", width=400)
        self.frameleft.pack(side=LEFT, fill=BOTH)
       
        self.nameLabel=Label(self.frameleft,text='Member Name :',bg="#CFDBD5",fg="#242423",font=('tahoma',12,'bold'))
        self.nameLabel.place(x=15,y=20,width=130,height=40)
        self.phoneLabel = Label(self.frameleft, text='Phone :',bg="#CFDBD5",fg="#242423", font=('tahoma', 12, 'bold'))
        self.phoneLabel.place(x=15,y=65,width=130,height=40)
        self.sportsLabel = Label(self.frameleft, text='Sports :',bg="#CFDBD5",fg="#242423", font=('tahoma', 12, 'bold'))
        self.sportsLabel.place(x=15, y=110, width=120, height=40)
        self.RdatedLabel = Label(self.frameleft, text='Starting Date :',bg="#CFDBD5",fg="#242423", font=('tahoma', 12, 'bold'))
        self.RdatedLabel.place(x=15, y=240, width=130, height=40)
        self.EdaterLabel = Label(self.frameleft, text='Expiry Date :',bg="#CFDBD5",fg="#242423", font=('tahoma', 12, 'bold'))
        self.EdaterLabel.place(x=15, y=415, width=120, height=40)
        
        self.Subscribername=StringVar()
        self.phone = StringVar()
        self.sports= StringVar()
        self.registrationDate=StringVar()
        self.expiryDate= StringVar()
        

        self.SubscriberName1 = Entry(self.frameleft,bg="white",fg="#515A5A",font=('tahoma',12,'bold'),textvariable=self.Subscribername)
        self.SubscriberName1.place(x=170,y=20,width=200,height=40)
        self.phone1 = Entry(self.frameleft,bg="white",fg="#515A5A", font=('tahoma', 12, 'bold'), textvariable=self.phone)
        self.phone1.place(x=170, y=65, width=200, height=40)
        self.Sports1 = ttk.Combobox(self.frameleft, values=["","swimming","Fitness","Football","Basketball"],state='readonly',textvariable=self.sports)
        self.Sports1.place(x=170, y=110, width=200, height=40)
        self.RegistrationDate1=Calendar(self.frameleft)
        self.RegistrationDate1.place(x=170, y=240,width=200,height=170)
        self.ExpiryDate1 = Calendar(self.frameleft)
        self.ExpiryDate1.place(x=170, y=415, width=200, height=170)
        

        self.buttonAdd=Button(self.frameleft,text="ADD", command=self.addsportclub,fg="#242423",bg="#F5CB5C"  ,font=('tahoma',11,'bold'))
        self.buttonAdd.place(x=10,y=630,width=60,height=60)
        self.buttonUpdate = Button(self.frameleft,command=self.updatesportclub,fg="#242423",bg="#F5CB5C" , text="UPDATE",font=('tahoma',11,'bold'))
        self.buttonUpdate.place(x=90, y=630,width=60,height=60)
        self.buttonDelete = Button(self.frameleft,command=self.deletesportclub,fg="#242423",bg="#F5CB5C" , text="DELETE",font=('tahoma',11,'bold'))
        self.buttonDelete.place(x=170, y=630,width=60,height=60)
        self.buttonRead = Button(self.frameleft, command=self.readsportclub,fg="#242423",bg="#F5CB5C" , text="SHOW", font=('tahoma', 11, 'bold'))
        self.buttonRead.place(x=250, y=630, width=60, height=60)
        self.buttonReset = Button(self.frameleft,command=self.resetsportclub,fg="#242423",bg="#F5CB5C" , text="RESET", font=('tahoma', 11, 'bold'))
        self.buttonReset.place(x=330, y=630, width=60, height=60)

        self.frameright = Frame(self.master, bg="#E8EDDF", width=800)
        self.frameright.pack(side=LEFT, fill=Y)
    
        self.framerighttop=Frame(self.frameright, bg="#E8EDDF",height=50,pady=5,padx=5)

        self.searchstudent = Entry(self.framerighttop, fg="#515A5A", font=('tahoma', 12, 'bold'),width=110)
        self.searchstudent.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        self.buttonsearch = Button(self.framerighttop,command=self.searchsportclub, text='Search',fg="#242423",bg="#F5CB5C", font=('tahoma', 12, 'bold'),width=50)
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        self.framerighttop.pack(fill=X)
        
        self.frameView=Frame(self.frameright,bg='blue')
        self.frameView.pack(fill=Y)
        self.scrollbar=Scrollbar(self.frameView,orient=VERTICAL)
        self.table=ttk.Treeview(self.frameView,columns=("ID","SubscriberName","Phone","Sports","RegistrationDate","ExpiryDate"),show='headings',yscrollcommand=self.scrollbar.set,height=300)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID",text="ID")
        self.table.heading("SubscriberName", text="SubscriberName")
        self.table.heading("Phone", text="Phone")
        self.table.heading("Sports", text="Sports")
        self.table.heading("RegistrationDate", text="RegistrationDate")
        self.table.heading("ExpiryDate", text="ExpiryDate")
        

        self.table.column("ID", anchor=W,width=7)
        self.table.column("SubscriberName", anchor=W)
        self.table.column("Phone",anchor=W)
        self.table.column("Sports",anchor=W)
        self.table.column("RegistrationDate",anchor=W)
        self.table.column("ExpiryDate",anchor=W)
        self.readsportclub()
        self.table.bind("<ButtonRelease>",self.showsportclub)
    def addsportclub(self):
        mydb=mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="insert into sportclub(SubscriberName,Phone,Sports,RegistrationDate,ExpiryDate) values (%s,%s,%s,%s,%s)"
        if (len(self.SubscriberName1.get())==0  or len(self.phone.get())==0 or  len(self.sports.get())==0 or len(self.RegistrationDate1.get_date())==0 or  len(self.ExpiryDate1.get_date())==0) :
            mb.showerror('Error', 'all data should be required')
        else:
            val=(self.SubscriberName1.get(),self.phone.get(),self.sports.get(),self.RegistrationDate1.get_date(),self.ExpiryDate1.get_date())
            mycursor.execute(sql,val)
            mydb.commit()
            mydb.close()
            mb.showinfo('Successfully added', 'Data inserted Successfully',parent=self.master)
            self.resetsportclub()
            self.readsportclub()
            
    def readsportclub(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="select * from sportclub"
        mycursor.execute(sql)
        myresults=mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        for res in myresults:
            self.table.insert('','end',iid=res[0],values=res)
            mydb.commit()
        mydb.close()
        
    def showsportclub(self,ev):
        self.iid=self.table.focus()
        alldata=self.table.item(self.iid)
        val=alldata['values']
        self.Subscribername.set(val[1])
        self.phone.set(val[2])
        self.sports.set(val[3])
        self.registrationDate.set(val[4])
        self.expiryDate.set(val[5])
        
    def resetsportclub(self):
        self.SubscriberName1.delete(0, 'end')
        self.phone1.delete(0, 'end')
        self.Sports1.current(0)
        self.RegistrationDate1.selection_clear()
        self.ExpiryDate1.selection_clear()

    def deletesportclub(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("delete from sportclub where id="+self.iid)
        mycursor.execute(sql)
        mydb.commit()
        mb.showinfo('Delete','this student deleted',parent=self.master)
        self.readsportclub()
        self.resetsportclub()
        
    def updatesportclub(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("update sportclub set SubscriberName=%s,Phone=%s,Sports=%s,RegistrationDate=%s,ExpiryDate=%s where id=%s")
        val=(self.Subscribername.get(),self.phone.get(),self.sports.get(),self.RegistrationDate1.get_date(),self.ExpiryDate1.get_date(),self.iid)
        mycursor.execute(sql,val)
        mydb.commit()
        mb.showinfo('update','this student is updated',parent=self.master)
        self.readsportclub()
        self.resetsportclub()
        
    def searchsportclub(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        print(self.searchstudent.get())
        sql = ("select * from sportclub where id="+self.searchstudent.get())
        mycursor.execute(sql)
        myresults = mycursor.fetchone()
        self.table.delete(*self.table.get_children())
        self.table.insert('', 'end', iid=myresults[0], values=myresults)
        mydb.commit()
        mydb.close()    