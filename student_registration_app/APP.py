import tkinter as tk
import mysql.connector
import datetime as dt
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import pathlib



def check(*args):
    a = name.get()
    b = dob.get()
    c = tele.get()
    d = radio_conv()
    e = occupation.get()
    f = guardian.get()
    g = religion.get()
    h = combo.get()
    i = address_textbox.get('1.0', 'end')
    j = age.get()
    if a and b and c and d and e and f and g and h and i and j:
        save_button.config(state='normal')
    else:
        save_button.config(state='disabled')


def radio_conv():
    if radio.get() == 1:
        return 'Male'
    else:
        return 'Female'



# INSERTING ALL ENTRIES INTO DATABASE
def save():
    
    my_cursor = db.cursor()
    my_cursor.execute(f'''
        INSERT INTO students (
            FULL_NAME, 
            DOB,
            GENDER,
            CLASS ,
            RELIGION,
            AGE)
        
        
        VALUES(
        '{name.get()}', '{dob.get()}',
        '{radio_conv()}','{combo.get()}','{religion.get()}',
        '{ age.get()}')
    
    ''')
    db.commit()
    messagebox.showinfo('MESSAGE','SUCCESSFULLY SAVED')



#VARIABLES
background = '#06283D'
framefg = background
framebg = '#ededed'

# INITIALIZING WINDOW
root = tk.Tk()
root.title('Student Registration System')
root.geometry('1250x700+70+20')
root.config(bg=background)
root.resizable(width=False, height=False)
root.iconbitmap('./icons/Database.ico')


# GENDER
def selection():
    value = radio.get()
    if value == 1:
        gender = 'Male'
    else:
        gender = 'Female'
     


# EXIT
def exit():
    root.destroy()


#UPLOAD
def upload():
    global file_name
    global pic
    file_name = filedialog.askopenfile(initialdir=os.getcwd(),
                                       title='Select image',
                                       filetypes=(('jpg_file', '.jpg'),
                                                  ('png_file', '.png'),
                                                  ('text_file', '.txt')))
    pic = (Image.open(file_name.name))
    resized_pic = pic.resize((190, 190))
    photo2 = ImageTk.PhotoImage(resized_pic)
    profile.config(image=photo2)
    profile.image_names((photo2))


# RESET
def reset():
    name.set('')
    dob.set('')
    religion.set('')
    age.set('')
    guardian.set('')
    occupation.set('')
    tele.set('')
    address_textbox.setvar('')
    combobox.set('')
    radio.set(None)
    address_textbox.delete('1.0', 'end')
    profile.config(image=img)
    profile.image_names((img))


#TOP FRAMES
label_1 = tk.Label(root,
                   text='Email: ioenimil@gmail.com',
                   height=3,
                   background='#f0687c',
                   anchor='e')
label_1.pack(fill='x', )

label_2 = tk.Label(root,
                   text='STUDENT REGISTRATION',
                   height=2,
                   background='#C36464',
                   foreground='#fff',
                   font=('arial', 19, 'bold'))
label_2.pack(fill='x', )

#SEARCH BOX TO UPDATE
search = tk.StringVar()
a = tk.Entry(root, 
    textvariable=search, 
    width=15,
    bd=2, 
    font=('arial',20,))

a.place(x=820, y=70)

imageicon3 = tk.PhotoImage(file='./icons/search.png')
search_but = tk.Button(root,
                       text='Search',
                       compound='left',
                       image=imageicon3,
                       width=123,
                       height=30,
                       background='blue',
                       font='arial 18 bold')
search_but.place(x=1060, y=70)

#REGISTRATION AND DATE
label_3 = tk.Label(root,
                   text='Registration Number: ',
                   font='arial 13',
                   fg=framebg,
                   background=background)
label_3.place(x=30, y=150)

label_4 = tk.Label(root,
                   text='Date: ',
                   font='arial 13',
                   fg=framebg,
                   background=background)
label_4.place(x=500, y=150)

registration = tk.StringVar()
date = tk.StringVar()

reg_entry = tk.Entry(root,
                     textvariable=registration,
                     width=15,
                     font='arial 10')
reg_entry.place(x=200, y=152)

# REGISTRATION DATE

today = dt.date.today()
d1 = today.strftime('%d/%m/%Y')
date_entry = tk.Entry(root,
                      textvariable=date,
                      state='readonly',
                      width=15,
                      font='arial 10')
date_entry.place(x=550, y=152)

date.set(f'    {d1}')


# STUDENT DETAILS
obj = tk.LabelFrame(root,
                    text="Student's Details",
                    font=20,
                    bd=2,
                    width=900,
                    bg=framebg,
                    fg=framefg,
                    height=250,
                    relief='groove')
obj.place(x=30, y=200)

tk.Label(obj, text='Full Name: ', font='arial 13', bg=framebg,
         fg=framefg).place(x=30, y=50)
tk.Label(obj, text='Date of Birth: ', font='arial 13', bg=framebg,
         fg=framefg).place(x=30, y=100)
tk.Label(obj, text='Gender: ', font='arial 13', bg=framebg,
         fg=framefg).place(x=30, y=150)

tk.Label(obj, text='Class: ', font='arial 13', bg=framebg,
         fg=framefg).place(x=500, y=50)
tk.Label(obj, text='Religion: ', font='arial 13', bg=framebg,
         fg=framefg).place(x=500, y=100)
