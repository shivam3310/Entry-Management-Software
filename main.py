from datetime import datetime
from tkinter import *
from mail import *
from message import *

def entry(e1,e2,e3,e4,e5,e6):                           # if check-in button is selected then this function is called.
    try:
        import mysql.connector
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "keshav123",
            database = "testdb"
        )

        mycursor = mydb.cursor()
        sqlformula_visitor = "INSERT INTO visitors (Name,Phone,Mail) VALUES (%s,%s,%s)"
        sqlformula_host = "INSERT INTO host (Name,Phone,Mail) VALUES (%s,%s,%s)"
        entry1 = (e1,e3,e2)
        entry2 = (e4,e6,e5)
        entry3 = (e3,e6,datetime.now().strftime("%H:%M:%S"))

        mycursor.execute("SELECT * from visitors where Phone = (%s)",(e3,))
        vcheck = mycursor.fetchall()
        #mycursor.execute("INSERT INTO visitors (Name,Phone,Mail) VALUES (%s,%s,%s)",(e1,e3,e2))
        if len(vcheck) == 0:
            mycursor.execute("INSERT INTO visitors (Name,Phone,Mail) VALUES (%s,%s,%s)",(e1,e3,e2))
            mydb.commit()

        mycursor.execute("SELECT * from host where Phone = (%s)", (e6,))
        hcheck = mycursor.fetchall()
        if len(hcheck) == 0:
            mycursor.execute("INSERT INTO host VALUES (%s,%s,%s)", (e4, e6, e5))
            mydb.commit()
        time = datetime.now()
        itime = time.strftime("%Y-%m-%d %H:%M:%S")
        print(type(time))
        mycursor.execute("INSERT INTO visit VALUES (%s,%s,%s,%s)", (e3, e6, itime,"Null"))
        mydb.commit()

        emailh(e5,e1,e3,e2,itime,e6)
    except:
        return
    exit()


def exit1(num):                                         # if check-out button is selected then this function is called.
    import mysql.connector
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "keshav123",
        database = "testdb"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT Outtime from visit where vphone = (%s) AND Outtime = (%s)", (num,'Null'))
    hcheck = mycursor.fetchall()

    if hcheck[0][0] == 'Null':
        time = datetime.now()
        otime = time.strftime("%Y-%m-%d %H:%M:%S")
        mycursor.execute("UPDATE visit SET Outtime = (%s) WHERE vphone = (%s) AND Outtime = (%s)", (otime,num,'Null'))
        mydb.commit()

        mycursor.execute("SELECT Outtime from visit where Outtime = (%s)", (otime,))
        outtime = mycursor.fetchall()

        mycursor.execute("SELECT  Intime from visit where Outtime = (%s)", (otime,))
        intime = mycursor.fetchall()
        intime = intime[0][0]

        mycursor.execute("SELECT hphone from visit where Outtime = (%s)", (otime,))
        hphone = mycursor.fetchall()

        hphone = hphone[0][0]
        vphone = num

        mycursor.execute("SELECT Mail from host WHERE Phone = (%s)",(hphone,))
        hmail = mycursor.fetchall()

        hmail = hmail[0][0]

        mycursor.execute("SELECT Name from host WHERE Phone = (%s)", (hphone,))
        hname = mycursor.fetchall()
        hname = hname[0][0]

        mycursor.execute("SELECT Mail from visitors WHERE Phone = (%s)",(vphone,))
        vmail = mycursor.fetchall()
        vmail = vmail[0][0]

        mycursor.execute("SELECT Name from visitors WHERE Phone = (%s)", (vphone,))
        vname = mycursor.fetchall()
        vname = vname[0][0]

    emailv(hname,vname,vphone,vmail,intime,outtime)
    exit()

def start():
    window = Tk()
    window.title('Entry')
    window.geometry("600x500")

    head1 = Label(window,
             text="For Check-in proceed over here",
             fg="black",
             font="Times")

    head1.place(x=110, y=15)

    label1 = Label(window, bg="white",fg='black', text="Visitor name")
    label1.place(x=60, y=50)
    e1 = Entry(window, text="")
    e1.place(x=200, y=50)

    label2 = Label(window, bg="white", fg='black', text="Visitor E-mail id")
    label2.place(x=60, y=90)
    e2 = Entry(window, text="")
    e2.place(x=200, y=90)

    label3 = Label(window, bg="white", fg='black', text="Visitor Mobile No.")
    label3.place(x=60, y=130)
    e3 = Entry(window, text="")
    e3.place(x=200, y=130)

    label4 = Label(window, bg="white", fg='black', text="Host Name")
    label4.place(x=60, y=170)
    e4 = Entry(window, text="")
    e4.place(x=200, y=170)

    label5 = Label(window, bg="white", fg='black', text="Host E-mail id")
    label5.place(x=60, y=210)
    e5 = Entry(window, text="")
    e5.place(x=200, y=210)

    label6 = Label(window, bg="white", fg='black', text="Host Mobile No.")
    label6.place(x=60, y=250)
    e6 = Entry(window, text="")
    e6.place(x=200, y=250)

    head2 = Label(window,
          text="For Check-out proceed over here",
          fg="black",
          font="Times")

    head2.place(x=110, y=340)

    label7 = Label(window, bg="white", fg='black', text="Visitor's Mobile No.")
    label7.place(x=60, y=370)
    e7 = Entry(window, text="")
    e7.place(x=200, y=370)

    btn1 = Button(window, bg="white",fg='black',text="Check In",
                 command=lambda: entry(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()))

    btn1.place(x=160, y=290)
    btn1.bind("<Button-1>")

    btn2 = Button(window, bg="white", fg='black', text="Check Out",
                  command=lambda: exit1(e7.get()))

    btn2.place(x=160,y=400)
    btn2.bind("<Button-2>")
    window.mainloop()



start()                             # calling the start function to start the application.
