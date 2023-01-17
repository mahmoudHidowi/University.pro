from tkinter import *
import Library as lib
import Exam as ex
import Sportclub as sc
import UniversityInfo as ui
import Staff as  st
import Student as s
import  mysql.connector as mc
import tkinter.messagebox as mb 
from PIL import ImageTk
import PIL

                                      


class University:
    
    def __init__(self, window):
        self.master=window
        self.master.title("University Management System")
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width , h=self.height ))
        self.master.state("zoomed")
        self.frametop=Frame(self.master,bg="#333533",height=200)
        self.frametop.pack(fill=X)
        self.usm=Label(self.frametop,text="University Management System",bg="#333533",fg="#F5CB5C",font=("tahoma",50),pady=50)
        self.usm.pack()
        
        
        
        self.centerFrame=Frame(self.master)
        self.centerFrame.pack(fill=X)

        stf=st.staff(self.centerFrame)
        uni=ui.universityinfo(self.centerFrame)
        std=s.student(self.centerFrame)
        
      
        self.centerFrame.grid_columnconfigure(0,weight=1)
        self.centerFrame.grid_columnconfigure(1,weight=1)
        self.centerFrame.grid_columnconfigure(2,weight=1)
       
        self.bottomFrame=Frame(self.master,bg="#F5CB5C")
        self.bottomFrame.pack(fill=X)
        
         
        libr=lib.library(self.bottomFrame)
        exa=ex.exam(self.bottomFrame)
        spo=sc.sportclub(self.bottomFrame)
        
        self.bottomFrame.grid_columnconfigure(0,weight=1)
        self.bottomFrame.grid_columnconfigure(1,weight=1)
        self.bottomFrame.grid_columnconfigure(2,weight=1)
        
        
    def logout(self):
        self.master.destroy()
        
class book:
    def __init__(self,bookname,author,pagenambers,id):
        self.Bookbookname=bookname
        self.Bookauthor=author
        self.Bookpagenambers=pagenambers
        self.Bookid=id
        
            
      
class login:
    def __init__(self, window):
        self.master = window
        self.master.title("Login System")
        self.master.geometry("500x500+400+100")
        self.img = PIL.Image.open('images/login.png')
        self.img.thumbnail((200, 200))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imgStudent = Label(self.master, image=self.new_img)
        self.imgStudent.pack()
        self.frameLogin=Frame(self.master)
        self.frameLogin.pack()
        self.labelUser = Label(self.frameLogin, text='Username',padx=10,pady=10, font=('tahoma', 12, 'bold'))
        self.labelUser.grid(row=0, column=0)
        self.labelPass = Label(self.frameLogin, text='Password',padx=10,pady=10, font=('tahoma', 12, 'bold'))
        self.labelPass.grid(row=1, column=0)
        self.username = Entry(self.frameLogin,bg="white",fg="#515A5A", font=('tahoma', 12, 'bold'))
        self.username.grid(row=0, column=1, pady=10, padx=10)
        self.password = Entry(self.frameLogin,bg="white",fg="#515A5A", font=('tahoma', 12, 'bold'), show="*")
        self.password.grid(row=1, column=1, pady=10, padx=10)
        self.LoginButton = Button(self.frameLogin, command=self.login, text='Login', font=('tahoma', 11, 'bold')
                                  ,fg="#242423",bg="#F5CB5C", cursor='cross')
        self.LoginButton.grid(row=2, column=0, columnspan=2, sticky='snew', pady=12, padx=12)

    def login(self):
                mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
                )

                mycursor = mydb.cursor()
                sql = "select * from login where Username='"+ self.username.get() +"' and Password='" + self.password.get() + "'"
                mycursor.execute(sql)
                res = mycursor.fetchone()
                if (res == None):
                    mb.showerror('Failed Login', 'Invalid Username and Password ! please Try again')
                else:
                    windo = Toplevel()
                    window = University(windo)
            
   
        
if(__name__=="__main__"):
      window=Tk()
      new_window = login(window)
      
      window.mainloop()
                      
