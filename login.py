from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
import smtplib
import sqlite3
import random
from signup import *
import time as tm
import datetime as dt

class log:
#change password
    def change(self):
        if(self.text.get().strip("")=="" and self.text2.get().strip("")==""):
            showinfo("","Every Field is Mandatory")
        elif(self.text.get()!=self.text2.get()):
            showerror("","Password Does'nt Match")
        else:
            conn = sqlite3.connect("db.sqlite3")
            cr=conn.cursor()
            a="update info set password='"+self.text.get()+"' where username='"+self.f+"'"
            cr.execute(a)
            conn.commit()
            self.win9.destroy()
            showinfo("","Password Changed Successfully")


#password change window
    def resetpass(self):

        global text,text2
        if (l[1]!=self.txt.get()):
            showerror("Incorrect","Answer Does'nt Match")
            self.txt.delete(0,'end')
        else:
            self.win9=Tk()
            self.war=Label(self.win9,text="Window Will Automatically close after 20 Seconds")
            self.lb1=Label(self.win9,text="Enter New Password")
            self.lb2=Label(self.win9,text="Re-Enter Password")
            self.bt=Button(self.win9,text="UPDATE",command=self.change)
            self.bt.grid(row=2,column=1)
            self.bt2=Button(self.win9,text="Cancel",command=self.__init__)
            self.bt2.grid(row=2,column=0)
            self.text=Entry(self.win9)
            self.text2=Entry(self.win9)
            self. war.grid(row=3,column=0)
            self.lb1.grid(row=0,column=0)
            self.text.grid(row=0,column=1)
            self.lb2.grid(row=1,column=0)
            self.text2.grid(row=1,column=1)
            self.win9.after(20000,lambda :root.destroy())
            self.win.withdraw()
            self.win9.mainloop()

    def sign(self):
        obj=signup()
    def page(self):
        global result,l,txt,f
        self.f=self.txt1.get()
        conn = sqlite3.connect("db.sqlite3")
        cr=conn.cursor()
        sh="select username from info"
        cr.execute(sh)
        no=cr.fetchall()
        flag=1
        for rel in no:
            if (str(rel[0])==self.f):
                flag=0
                break
        if (flag==0):
            self.win=Tk()
            conn = sqlite3.connect("db.sqlite3")
            cr=conn.cursor()
            s="select securityques,securityans from info where username='"+self.f+"'"
            cr.execute(s)
            result=cr.fetchall()
            for l in result:
                j=l[0]
                self.lb1 = Label(self.win, text=j)
                self.lb2=Label(self.win,text="Answer here(case sensitive)")
                self.txt=Entry(self.win)
                self.bt1=Button(self.win,text="SUBMIT",command=self.resetpass)
                self.txt.delete(0,'end')


                self.lb1.grid(row=0,column=0)
                self.lb2.grid(row=1,column=0)
                self.txt.grid(row=1,column=1)
                self.bt1.grid(row=2,column=1)


                self.win.mainloop()

        elif(flag==1):
            showinfo("","Username ERROR")

    def passshow(self):
        self.showpass=Label(self.win,text=self.txt2.get())
        self.showpass.grid(row=3,column=1)
    def show(self):
        global h
        conn = sqlite3.connect("db.sqlite3")
        cr=conn.cursor()
        q="select username,password from info"
        cr.execute(q)
        result=cr.fetchall()
        flag=0
        for i in result:
            if (str(i[0])==self.txt1.get() and str(i[1])==self.txt2.get()):
                flag=1
                break
        if flag==0:
            showerror("PROBLEM","Invalid Password or Username")
        else:
            self.h = (self.txt1.get())
            self.lb4=Label(self.win,text="Login Successful")

            self.lb4.grid(row=6,column=1)
            self.o = timedis = tm.strftime('%I:%M:%S %p')
            self.now = dt.datetime.now()
            self.g = self.now.strftime("%d-%m-%Y")
            cr=conn.cursor()
            q="insert into logininfo values('"+self.txt1.get()+ "','" +self.txt2.get()+"','"+self.o+"','"+self.g+"')"
            cr.execute(q)
            conn.commit()
            self.txt1.delete(0, 'end')
            self.txt2.delete(0, 'end')
            self.win.withdraw()
            self.logind(self.txt1.get(),self.txt2.get())    #after login

    def editseqans(self):
        self.win4 = Tk()
        self.win4.title("Change Your Security Ans")
        conn = sqlite3.connect("db.sqlite3")
        cr = conn.cursor()
        quesdisplay = "select securityques from info where username='" + self.h + "'"
        cr.execute(quesdisplay)
        result = cr.fetchone()



        def change():
            upd = "update info set securityans='" + self.newans.get() + "' where username='" + self.h + "'"
            cr.execute(upd)
            conn.commit()
            showinfo("UPDATED", "Successfully Updated")
            self.win4.destroy()

    # email send
    # code here
    # -------------------


        self.yu = Label(self.win4, text="Security Question : ")
        self.quesdis = Label(self.win4, text=result[0])
        self.lb = Label(self.win4, text="Enter New Answer")
        self.newans = Entry(self.win4)
        self.chn = Button(self.win4, text="Update", command=change)

        self.yu.grid(row=0, column=0)
        self.quesdis.grid(row=0, column=1)
        self.lb.grid(row=1, column=0)
        self.newans.grid(row=1, column=1)
        self.chn.grid(row=2, column=1)
        self.win4.mainloop()


    def editpass(self):
        self.win3 = Tk()
        self.win3.title("Change Password")
        conn = sqlite3.connect("db.sqlite3")
        cr = conn.cursor()
        passdisplay = "select password from info where username='" + self.h + "'"
        cr.execute(passdisplay)
        result = cr.fetchone()



        def change():
            if(str(result[0])!=self.tt.get()):
                showerror("","Previous Password Not Match")
            else:
                upd = "update info set password='" + self.newpass.get() + "' where username='" + self.h + "'"
                cr.execute(upd)
                conn.commit()
                showinfo("UPDATED", "Successfully Updated")
                self.win3.destroy()

    # email send
    # code here
    # -------------------


        self.yu = Label(self.win3, text="Enter Previous Password : ")
        self.tt = Entry(self.win3)
        self.lb = Label(self.win3, text="Enter New Password")
        self.newpass = Entry(self.win3)
        self.chn = Button(self.win3, text="Update", command=change)

        self.yu.grid(row=0, column=0)
        self.tt.grid(row=0, column=1)
        self.lb.grid(row=1, column=0)
        self.newpass.grid(row=1, column=1)
        self.chn.grid(row=2, column=1)
        self.win3.mainloop()

    def editname(self):
        self.win2=Tk()
        self.win2.title("Change Your Name")
        conn = sqlite3.connect("db.sqlite3")
        cr = conn.cursor()
        namedisplay = "select name from info where username='"+self.h+"'"
        cr.execute(namedisplay)
        result = cr.fetchone()
        def change():
            upd="update info set name='"+self.newname.get()+"' where username='"+self.h+"'"
            cr.execute(upd)
            conn.commit()
            showinfo("UPDATED","Successfully Updated")
            self.win2.destroy()
            self.root.destroy()
            self.win.withdraw()
            self.logind(self.txt1.get(),self.txt2.get())    #then again Login


            #email send
            #code here
            #-------------------

        self.yu=Label(self.win2,text="Existing Name : ")
        self.namedis=Label(self.win2,text=result[0])
        self.lb=Label(self.win2,text="Enter New Name")
        self.newname=Entry(self.win2)
        self.chn=Button(self.win2,text="Update",command=change)

        self.yu.grid(row=0,column=0)
        self.namedis.grid(row=0,column=1)
        self.lb.grid(row=1,column=0)
        self.newname.grid(row=1,column=1)
        self.chn.grid(row=2,column=1)
        self.win2.mainloop()


    def accountinformation(self):
        self.win5=Tk()
        self.win5.title("My Information")
        self.f1=Frame(self.win5)
        self.win5.geometry("1500x50")
        conn = sqlite3.connect("db.sqlite3")
        cr=conn.cursor()
        all="select * from info where username='"+self.h+"'"
        cr.execute(all)
        res=cr.fetchall()
        conn.commit()

        self.t1=Treeview(self.f1,columns=("name","username","password","gender","sques","sans","email"))
        self.t1.heading("name",text="Name")
        self.t1.heading("username",text="Username")
        self.t1.heading("password",text="Password")
        self.t1.heading("gender",text="Gender")
        self.t1.heading("sques",text="Security Question")
        self.t1.heading("sans",text="Security Answer")
        self.t1.heading("email",text="E-Mail")

        self.t1.column("name",anchor="center")
        self.t1.column("username", anchor="center")
        self.t1.column("password", anchor="center")
        self.t1.column("gender", anchor="center")
        self.t1.column("sques", anchor="center")
        self.t1.column("sans", anchor="center")
        self.t1.column("email", anchor="center")
        self.t1["show"]="headings"

        i=0
        for r in res:
            self.t1.insert("",index=i,values=r)
        self.t1.pack()
        self.f1.grid(row=0,column=0)


        self.win5.mainloop()




    def logincount(self):
        self.win6=Tk()
        self.win6.title("WOW!")
        self.f1=Frame(self.win6)
        self.f2=Frame(self.win6)

        conn = sqlite3.connect("db.sqlite3")
        cr=conn.cursor()
        s="select count(*) from logininfo where username='"+self.h+"'"
        cr.execute(s)
        resu=cr.fetchone()
        print(resu[0])
        self.lbbb=Label(self.f1,text="You Have Logged in")


        r=str(resu[0])+" Times till now"
        self.lbbb2=Label(self.f1,text=r)

        self.tyy=Label(self.f2,text="Window will Automatically close after 5 Seconds ")
        self.tyy.grid(row=1,column=1)
        self.lbbb.grid(row=0,column=0)
        self.lbbb2.grid(row=0,column=1)


        self.f1.pack()
        self.f2.pack()
        self.win6.after(5000,lambda :self.win6.destroy())

    def accordel(self,event):
        self.test = self.t4.item(self.t4.selection())
        def accept():
            self.a = timedis = tm.strftime('%I:%M:%S %p')
            now = dt.datetime.now()
            self.g = now.strftime("%d-%m-%Y")
            conn = sqlite3.connect("db.sqlite3")
            cr=conn.cursor()
            ac="update friends set accepted='Yes' where myusername='"+ self.test['values'][1] +"'and friendusername='" + self.h + "'"
            cr.execute(ac)
            cr.close()
            conn.commit()
            self.win11.withdraw()
            conn = sqlite3.connect("db.sqlite3")
            cr = conn.cursor()
            asss = "select count(*) from friends,info where friends.friendusername='" + self.h + "' and info.username=friends.myusername and accepted='No'"
            cr.execute(asss)
            aas = cr.fetchone()
            a = "You Have "
            b = " Requests"
            df = a + str(aas[0]) + b
            self.re.destroy()
            self.re = Label(self.f6, text=df)
            self.re.grid(row=3, column=0)
            cr.close()
            conn.commit()
            for row in self.t4.get_children():
                self.t4.delete(row)
            showinfo("","Added")

        def decline():
            conn = sqlite3.connect("db.sqlite3")
            cr = conn.cursor()
            ex = "delete from `friends` where myusername='" + self.test['values'][1] + "' and friendusername='" + self.h + "'"
            cr.execute(ex)
            r = cr.fetchall()
            cr.close()
            conn.commit()
            self.win11.withdraw()
            conn = sqlite3.connect("db.sqlite3")
            cr = conn.cursor()
            asss = "select count(*) from friends,info where friends.friendusername='" + self.h + "' and info.username=friends.myusername and  accepted='No'"
            cr.execute(asss)
            aas = cr.fetchone()
            a = "You Have "
            b = " Requests"
            df = a + str(aas[0]) + b
            self.re.destroy()
            self.re = Label(self.f6, text=df)
            self.re.grid(row=3, column=0)
            cr.close()
            conn.commit()

            for row in self.t4.get_children():
                self.t4.delete(row)
            showinfo("", "Removed")

        self.win11=Tk()
        self.nn=Label(self.win11,text="Name")
        self.nn1=Label(self.win11,text=self.test['values'][0])
        self.nn.grid(row=0,column=0)
        self.nn1.grid(row=0,column=1)

        self.uu=Label(self.win11,text="Username")
        self.uu1=Label(self.win11,text=self.test['values'][1])
        self.uu.grid(row=1,column=0)
        self.uu1.grid(row=1,column=1)

        self.decbtn=Button(self.win11,text="Decline",command=decline)
        self.accbtn=Button(self.win11,text="Accept",command=accept)

        self.decbtn.grid(row=3,column=0)
        self.accbtn.grid(row=3,column=1)


        self.win11.mainloop()


    def myrequests(self):
        conn = sqlite3.connect("db.sqlite3")
        cr=conn.cursor()
        fd="select info.name,friends.myusername ,info.gender from friends,info where friends.friendusername='"+self.h+"' and info.username=friends.myusername and friends.accepted='No'"
        cr.execute(fd)
        hg=cr.fetchall()
        cr.close()
        self.win8=Tk()
        self.win8.title("My Requests")
        self.t4=Treeview(self.win8,columns=("name","username","gender"))
        self.t4.heading("name",text="Name")
        self.t4.heading("username",text="Username")
        self.t4.heading("gender",text="Gender")
        self.t4["show"]="headings"

        i=0
        for ij in hg:
            self.t4.insert("",index=i,values=ij)
        self.t4.pack()
        self.t4.bind("<<TreeviewSelect>>", self.accordel)

        self.win8.mainloop()




    def displaymyfriendlist(self):
        conn = sqlite3.connect("db.sqlite3")
        cr=conn.cursor()
        ck="select friendusername from friends where accepted='Yes'"
        ckk = "select myusername from friends where accepted='Yes'"
        cr.execute(ck)
        fred=cr.fetchall()
        cr.execute(ckk)
        myed = cr.fetchall()
        print(myed)
        print(fred)






        self.flist=Tk()
        self.flist.title("My Friends")
        self.t3=Treeview(self.flist,columns=("acc","name","username","gender"))
        self.t3.heading("acc",text="Accepted?")
        self.t3.heading("name",text="Name")
        self.t3.heading("username",text="Username")
        self.t3.heading("gender",text="Gender")
        self.t3["show"]="headings"
        self.t3.column("acc", anchor="center")
        self.t3.column("name", anchor="center")
        self.t3.column("username", anchor="center")
        self.t3.column("gender", anchor="center")

        for myed1 in myed:
            print(str(myed1[0]))
            if (str(myed1[0]) == self.h or str(myed1[0][1])==self.h):
                kjh = "select accepted,friendname,friendusername,friendgender from friends where myusername='" + self.h + "' and accepted='Yes'"
                cr.execute(kjh)
                self.tr = cr.fetchall()
        for fred1 in fred:
            if (str(fred1[0]) == self.h or str(fred1[0][1])==self.h):
                kjhh = "select accepted,myname,myusername,mygender from friends where friendusername='" + self.h + "' and accepted='Yes'"
                cr.execute(kjhh)
                self.tr = cr.fetchall()
        try:
            i = 0
            for f in self.tr:
                self.t3.insert("", index=i, values=f)
            self.t3.pack()
            self.flist.mainloop()
        except:
            self.flist.withdraw()
            showinfo("","Friend List is Empty")
            self.findfriend()



    def delreq(self):
        conn = sqlite3.connect("db.sqlite3")
        cr=conn.cursor()
        ex="delete from `friends` where friendusername='"+self.us+"' and myusername='"+self.h+"'"
        cr.execute(ex)
        r=cr.fetchall()
        cr.close()
        conn.commit()
        addwin.destroy()
        showinfo("","Unsent Successfully")

    def add(self,event):
        self.a = timedis = tm.strftime('%I:%M:%S %p')
        self.now = dt.datetime.now()
        self.g = self.now.strftime("%d-%m-%Y")
        def sendreq():
            conn = sqlite3.connect("db.sqlite3")
            cr=conn.cursor()
            lk="select gender from info where username='"+usernameu+"'"
            cr.execute(lk)
            lkkk=cr.fetchone()
            s="INSERT INTO `friends`(`myname`,`myusername`,`mygender`, `friendname`, `friendusername`,`friendgender` ,`accepted`,`dateofreqsent`,`timeofreqsent`) VALUES ('"+self.name[0]+"','"+self.h+"','"+self.name[1]+"','"+nameof+"','"+usernameu+"','"+lkkk[0]+"','No','"+self.g+"','"+self.a+"')"
            cr.execute(s)
            cr.close()
            conn.commit()
            addwin.destroy()
            showinfo("Done👍","Successfully Sent")

        def call():
            global addwin,usernameu
            addwin=Tk()
            self.item = self.t2.item(self.t2.selection())
            nameof = (self.item['values'][0])
            usernameu = self.item['values'][1]
            self.us = usernameu
            n1 = Label(addwin, text="Name").grid(row=0, column=0)
            n = Label(addwin, text=self.item['values'][0]).grid(row=0, column=1)
            u1 = Label(addwin, text="Username").grid(row=1, column=0)
            u = Label(addwin, text=self.item['values'][1]).grid(row=1, column=1)
            conn = sqlite3.connect("db.sqlite3")
            cr = conn.cursor()
            d = "select friendusername from friends where myusername='" + self.h + "'"
            cr.execute(d)
            re=cr.fetchall()
            ex = "select accepted from friends where (myusername='" +usernameu+ "' and friendusername='" + self.h + "') or(friendusername='" +usernameu+ "' and myusername='" + self.h + "')"
            cr.execute(ex)
            qi = cr.fetchall()
            for self.ij in qi:
                print(str(self.ij[0]))
                print(str(self.ij[0])=='Yes')

            flag=0
            for i in re:
                if(str(i[0])==self.item['values'][1]):
                    flag=1
                    break
            if(not re):
                b = Button(addwin, text="Send Req.", command=sendreq).grid(row=2, column=1)
            elif(flag==0):
                b=Button(addwin,text="Send Req.",command=lambda :[sendreq()]).grid(row=2,column=1)
            elif(str(self.ij[0])=='Yes'):

                b = Button(addwin, text="You Are Already Friends", command=lambda: showinfo("", "You are Friends")).grid(row=2, column=1)
            else:
                b = Button(addwin, text="Already Sent",command=lambda :showinfo("","Already Sent")).grid(row=2, column=1)
                bn = Button(addwin, text="Cancel Req.", command=self.delreq).grid(row=2, column=0)

            addwin.mainloop()

        self.item = self.t2.item(self.t2.selection())
        nameof = (self.item['values'][0])
        usernameu = self.item['values'][1]
        call()
    def findfriend(self):

        def search():
            for row in self.t2.get_children():
                self.t2.delete(row)
            s="select name,username from info where (name like '%"+self.searchbar.get()+"%' or username like '%"+self.searchbar.get()+"%') and username not in('"+self.h+"') "
            cr.execute(s)
            show=cr.fetchall()
            i=0
            for r in show:
                self.t2.insert("",index=i,values=r)
            self.t2.pack()
            self.t2.bind("<<TreeviewSelect>>", self.add)

        conn = sqlite3.connect("db.sqlite3")
        cr=conn.cursor()
        self.win7=Tk()
        self.f3=Frame(self.win7)
        self.f4=Frame(self.win7)


        self.t2=Treeview(self.f4,columns=("name","username"))
        self.t2.heading("username",text="Username")
        self.t2.heading("name",text="Name")
        self.t2.column("username",anchor="center")
        self.t2["show"]="headings"




        self.win7.title("Find Friends")
        self.searchbar=Entry(self.f3)
        self.searchbtn=Button(self.f3,text="Search",command=search)


        self.searchbar.grid(row=0,column=0)
        self.searchbtn.grid(row=0,column=1)
        self.f3.pack()
        self.f4.pack()
        self.win7.mainloop()



    def logind(self,username,password):
        global name,h
        self.root = Tk()
        self.f5=Frame(self.root)
        self.f6=Frame(self.root)
        self.f7=Frame(self.root)
        self.root.title("Welcome!")
    # -------------------------------------------time and date
        self.a = timedis = tm.strftime('%I:%M:%S %p')  # --I is used to Print time in 12hour format and P is used to print AM or PM
    # self.timedis=tm.strftime('%H:%M:%S')---->it will print time in 24 Hour Format
        self.now = dt.datetime.now()
        self.g = self.now.strftime("%d-%m-%Y")
    # ----
        self.lb1 = Label(self.f5, text="Login Time:")
        self.lb2 = Label(self.f5, text=self.a)
        self.sp = Label(self.f5, text="      ")
        self.lb3 = Label(self.f5, text="Date of Login")
        self.lb4 = Label(self.f5, text=self.g)
    #---displaying user's name
        conn = sqlite3.connect("db.sqlite3")
        cr=conn.cursor()
        username=self.h
        password=self.txt2.get()

        q="select name,gender from info where username='"+self.h+"'"
        cr.execute(q)
        self.name=cr.fetchone()
        self.lb6=Label(self.f5,text="Welcome")
        self.lb6.config(font=("Arial", 10))
        self.lb5=Label(self.f5,text=self.name[0])
        self.lb5.config(font=("Courier", 10))
        self.findf=Button(self.f5,text="Find Friends",command=self.findfriend)
        self.findf.grid(row=2,column=0)

        asss="select count(*) from friends,info where friends.friendusername='"+self.h+"' and info.username=friends.myusername and accepted='No'"
        cr.execute(asss)
        aas=cr.fetchone()
        a="You Have "
        b=" Requests"
        df=a+str(aas[0])+b
        self.re=Label(self.f6,text=df)
        self.re.grid(row=3,column=0)
        self.btt=Button(self.f6,text="My Requests",command=self.myrequests)
        self.btt.grid(row=3,column=1)
        self.logout=Button(self.f7,text="Log Out",command=lambda :[self.root.destroy(),self.__init__()])
        self.logout.grid(row=6,column=2)
        self.lb6.grid(row=1,column=0)
        self.lb5.grid(row=1,column=1)
        # ----
        self.lb1.grid(row=0, column=0)
        self.lb2.grid(row=0, column=1)
        self.sp.grid(row=0, column=2)
        self.lb3.grid(row=0, column=3)
        self.lb4.grid(row=0, column=4)

        self.mymenu=Menu(self.root)
        self.root.config(menu=self.mymenu)

        submenu1=Menu(self.mymenu,tearoff=False)
        self.mymenu.add_cascade(label="ADD",menu=submenu1)
        submenu1.add_command(label="ADD Friends",command=self.findfriend)
        submenu1.add_command(label="@nd")

        submenu2 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Edit", menu=submenu2)
        submenu2.add_command(label="Name",command=self.editname)
        submenu2.add_command(label="Password",command=self.editpass)
        submenu2.add_command(label="Security Answer",command=self.editseqans)

        submenu3 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="View", menu=submenu3)
        submenu3.add_command(label="Your Account",command=self.accountinformation)
        submenu3.add_command(label="My Friends",command=self.displaymyfriendlist)
        submenu3.add_command(label="My Requests", command=self.myrequests)
        submenu3.add_command(label="No. of Time Login's",command=self.logincount)



        self.f5.pack()
        self.f6.pack()
        self.f7.pack()
        self.root.mainloop()

    def __init__(self):
        global txt1, root, txt2

        self.win=Tk()

        self.win.title("Login Here")
        self.hed=Label(self.win,text="LOGIN your ACCOUNT")
        self.lb1=Label(self.win,text="Enter Username")
        self.txt1=Entry(self.win)
        self.lb2=Label(self.win,text="Enter Password")
        self.txt2=Entry(self.win,show="*")
        self.bt1=Button(self.win,text="Login",command=lambda:[self.show()])
        self.bt2=Button(self.win,text="Show Password",command=self.passshow)


        self.bt3=Button(self.win,text="Forgot Password?",command=self.page)
        self.ll=Label(self.win,text="------------")
        self.ll.grid(row=5,column=0)
        self.sin=Button(self.win,text="SIGNUP",command=self.sign)
        self.sin.grid(row=6,column=0)

        self.hed.grid(row=0,column=1)
        self.lb1.grid(row=1,column=0)
        self.txt1.grid(row=1,column=1)
        self.lb2.grid(row=2,column=0)
        self.txt2.grid(row=2,column=1)
        self.bt2.grid(row=3,column=0)
        self.bt1.grid(row=4,column=1)
        self.bt3.grid(row=4,column=0)
        self.win.mainloop()
#--------------

