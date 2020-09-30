from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
import smtplib
import random
import sqlite3


class signup:
    def verify(self):
        flag = 1

        if (str(self.txt5.get()).count("@")!=1  or str(self.txt5.get()).count(".")<1 or self.txt5.get().strip("")==""):
            showinfo("INVALID", "Not a Valid E-Mail")
        else:
            try:
                self.otp=random.randint(1001,9999)
                print(self.otp)
                msg1="Thanks for Using My software\n"
                msg2="Regards - Sairish(Developer)\n"
                msg3="Please Verify Your E-Mail using OTP."
                msg4="\nYour OTP is "
                msg5=str(self.otp)
                msg=msg1+msg2+msg3+msg4+msg5
                user = 'emailaddress'
                password = 'emailpassword'
                sender = self.txt5.get()
                subject = "Verify Your E-Mail "
                message = "Subject: {} \n\n{}".format(subject,msg)
                send_to = ("{}".format(sender))
                mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                mail.ehlo()
                mail.login(user, password)
                mail.sendmail(user, send_to, message)
                mail.close()
                print("Success Email!")
                flag=0
                self.lbb=Label(self.wi,text="Enter OTP")
                self.txt6=Entry(self.wi)
                self.bt4 = Button(self.wi, text="VERIFY", command=self.otpchk)



                self.lbb.grid(row=11,column=0)
                self.txt6.grid(row=11,column=1)
                self.bt4.grid(row=11,column=2)

            except:
                showerror("Error","Error While Sending")

        if (flag==0):

            self.lb10 = Label(self.wi, text="Sent")
            self.lb10.grid(row=10, column=2)


    def otpchk(self):

        if (self.txt6.get()==str(self.otp)):
            self.vr = Label(self.wi, text="Verified")
            self.vr.grid(row=12, column=2)
            self.bt1["state"]="enable"
            self.txt6.config(state='disabled')
            self.txt1.config(state='disabled')
            self.txt2.config(state='disabled')
            self.txt3.config(state='disabled')
            self.txt4.config(state='disabled')
            self.txt5.config(state='disabled')
            self.txt6.config(state='disabled')
            self.ans.config(state='disabled')
            self.rd1.config(state='disabled')
            self.rd2.config(state='disabled')
            self.cb1.config(state='disabled')
            self.bt4['state']='disable'




        else:
            self.vr = Label(self.wi, text="Incorrect")
            self.vr.grid(row=11, column=2)
            self.bt1["state"]="disable"

    def showpass(self):
        self.swp = Label(self.wi, text=self.txt3.get())
        self.swp.grid(row=5, column=1)

    def add(self):
        conn = sqlite3.connect("db.sqlite3")
        s = "select username from info"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        if (self.txt1.get().strip("") == "" or self.txt2.get().strip("") == "" or self.txt3.get().strip(
                "") == "" or self.cb1.get() == "" or self.txt4.get().strip("") == ""):
            showinfo("Don't Leave any Field", "Every Field is Mandatory")

        elif (self.txt3.get() != self.txt4.get()):
            showerror("PASSWORD!", "Password Does not Match")
            self.txt3.config(state='enabled')
            self.txt4.config(state='enabled')
        else:

            flag = 0
            for i in result:
                if (str(i[0]) == self.txt2.get()):
                    flag = 1
                    break
            if flag == 1:
                showinfo("OOPS!", "Username Already Exists")
                self.txt2.config(state='enabled')

            else:
                conn = sqlite3.connect("db.sqlite3")                
                cr = conn.cursor()
                q = "insert into info values('" + self.txt1.get() + "','" + self.txt2.get() + "','" + self.txt3.get() + "','" + self.gh.get() + "','" + self.cb1.get() + "','" + self.ans.get() + "','"+self.txt5.get()+"')"

                cr.execute(q)
                conn.commit()
                showinfo("Yehh!!", "Account Created Successfully")
                self.txt1.config(state='enabled')
                self.txt2.config(state='enabled')
                self.txt3.config(state='enabled')
                self.txt4.config(state='enabled')
                self.txt5.config(state='enabled')
                self.txt6.config(state='enabled')
                self.ans.config(state='enabled')
                self.rd1.config(state='enabled')
                self.rd2.config(state='enabled')
                self.cb1.config(state='enabled')

                #sending user it's account information using email
                try:
                    nam=self.txt1.get()
                    msg1 = "Thanks "
                    ms=" for Using My software\n"
                    msg2 = "Regards - Sairish(Developer)\n"
                    msg3 = "Your Account Has Succesfully been Created"
                    msg4 = "\nYou Can Login By your"
                    msg5 = "\nUsername: "
                    msg6=self.txt2.get()
                    msg7="\nPassword: "
                    msg8=self.txt3.get()
                    msg = msg1 + nam + ms + msg2 + msg3 + msg4 + msg5+ msg6 + msg7 + msg8

                    user = 'downinnwh@gmail.com'
                    password = 'sairish12'

                    sender = self.txt5.get()

                    subject = "Account Created Successfully "
                    message = "Subject: {} \n\n{}".format(subject, msg)
                    send_to = ("{}".format(sender))

                    mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    mail.ehlo()
                    mail.login(user, password)
                    mail.sendmail(user, send_to, message)
                    mail.close()
                    print("Success Email!")
                except:
                    print("Sending Failed")

                #---------------------------


                self.txt1.delete(0,'end')
                self.txt2.delete(0, 'end')
                self.gh.set(NONE)
                self.gh.set(NONE)
                self.txt3.delete(0, 'end')
                self.txt4.delete(0, 'end')
                self.cb1.set("")
                self.ans.delete(0, 'end')
                self.txt6.delete(0,'end')
                self.txt5.delete(0,'end')


                self.wi.destroy()
                #root.after(20000, lambda: root.destroy())




    def __init__(self):

        self.wi = Tk()
        self.wi.title("Create Your New Account")

        self.lb1 = Label(self.wi, text="Enter full Name")
        self.txt1 = Entry(self.wi)

        self.lb2 = Label(self.wi, text="Enter Username")
        self.txt2 = Entry(self.wi)

        self.lb3 = Label(self.wi, text="Select Gender")
        self.gh = StringVar(self.wi, "1")
        self.gh = StringVar(self.wi, "2")
        self.rd1 = Radiobutton(self.wi, text="Male", var=self.gh, value="Male")
        self.rd2 = Radiobutton(self.wi, text="Female", var=self.gh, value="Female")

        self.lb4 = Label(self.wi, text="Enter Password")
        self.txt3 = Entry(self.wi, show="*")

        self.lb5 = Label(self.wi, text="Re-Enter Password")
        self.txt4 = Entry(self.wi, show="*")
        self.bt2 = Button(self.wi, text="Show Password", command=self.showpass)

        self.lb6 = Label(self.wi, text="Select Your Security Quesion")
        self.cb1 = Combobox(self.wi, values=(
            "What is Your favourite Book?", "Which is Your First School?", "What is the name of your best friend?",
            "Which is your Favourite Subject?", "Which is Your Favourite Sports?"), state="readonly", width=30)
        self.lb8 = Label(self.wi, text="Answer Here(case sensitive)")
        self.ans = Entry(self.wi)
        self.lb9=Label(self.wi,text="Enter E-Mail")

        self.txt5=Entry(self.wi)
        self.bt3=Button(self.wi,text="Send OTP",command=lambda:[self.verify()])




        self.lb1.grid(row=0, column=0)
        self.txt1.grid(row=0, column=1)
        self.lb2.grid(row=1, column=0)
        self.txt2.grid(row=1, column=1)
        self.lb3.grid(row=2, column=0)
        self.rd1.grid(row=2, column=1)
        self.rd2.grid(row=2, column=2)
        self.lb4.grid(row=3, column=0)
        self.txt3.grid(row=3, column=1)
        self.lb5.grid(row=4, column=0)
        self.txt4.grid(row=4, column=1)
        self.lb6.grid(row=6, column=1)
        self.cb1.grid(row=7, column=1)
        self.lb8.grid(row=8, column=0)
        self.ans.grid(row=8, column=1)
        self.lb9.grid(row=9,column=0)
        self.txt5.grid(row=9,column=1)
        self.bt3.grid(row=9,column=2)
        self.bt2.grid(row=5, column=0)

        self.bt1 = Button(self.wi, text="Create Account", command=self.add)
        self.bt1.grid(row=14, column=1)
        self.bt1["state"] = "disable"

        self.wi.mainloop()
# ------------------------------------
