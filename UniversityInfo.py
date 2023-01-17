from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
from tkinter import ttk


class universityinfo:
    def __init__(self,cf):
       
        self.universityinfo = Frame(cf, pady=2, padx=10)
        self.universityinfo.grid(row=0, column=0, sticky='senw')
        self.img = Image.open('images/university.png')
        self.img.thumbnail((193,195))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imgUniversity = Label(self.universityinfo, image=self.new_img, padx=10, pady=9)
        self.imgUniversity.pack()
        self.buttonUniversity = Button(self.universityinfo,command=self.openinfowindow, font=('tahoma', "11", 'bold'), text='About University',fg="#242423",bg="#F5CB5C", padx=10, pady=12)
        self.buttonUniversity.pack()

    def openinfowindow(self):
       info=InfoWindow()



class InfoWindow:
    
    def __init__(self,uniname,craetdate,presencecity):
        
        self.Uuniname=uniname
        self.Ucreatdate=craetdate
        self.Upresencecity=presencecity
        
    def __init__(self):
    
        self.master = Toplevel()
        self.master.title('University Info')
        self.master.geometry("1200x800+80+0")
        self.TitleLabel=Label(self.master,text='University Of Applied Sciences',bg="#333533",pady=100,fg="#F5CB5C",font=('Tahoma',30,'bold'))
        self.TitleLabel.pack(fill=X)
        self.txt=StringVar()
        self.Message=Message(self.master,textvariable=self.txt,justify=CENTER,font=('tahoma',11))
        self.Message.pack()
        self.txt.set("\n Founded in February 1999 with the support of the Free Hanseatic City of Bremen, the University \n\n  of Bremen and Rice University, the “International University Bremen” (IUB) started its first academic year in 2001. \n\n Since its founding, the private, English-speaking, campus university has been committed to its core principles: excellence in research and teaching, being a driver of innovation, maintaining a broad portfolio of academic programs, fostering a vibrant community, and hosting a campus that is a home away from home for its international student body.\n\n It has survived not only five centuries, but also the leap into electronic typesetting, \n\n Currently, its more than 1,500 students come from more than 110 countries with around 80% having relocated to Germany for their studies. \n\n Jacobs University’s research projects are funded by the German Research Foundation, or the EU Research and Innovation program, as well as by global leading companies. \n\n The high quality of research and teaching at Jacobs University Bremen has been repeatedly confirmed by renowned national and international university rankings.\n\n In the “Young University Rankings 2021” of the British magazine “Times Higher Education” (THE) for universities under the age of 50.")
        