from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import mysql.connector
from pyttsx3 import speak
def on_enter(e):
    user.delete(0,'end')
    pass
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')
    pass

def signup_command():
    def on_enter(e):
        user.delete(0,'end')
        pass
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Username')
        pass

    def signup():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='game',
                                                 user='root',
                                                 password='1234')
            cursor = connection.cursor()
            query = "CREATE TABLE IF NOT EXISTS USER(username varchar(30) primary key, password varchar(30));"
            cursor.execute(query)
            query = "CREATE TABLE IF NOT EXISTS GAMESS(game_ID varchar(30) primary key, name varchar(30), genre varchar(30), release_year varchar(30), creator varchar(30), price int, duration int, critic_rating int)"
            cursor.execute(query)
            username = user.get()
            passw1 = code.get()
            passw2 = confirm_code.get()
            if passw1 == passw2:
                validate = []
                query1 = "SELECT username FROM USER"
                cursor.execute(query1)
                results = cursor.fetchall()
                for row in results:
                    for x in row:
                        validate.append(row)
                print(validate)
                if username in validate or username.lower() == 'admin':
                    messagebox.showerror("Invalid","Username already taken")
                    print(3)
                else:
                    query2 = """INSERT INTO USER(username, password)
                                VALUES (%s,%s)"""
                    record = (username,passw1)
                    cursor.execute(query2,record)
                    speak(f"Welcome {username}")
                    #show = []
                    #query3 = "SELECT * FROM USER"
                    #cursor.execute(query3)
                    #res = cursor.fetchall()
                    #for row in res:
                        #for x in row:
                        #    show.append(x)
                    #print(show)
                    #print(2)
                connection.commit()
                window.destroy()
            else:
                messagebox.showerror("Invalid","Passwords do not match")
                speak("Sorry the passwords don't match")
                print(1)
        except:
            messagebox.showerror("Invalid","Username is already taken")
            speak("Sorry username already taken")
    
    def sign():
        window.destroy()
    


    window = Toplevel(root)
    window.title("Database")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)
    img = PhotoImage(file='login.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=90)
    frame = Frame(window,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)
    heading = Label(frame,text='Sign up',fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=5)
    user = Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    def on_enter(e):
        code.delete(0,'end')
        pass
    def on_leave(e):
        if code.get()=='':
            code.insert(0,'Password')
        pass

    code = Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    def on_enter(e):
        confirm_code.delete(0,'end')
        pass
    def on_leave(e):
        if confirm_code.get()=='':
            confirm_code.insert(0,'Confirm Password')
        pass

    confirm_code = Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
    confirm_code.place(x=30,y=220)
    confirm_code.insert(0,'Confirm Password')
    confirm_code.bind("<FocusIn>",on_enter)
    confirm_code.bind("<FocusOut>",on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
    label = Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
    label.place(x=90,y=340)

    signin = Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
    signin.place(x=300,y=340)
    window.mainloop()

def signinn():
    username = user.get()
    password = code.get()
    storing = []
    try:
        tuser,q,t1,t2,t3,t4,t5,t6,t7,t8,q3 = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
        connection = mysql.connector.connect(host='localhost',
                                             database='game',
                                             user='root',
                                             password='1234')
        cursor = connection.cursor()
        query = "CREATE TABLE IF NOT EXISTS GAMESS(game_ID varchar(30) primary key, name varchar(30), genre varchar(30), release_year varchar(30), creator varchar(30), price int, duration int, critic_rating int)"
        cursor.execute(query)
        query = "SELECT * FROM USER"
        cursor.execute(query)
        result = cursor.fetchall()
        rec = (username,password)
        if username == "admin" and password == "1234":
            def update(rows):
                trv.delete(*trv.get_children())
                for i in rows:
                    trv.insert('','end',values=i)
            def update1(rows):
                trv1.delete(*trv1.get_children())
                for i in rows:
                    trv1.insert('','end',values=i)
            def clear():
                query = "SELECT * FROM GAMESS"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("CLEAR successful")
            def clear1():
                query = "SELECT username FROM USER"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update1(rows)
                print("CLEAR successful")
            def insertion():
                a = t1.get()
                b = t2.get()
                c = t3.get()
                d = t4.get()
                e = t5.get()
                f = t6.get()
                g = t7.get()
                h = t8.get()
                fint = int(f)
                gint = int(g)
                hint = int(h)
                query = "INSERT INTO GAMESS (game_ID,name,genre,release_year,creator,price,duration,critic_rating) VALUES ("+str(f"'{a}','{b}','{c}','{d}','{e}',{fint},{gint},{hint})")
                print(query)
                cursor.execute(query)
                connection.commit()
                clear()
                print("Record inserted correctly")
            def search():
                q2 = q.get()
                query = "SELECT game_ID, name, genre, release_year, creator, price, duration, critic_rating FROM GAMESS WHERE game_ID LIKE '%"+q2+"%' OR name LIKE '%"+q2+"%' OR genre LIKE '%"+q2+"%' OR release_year LIKE '%"+q2+"%' OR creator LIKE '%"+q2+"%' OR price LIKE '%"+q2+"%' OR duration LIKE '%"+q2+"%' OR critic_rating LIKE '%"+q2+"%'"
                cursor.execute(query)
                rows = cursor.fetchall()
                update(rows)
                print("SEARCH successful")
            def search1():
                qr = q3.get()
                query = "SELECT username FROM USER WHERE username LIKE '%"+qr+"%'"
                cursor.execute(query)
                rows = cursor.fetchall()
                update1(rows)
                print("SEARCH successful")
                pass
            def getrow(event):
                rowid = trv.identify_row(event.y)
                item = trv.item(trv.focus())
                t1.set(item['values'][0])
                t2.set(item['values'][1])
                t3.set(item['values'][2])
                t4.set(item['values'][3])
                t5.set(item['values'][4])
                t6.set(item['values'][5])
                t7.set(item['values'][6])
                t8.set(item['values'][7])
            def getrow1(event):
                rowid = trv1.identify_row(event.y)
                item2 = trv1.item(trv1.focus())
                tuser.set(item2['values'][0])
            def deleting():
                gameid = t1.get()
                if messagebox.askyesno("Confirm Delete?", "Are you sure you want to delete this user?"):
                    query = "DELETE FROM GAMESS WHERE game_ID ="+gameid
                    cursor.execute(query)
                    connection.commit()
                    clear()
                else:
                    return True
            def deleting1():
                userids = tuser.get()
                if messagebox.askyesno("Confirm Delete?", "Are you sure you want to delete this user?"):
                    query = 'DELETE FROM USER WHERE username = "'+userids+'"'
                    print(query)
                    cursor.execute(query)
                    connection.commit()
                    clear1()
                else:
                    return True
            def updatin():
                a = t1.get()
                b = t2.get()
                c = t3.get()
                d = t4.get()
                e = t5.get()
                f = t6.get()
                g = t7.get()
                h = t8.get()
                fint = int(f)
                gint = int(g)
                hint = int(h)
                if a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == "":
                    messagebox.showerror("Invalid","All fields must be filled")
                elif messagebox.askyesno("Confirm Please","Are you sure you want to update the game details?"):
                    query = f"UPDATE GAMESS SET name = '{b}', genre = '{c}',release_year = '{d}', creator = '{e}', price = {fint}, duration = {gint} , critic_rating = {hint} WHERE game_ID = '{a}'"
                    cursor.execute(query)
                    connection.commit()
                    clear()
                else:
                    return True
            def sort_by_id():
                query = f"SELECT * FROM GAMESS ORDER BY game_ID"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")

            def sort_by_user():
                query = f"SELECT username FROM USER ORDER BY username"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update1(rows)
                print("Sort successful")

            def sort_by_name():
                query = f"SELECT * FROM GAMESS ORDER BY name"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")            

            def sort_by_genre():
                query = f"SELECT * FROM GAMESS ORDER BY genre"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")

            def sort_by_release_year():
                query = f"SELECT * FROM GAMESS ORDER BY release_year"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")

            def sort_by_creator():
                query = f"SELECT * FROM GAMESS ORDER BY creator"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")
            
            def sort_by_price():
                query = f"SELECT * FROM GAMESS ORDER BY price"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")

            def sort_by_duration():
                query = f"SELECT * FROM GAMESS ORDER BY duration"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")
            
            def sort_by_rating():
                query = f"SELECT * FROM GAMESS ORDER BY critic_rating"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")
            screen = Toplevel(root)
            screen.title("APP")
            screen.geometry('1440x1280')
            screen.config(bg="white")
            speak(f"Hello {username}")
            wrapper1 = LabelFrame(screen,text="Game ID")
            wrapper2 = LabelFrame(screen,text="Game ID")
            wrapper3 = LabelFrame(screen,text="Game ID")
            wrapper4 = LabelFrame(screen,text="Game ID")
            wrapper1.pack(fill="both",expand="yes",padx=20,pady=10)
            wrapper2.pack(fill="both",expand="yes",padx=20,pady=10)
            wrapper3.pack(fill="both",expand="yes",padx=20,pady=10)
            wrapper4.pack(fill="both",expand="yes",padx=20,pady=10)

            trv = Treeview(wrapper1,columns=(1,2,3,4,5,6,7,8),show="headings",height="6")
            trv.pack()

            trv.heading(1,text="ID")
            trv.heading(2,text="Name")
            trv.heading(3,text="Genre")
            trv.heading(4,text="Release Year")
            trv.heading(5,text="Creator")
            trv.heading(6,text="Price")
            trv.heading(7,text="Duration")
            trv.heading(8,text="Critic Rating")

            trv1 = Treeview(wrapper2,columns=(1),show="headings",height="6")
            trv1.pack()

            trv1.heading(1,text="username")

            trv1.bind("<Double 1>",getrow1)

            query = "SELECT username FROM USER"
            cursor.execute(query)
            rows = cursor.fetchall()
            update1(rows)

            trv.bind("<Double 1>",getrow)

            query = "SELECT * FROM GAMESS"
            cursor.execute(query)
            rows = cursor.fetchall()
            update(rows)

            lab1 = Label(wrapper3,text="SEARCH:")
            lab1.place(x=10,y=20)
            serch = Entry(wrapper3,textvariable=q)
            serch.place(x=60,y=20)
            btserch = Button(wrapper3,text="SEARCH",command=search)
            btserch.place(x=195,y=18)
            btclc = Button(wrapper3,text="CLEAR",command=clear)
            btclc.place(x=260,y=18)
            Frame(wrapper3,width=2,height=500,bg='black').place(x=335,y=-10)
            lbl = Label(wrapper3, text='Game ID:')
            lbl.grid(row=0,column=0,padx=360,pady=3)
            en1 = Entry(wrapper3,textvariable=t1)
            en1.place(x=460,y=3)
            lbl2 = Label(wrapper3,text="Name:")
            lbl2.grid(row=1,column=0,padx=360,pady=3)
            en2 = Entry(wrapper3,textvariable=t2)
            en2.place(x=460,y=30)
            lbl3 = Label(wrapper3, text='Genre:')
            lbl3.grid(row=2,column=0,padx=360,pady=3)
            en3 = Entry(wrapper3,textvariable=t3)
            en3.place(x=460,y=57)
            lbl4 = Label(wrapper3,text="Release Year:")
            lbl4.grid(row=3,column=0,padx=360,pady=3)
            en4 = Entry(wrapper3,textvariable=t4)
            en4.place(x=460,y=84)
            lbl5 = Label(wrapper3, text='Creator:')
            lbl5.grid(row=4,column=0,padx=360,pady=3)
            en5 = Entry(wrapper3,textvariable=t5)
            en5.place(x=460,y=111)  
            lbl6 = Label(wrapper3,text="Price:")
            lbl6.grid(row=5,column=0,padx=360,pady=3)
            en6 = Entry(wrapper3,textvariable=t6)
            en6.place(x=460,y=138)
            lbl7 = Label(wrapper3, text='Duration:')
            lbl7.grid(row=6,column=0,padx=360,pady=3)
            en7 = Entry(wrapper3,textvariable=t7)
            en7.place(x=460,y=165)
            lbl8 = Label(wrapper3,text="Critic Rating:")
            lbl8.grid(row=7,column=0,padx=360,pady=3)
            en8 = Entry(wrapper3,textvariable=t8)
            en8.place(x=460,y=192)
            up_btn = Button(wrapper3,text="Update",command=updatin)
            up_btn.grid(row=8,column=0,padx=360,pady=3)
            add_btn = Button(wrapper3,text="Add New",command=insertion)
            add_btn.place(x=460,y=219)
            del_btn = Button(wrapper3,text="Delete",command=deleting)
            del_btn.place(x=550,y=219)
            Frame(wrapper3,width=2,height=500,bg='black').place(x=625,y=-10)
            heading = Label(wrapper3,text="SORT BY")
            heading.place(x=675,y=3)
            sort1 = Button(wrapper3,text="ID",command=sort_by_id)
            sort1.place(x=675,y=30)
            sort2 = Button(wrapper3,text="Name",command=sort_by_name)
            sort2.place(x=675,y=57)
            sort3 = Button(wrapper3,text="Genre",command=sort_by_genre)
            sort3.place(x=675,y=84)
            sort4 = Button(wrapper3,text="Release Year",command=sort_by_release_year)
            sort4.place(x=675,y=111)
            sort5 = Button(wrapper3,text="Creator",command=sort_by_creator)
            sort5.place(x=675,y=138)
            sort6 = Button(wrapper3,text="Price",command=sort_by_price)
            sort6.place(x=675,y=165)
            sort7 = Button(wrapper3,text="Duration",command=sort_by_duration)
            sort7.place(x=675,y=192)
            sort8 = Button(wrapper3,text="Critic Rating",command=sort_by_rating)
            sort8.place(x=675,y=219)


            lab12 = Label(wrapper4,text="SEARCH:")
            lab12.place(x=10,y=20)
            serch2 = Entry(wrapper4,textvariable=q3)
            serch2.place(x=60,y=20)
            btserch2 = Button(wrapper4,text="SEARCH",command=search1)
            btserch2.place(x=195,y=18)
            btclc2 = Button(wrapper4,text="CLEAR",command=clear1)
            btclc2.place(x=260,y=18)
            Frame(wrapper4,width=2,height=500,bg='black').place(x=335,y=-10)
            lbl2 = Label(wrapper4, text='Username:')
            lbl2.grid(row=0,column=0,padx=360,pady=3)
            en122 = Entry(wrapper4,textvariable=tuser)
            en122.place(x=460,y=3)
            del_btn2 = Button(wrapper4,text="Delete",command=deleting1)
            del_btn2.place(x=460,y=30)
            Frame(wrapper4,width=2,height=500,bg='black').place(x=625,y=-10)
            heading2 = Label(wrapper4,text="SORT BY")
            heading2.place(x=675,y=3)
            sort12 = Button(wrapper4,text="ID",command=sort_by_user)
            sort12.place(x=675,y=30)

            screen.mainloop()

        elif rec in result:
            speak(f"Hello {username}")
            def update(rows):
                trv.delete(*trv.get_children())
                for i in rows:
                    trv.insert('','end',values=i)
            def clear():
                query = "SELECT * FROM GAMESS"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("CLEAR successful")
            def insertion():
                a = t1.get()
                b = t2.get()
                c = t3.get()
                d = t4.get()
                e = t5.get()
                f = t6.get()
                g = t7.get()
                h = t8.get()
                fint = int(f)
                gint = int(g)
                hint = int(h)
                query = "INSERT INTO GAMESS (game_ID,name,genre,release_year,creator,price,duration,critic_rating) VALUES ("+str(f"'{a}','{b}','{c}','{d}','{e}',{fint},{gint},{hint})")
                print(query)
                cursor.execute(query)
                connection.commit()
                clear()
                print("Record inserted correctly")
            def search():
                q2 = q.get()
                query = "SELECT game_ID, name, genre, release_year, creator, price, duration, critic_rating FROM GAMESS WHERE game_ID LIKE '%"+q2+"%' OR name LIKE '%"+q2+"%' OR genre LIKE '%"+q2+"%' OR release_year LIKE '%"+q2+"%' OR creator LIKE '%"+q2+"%' OR price LIKE '%"+q2+"%' OR duration LIKE '%"+q2+"%' OR critic_rating LIKE '%"+q2+"%'"
                cursor.execute(query)
                rows = cursor.fetchall()
                update(rows)
                print("SEARCH successful")
            def getrow(event):
                rowid = trv.identify_row(event.y)
                item = trv.item(trv.focus())
                t1.set(item['values'][0])
                t2.set(item['values'][1])
                t3.set(item['values'][2])
                t4.set(item['values'][3])
                t5.set(item['values'][4])
                t6.set(item['values'][5])
                t7.set(item['values'][6])
                t8.set(item['values'][7])
            def deleting():
                gameid = t1.get()
                if messagebox.askyesno("Confirm Delete?", "Are you sure you want to delete this user?"):
                    query = "DELETE FROM GAMESS WHERE game_ID ="+gameid
                    cursor.execute(query)
                    connection.commit()
                    clear()
                else:
                    return True
            def updatin():
                a = t1.get()
                b = t2.get()
                c = t3.get()
                d = t4.get()
                e = t5.get()
                f = t6.get()
                g = t7.get()
                h = t8.get()
                fint = int(f)
                gint = int(g)
                hint = int(h)
                if a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == "":
                    messagebox.showerror("Invalid","All fields must be filled")
                elif messagebox.askyesno("Confirm Please","Are you sure you want to update the game details?"):
                    query = f"UPDATE GAMESS SET name = '{b}', genre = '{c}',release_year = '{d}', creator = '{e}', price = {fint}, duration = {gint} , critic_rating = {hint} WHERE game_ID = '{a}'"
                    cursor.execute(query)
                    connection.commit()
                    clear()
                else:
                    return True
            def sort_by_id():
                query = f"SELECT * FROM GAMESS ORDER BY game_ID"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")

            def sort_by_name():
                query = f"SELECT * FROM GAMESS ORDER BY name"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")            

            def sort_by_genre():
                query = f"SELECT * FROM GAMESS ORDER BY genre"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")

            def sort_by_release_year():
                query = f"SELECT * FROM GAMESS ORDER BY release_year"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")

            def sort_by_creator():
                query = f"SELECT * FROM GAMESS ORDER BY creator"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")
            
            def sort_by_price():
                query = f"SELECT * FROM GAMESS ORDER BY price"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")

            def sort_by_duration():
                query = f"SELECT * FROM GAMESS ORDER BY duration"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")
            
            def sort_by_rating():
                query = f"SELECT * FROM GAMESS ORDER BY critic_rating"
                cursor.execute(query)
                rows = cursor.fetchall()
                print(rows)
                update(rows)
                print("Sort successful")


            screen = Toplevel(root)
            screen.title("APP")
            screen.geometry('1440x1280')
            screen.config(bg="white")
            speak(f"Hello {username}")
            wrapper1 = LabelFrame(screen,text="Game ID")
            wrapper2 = LabelFrame(screen,text="Game ID")
            wrapper1.pack(fill="both",expand="yes",padx=20,pady=10)
            wrapper2.pack(fill="both",expand="yes",padx=20,pady=10)

            trv = Treeview(wrapper1,columns=(1,2,3,4,5,6,7,8),show="headings",height="6")
            trv.pack()

            trv.heading(1,text="ID")
            trv.heading(2,text="Name")
            trv.heading(3,text="Genre")
            trv.heading(4,text="Release Year")
            trv.heading(5,text="Creator")
            trv.heading(6,text="Price(in Rs.)")
            trv.heading(7,text="Duration(hours)")
            trv.heading(8,text="Critic Rating(out of 100)")

            trv.bind("<Double 1>",getrow)

            query = "SELECT * FROM GAMESS"
            cursor.execute(query)
            rows = cursor.fetchall()
            update(rows)

            lab1 = Label(wrapper2,text="SEARCH:")
            lab1.place(x=10,y=20)
            serch = Entry(wrapper2,textvariable=q)
            serch.place(x=60,y=20)
            btserch = Button(wrapper2,text="SEARCH",command=search)
            btserch.place(x=195,y=18)
            btclc = Button(wrapper2,text="CLEAR",command=clear)
            btclc.place(x=260,y=18)
            Frame(wrapper2,width=2,height=500,bg='black').place(x=335,y=-10)
            lbl = Label(wrapper2, text='Game ID:')
            lbl.grid(row=0,column=0,padx=360,pady=3)
            en1 = Entry(wrapper2,textvariable=t1)
            en1.place(x=460,y=3)
            lbl2 = Label(wrapper2,text="Name:")
            lbl2.grid(row=1,column=0,padx=360,pady=3)
            en2 = Entry(wrapper2,textvariable=t2)
            en2.place(x=460,y=30)  
            lbl3 = Label(wrapper2, text='Genre:')
            lbl3.grid(row=2,column=0,padx=360,pady=3)
            en3 = Entry(wrapper2,textvariable=t3)
            en3.place(x=460,y=57)
            lbl4 = Label(wrapper2,text="Release Year:")
            lbl4.grid(row=3,column=0,padx=360,pady=3)
            en4 = Entry(wrapper2,textvariable=t4)
            en4.place(x=460,y=84)
            lbl5 = Label(wrapper2, text='Creator:')
            lbl5.grid(row=4,column=0,padx=360,pady=3)
            en5 = Entry(wrapper2,textvariable=t5)
            en5.place(x=460,y=111)
            lbl6 = Label(wrapper2,text="Price:")
            lbl6.grid(row=5,column=0,padx=360,pady=3)
            en6 = Entry(wrapper2,textvariable=t6)
            en6.place(x=460,y=138)
            lbl7 = Label(wrapper2, text='Duration:')
            lbl7.grid(row=6,column=0,padx=360,pady=3)
            en7 = Entry(wrapper2,textvariable=t7)
            en7.place(x=460,y=165)
            lbl8 = Label(wrapper2,text="Critic Rating:")
            lbl8.grid(row=7,column=0,padx=360,pady=3)
            en8 = Entry(wrapper2,textvariable=t8)
            en8.place(x=460,y=192)
            up_btn = Button(wrapper2,text="Update",command=updatin)
            up_btn.grid(row=8,column=0,padx=360,pady=3)
            add_btn = Button(wrapper2,text="Add New",command=insertion)
            add_btn.place(x=460,y=219)
            del_btn = Button(wrapper2,text="Delete",command=deleting)
            del_btn.place(x=550,y=219)
            Frame(wrapper2,width=2,height=500,bg='black').place(x=625,y=-10)
            heading = Label(wrapper2,text="SORT BY")
            heading.place(x=675,y=3)
            sort1 = Button(wrapper2,text="ID",command=sort_by_id)
            sort1.place(x=675,y=30)
            sort2 = Button(wrapper2,text="Name",command=sort_by_name)
            sort2.place(x=675,y=57)
            sort3 = Button(wrapper2,text="Genre",command=sort_by_genre)
            sort3.place(x=675,y=84)
            sort4 = Button(wrapper2,text="Release Year",command=sort_by_release_year)
            sort4.place(x=675,y=111)
            sort5 = Button(wrapper2,text="Creator",command=sort_by_creator)
            sort5.place(x=675,y=138)
            sort6 = Button(wrapper2,text="Price",command=sort_by_price)
            sort6.place(x=675,y=165)
            sort7 = Button(wrapper2,text="Duration",command=sort_by_duration)
            sort7.place(x=675,y=192)
            sort8 = Button(wrapper2,text="Critic Rating",command=sort_by_rating)
            sort8.place(x=675,y=219)
            screen.mainloop()
        else:
            messagebox.showerror("Invalid","Invalid username or password")
    except:
        pass
    
root = Tk()
root.title("Database")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)
img = PhotoImage(file='login.png')
Label(root,image=img,border=0,bg='white').place(x=50,y=90)
frame = Frame(root,width=350,height=390,bg='#fff')
frame.place(x=480,y=50)
heading = Label(frame,text='Sign in',fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)
user = Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    code.delete(0,'end')
    pass
def on_leave(e):
    if code.get()=='':
        code.insert(0,'Password')
    pass

code = Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signinn).place(x=35,y=240)
label = Label(frame,text='Don\'t have an account?',fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
label.place(x=90,y=300)

signin = Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
signin.place(x=300,y=300)
root.mainloop()