tk.Label(obj, text='Age: ', font='arial 13', bg=framebg,
         fg=framefg).place(x=500, y=150)

name = tk.StringVar()
name_entry = tk.Entry(obj, textvariable=name, width=20, font='arial 10')
name_entry.place(x=160, y=50)
name.trace('w', check)

dob = tk.StringVar()
dob_entry = tk.Entry(obj, textvariable=dob, width=20, font='arial 10')
dob_entry.place(x=160, y=100)
dob.trace('w',check)

radio = tk.IntVar()
r1 = tk.Radiobutton(obj,
                    text='Male',
                    variable=radio,
                    value='1',
                    bg=framebg,
                    fg=framefg,
                    command=selection)
r1.place(x=150, y=150)

r2 = tk.Radiobutton(obj,
                    text='Female',
                    variable=radio,
                    value='0',
                    bg=framebg,
                    fg=framefg,
                    command=selection)
r2.place(x=200, y=150)
radio.trace('w', check)

religion = tk.StringVar()
religion_entry = tk.Entry(obj,
                          textvariable=religion,
                          width=20,
                          font='arial 10')
religion_entry.place(x=630, y=100)
religion.trace('w', check)

age = tk.StringVar()
age_entry = tk.Entry(obj, textvariable=age, width=20, font='arial 10')
age_entry.place(x=630, y=150)
age.trace('w', check)


combo = tk.StringVar()
combobox = Combobox(obj,
                    values=(
                        'N1', 'N2', 'KG1', 'KG2', 'B1',
                         'B2', 'B3', 'B4', 'B5',
                        'B6', 'B7', 'B8', 'B9'
                    ),
                    font='Roboto 10',
                    width=17,
                    state='r',
                    textvariable=combo)
combobox.place(x=630, y=50)
combobox.set('')
combo.trace('w', check)

# PARENTS DETAILS
obj2 = tk.LabelFrame(root,
                     text="Parent's Details",
                     font=20,
                     bd=2,
                     width=900,
                     bg=framebg,
                     fg=framefg,
                     height=220,
                     relief='groove')
obj2.place(x=30, y=470)

tk.Label(obj2,
         text="Guardian's Name: ",
         font='arial 13',
         bg=framebg,
         fg=framefg).place(x=30, y=50)
tk.Label(obj2, text="Occupation: ", font='arial 13', bg=framebg,
         fg=framefg).place(x=30, y=100)

tk.Label(obj2, text='Phone Number: ', font='arial 13', bg=framebg,
         fg=framefg).place(x=500, y=50)
tk.Label(obj2, text='Address: ', font='arial 13', bg=framebg,
         fg=framefg).place(x=500, y=100)

guardian = tk.StringVar()
guardian_entry = tk.Entry(obj2,
                          textvariable=guardian,
                          width=20,
                          font='arial 10')
guardian_entry.place(x=160, y=51)
guardian.trace('w', check)

occupation = tk.StringVar()
occupation_entry = tk.Entry(obj2,
                            textvariable=occupation,
                            width=20,
                            font='arial 10')
occupation_entry.place(x=160, y=100)
occupation.trace('w', check)

tele = tk.StringVar()
tele_entry = tk.Entry(obj2, textvariable=tele, width=20, font='arial 10')
tele_entry.place(x=630, y=50)
tele.trace('w', check)

address_textbox = tk.Text(obj2, width=20, height=4, font='arial 10')
address_textbox.place(x=630, y=100)


# IMAGE
img_frame = tk.Frame(root,
                     bd=3,
                     bg='black',
                     width=200,
                     height=200,
                     relief='groove')
img_frame.place(x=1000, y=150)
img = tk.PhotoImage(file='C:/Users/USER/Desktop/DATABASE/icons/face.png')
profile = tk.Label(img_frame, image=img)
profile.place(x=0, y=0)

# BUTTONS
tk.Button(root,
          text='UPLOAD',
          font='montserrat 15 bold',
          width=19,
          height=2,
          bg='lightblue',
          command=upload).place(x=1000, y=370)
save_button = tk.Button(root,
          text='SAVE',
          font='montserrat 15 bold',
          width=19,
          command=save,
          state='disable',
          height=2,
          bg='lightblue')
save_button.place(x=1000, y=450)

tk.Button(root,
          text='RESET',
          font='montserrat 15 bold',
          width=19,
          height=2,
          bg='lightblue',
          command=reset).place(x=1000, y=530)
tk.Button(root,
          text='EXIT',
          font='montserrat 15 bold',
          width=19,
          height=2,
          bg='lightblue',
          command=exit).place(x=1000, y=610)

# BACKEND

db = mysql.connector.connect(host='127.0.0.1',
                             user='root',
                             password='ioenimil',)

first_cursor = db.cursor()
first_cursor.execute('CREATE DATABASE IF NOT EXISTS SANKOFA;')

db = mysql.connector.connect(host='127.0.0.1',
                             user='root',
                             password='ioenimil',
                             database='SANKOFA')

def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

if checkTableExists(db, 'Students'):
    my_cursor = db.cursor()

    my_cursor.execute('''

        CREATE TABLE Students (
            ID INT(11) PRIMARY KEY AUTO_INCREMENT,
            FULL_NAME VARCHAR(50), 
            DOB VARCHAR(50),
            GENDER VARCHAR(50),
            CLASS VARCHAR(50),
            RELIGION VARCHAR(50),
            AGE SMALLINT UNSIGNED
            )
    ''')

root.mainloop()