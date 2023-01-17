
from tkinter import *
import Staff as  st
import Student as std
import Exam as ex
import Library as lib
import Sportclub as sc
from Person import person


class admin(person):
    
    def __init__(self,password,id,Firstname,Lastname,Email,phone,Birthdate,Gender):
       
        self.adminpassword=password
        self.adminid=id
        
        self._Firstname=Firstname
        self._Lastname=Lastname
        self._Email=Email
        self._Phone=phone
        self._Birthdate=Birthdate
        self._Gender=Gender
        
    def addStaff(self):
        st.staffwindow.addstaff()
    def readstaff(self):    
        st.staffwindow.readstaff()
    def showstaff(self):    
        st.staffwindow.showstaff()
    def resetstaff(self):    
        st.staffwindow.resetstaff()
    def deletestaff(self):    
        st.staffwindow.deletestaff()
    def pdatestaff(self):    
        st.staffwindow.updatestaff()
    def searchstaff(self):    
        st.staffwindow.searchstaff()
        
    
    
    def addstudent(self):
        std.studentWindow.addstudent()
    def readstudent(self):
        std.studentWindow.readstudent()
    def showstudent(self):
        std.studentWindow.showstudent()
    def resetstudent(self):
        std.studentWindow.resetstudent()
    def deletestudent(self):
        std.studentWindow.deletestudent()
    def updatestudent(self):
        std.studentWindow.updatestudent()
    def searchstudent(self):
        std.studentWindow.searchstudent()
   
    
            
    def addexam(self):
        ex.examWindow.addexam()
    def readexam(self):
        ex.examWindow.readexam()
    def showexam(self):
       ex.examWindow.showexam()
    def resetexam(self):
        ex.examWindow.resetexam()
    def deleteexam(self):
        ex.examWindow.deleteexam()
    def updateexam(self):
        ex.examWindow.updateexam()
    def searchexam(self):
        ex.examWindow.searchexam()
           
           
           
           
    def addlibrary(self):
        lib.libraryWindow.addlibrary()
    def readlibrary(self):
        lib.libraryWindow.readlibrary()
    def showlibrary(self):
       lib.libraryWindow.showlibrary()
    def resetlibrary(self):
        lib.libraryWindow.resetlibrary()
    def deletelibrary(self):
        lib.libraryWindow.deletelibrary()
    def updatelibrary(self):
        lib.libraryWindow.updatelibrary()
    def searchlibrary(self):
        lib.libraryWindow.searchlibrary()



    def addsportclub(self):
        sc.sportclubWindow.addsportclub()
    def readsportclub(self):
        sc.sportclubWindow.readsportclub()
    def showsportclub(self):
        sc.sportclubWindow.showsportclub()
    def resetsportclub(self):
        sc.sportclubWindow.resetsportclub()
    def deletesportclub(self):
        sc.sportclubWindow.deletesportclub()
    def updatesportclub(self):
        sc.sportclubWindow.updatesportclub()
    def searchsportclub(self):
        sc.sportclubWindow.searchsportclub()




      
   
        