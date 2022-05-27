from ctypes import resize
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.messagebox import showerror
from abc import ABC


from pickle import NONE

email = "user1@gmail.com"
password = "12345"

regular = "1"
vip = "2"
kosong ="-"


class Info(ABC):
    confirm = None
class Member(Info):

    def __init__(self, confirm):
        self.confirm = confirm 
        pass 
    
    def setConfirm(self, confirm):
        self.confirm = confirm
        pass
    def getConfirm(self):
        return self.confirm   
    
u1 = Member("Selamat anda telah sukses melakukan registrasi")

def login():
    def total():
            daily = combobox1.get()
            monthtly = combobox2.get()
            yearly = combobox3.get()


            if (regular == daily and kosong == monthtly == yearly):
                messagebox.showinfo(message="Anda memilih paket Regular.")
                window=Tk()
                window.geometry("300x140")
                window.title("Payment")
                window.resizable(width = 0, height = 0)
                label1=Label(window, text="Total Biaya Anda: 100.000", font="arial 10 bold")
                label1.place(x=50, y=40)
                buttonsubmit=Button(window, text="OK", font="arial 10", activebackground= "gray",command=exit)
                buttonsubmit.place(x=125, y=100)
            elif (regular == monthtly and kosong == daily == yearly ):
                messagebox.showinfo(message="Anda memilih paket Regular")
                window=Tk()
                window.geometry("300x140")
                window.title("Payment")
                window.resizable(width = 0, height = 0)
                label1=Label(window, text="Total Biaya Anda: 3.000.000", font="arial 10 bold")
                label1.place(x=50, y=40)
                buttonsubmit=Button(window, text="OK", font="arial 10", activebackground= "gray", command=exit)
                buttonsubmit.place(x=125, y=100)
            elif (regular == yearly and kosong== daily== monthtly):
                messagebox.showinfo(message="Anda memilih paket Regular")
                window=Tk()
                window.geometry("300x140")
                window.title("Payment")
                window.resizable(width = 0, height = 0)
                label1=Label(window, text="Total Biaya Anda: 30.000.000", font="arial 10 bold")
                label1.place(x=50, y=40)
                buttonsubmit=Button(window, text="OK", font="arial 10", activebackground= "gray", command=exit)
                buttonsubmit.place(x=125, y=100) 
            elif (vip == daily and kosong== monthtly == yearly):
                messagebox.showinfo(message="Anda memilih paket VIP")
                window=Tk()
                window.geometry("300x140")
                window.title("Payment")
                window.resizable(width = 0, height = 0)
                label1=Label(window, text="Total Biaya Anda: 300.000", font="arial 10 bold")
                label1.place(x=50, y=40)
                buttonsubmit=Button(window, text="OK", font="arial 10", activebackground= "gray", command=exit)
                buttonsubmit.place(x=125, y=100)  
            elif (vip == monthtly and kosong == daily == yearly):
                messagebox.showinfo(message="Anda memilih paket VIP")
                window=Tk()
                window.geometry("300x140")
                window.title("Payment")
                window.resizable(width = 0, height = 0)
                label1=Label(window, text="Total Biaya Anda: 6.000.000", font="arial 10 bold")
                label1.place(x=50, y=40)
                buttonsubmit=Button(window, text="OK", font="arial 10", activebackground= "gray", command=exit)
                buttonsubmit.place(x=125, y=100)
            elif (vip == yearly and kosong == daily == monthtly):
                messagebox.showinfo(message="Anda memilih paket VIP")
                window=Tk()
                window.geometry("300x140")
                window.title("Payment")
                window.resizable(width = 0, height = 0)
                label1=Label(window, text="Total Biaya Anda: 50.000.000", font="arial 10 bold")
                label1.place(x=50, y=40)
                buttonsubmit=Button(window, text="OK", font="arial 10", activebackground= "gray", command=exit)
                buttonsubmit.place(x=125, y=100)
            else:
                messagebox.showinfo(message="Pilih 1 atau 2 pada paket yang diinginkan dan isi - pada box yang tersisa")
            
    user = entry1.get()
    pas = entry2.get()

    if (email == user and password == pas):
        messagebox.showinfo(message="You are logged in")

        window=Tk()
        window.geometry("500x350")
        window.title("Gym Club Membership")
        window.resizable(width = 0, height = 0)

        labeltitle=Label(window, text="Membership Registration Form", font="times 12 bold")
        labeltitle.place(x=160, y=10)

        labelname=Label(window, text="Nama: ", font="times 10")
        labelname.place(x=40, y=70)
        strname = StringVar()
        entryname = Entry(window, text=strname, font="times 10")
        entryname.place(x=165, y=74)

        labelphone=Label(window, text="Nomor Telepon:", font="times 10")
        labelphone.place(x=40, y=102)
        strphone = IntVar()
        entryphone = Entry(window, text=strphone, font="times 10")
        entryphone.place(x= 165, y=104)

        labelage=Label(window, text="Umur:", font="times 10")
        labelage.place(x=40, y= 135)
        strage = IntVar()
        entryage = Entry(window, text=strage, font="times 10")
        entryage.place(x= 165, y=135)

        labelprice = Label(window, text= "Pilih Paket", font="times 11 underline")
        labelprice.place(x =40, y = 170)

        strprice1 = IntVar(value='1 or 2')
        combobox1 = ttk.Combobox(window, width=15, font="times 10", textvariable=strprice1, state="readonly")
        combobox1.place(x=165, y=200)
        combobox1['values'] = ('-','1','2')
        labelprice1 = Label(window, text= "Daily", font="times 10")
        labelprice1.place(x=40, y=200)

        strprice2 = IntVar(value='1 or 2')
        combobox2 = ttk.Combobox(window, width=15, font="times 10", textvariable=strprice2, state="readonly")
        combobox2.place(x=165, y=225)
        combobox2['values'] = ('-','1','2')
        labelprice2 = Label(window, text= "Monthly", font="times 10")
        labelprice2.place(x=40, y=225)

        strprice3 = IntVar(value='1 or 2')
        combobox3 = ttk.Combobox(window, width=15, font="times 10", textvariable=strprice3, state="readonly")
        combobox3.place(x=165, y=250)
        combobox3['values'] = ('-','1','2')
        labelprice3 = Label(window, text= "Yearly", font="times 10")
        labelprice3.place(x=40, y=250)

        labelpackage1 = Label(window, text="(1) \nRegular\n100.000\n3.000.000\n30.000.000", font="arial 10", width="10", height="6", foreground="black", background="white")
        labelpackage1.place(x=300, y=180 )
        labelpackage2 = Label(window, text="(2) \nVIP\n300.000\n6.000.000\n50.000.000", font="arial 10", width="9", height="6", foreground="black", background="white")
        labelpackage2.place(x=380, y=180 )

        buttonsubmit = Button(window,
                    text = "Submit",
                    font = ("arial 10"),
                    command= total,
                    fg = "black",
                    activebackground= "gray",
                    state = ACTIVE
                    ).place(x = 225, y = 300)
    else: 
        messagebox.showwarning(message="User not found")    
    

def exit():
    print(showinfo("Confirmation",(u1.getConfirm())))
    

window=Tk()

window.geometry("300x140")
window.title("Gym Login Page")
window.resizable(width = 0, height = 0)
label1= Label(window, text="Email: ",font="arial 10")
label1.place(x=45, y=30)
label2=Label(window, text="Password: ", font="arial 10")
label2.place(x=45, y=60)

stremail = StringVar()
entry1 = Entry(window, text=stremail, font="times 10")
entry1.place(x=95, y=30)
strpass = StringVar()
entry2 = Entry(window, text=strpass, font="times 10")
entry2.place(x=120, y=60)

buttonsubmit = Button(window,
                    text = "Login",
                    command = login,
                    font = ("arial 10"),
                    fg = "black",
                    activebackground= "gray",
                    state = ACTIVE
                    ).place(x = 120, y = 100)
window.mainloop()