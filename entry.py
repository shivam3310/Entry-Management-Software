def entry(e1,e2,e3,e4,e5,e6):
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