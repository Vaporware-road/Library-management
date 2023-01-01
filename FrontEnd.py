# witten by Abyys
# python 3.11.1
# 1 feb 2023
# broject -> Desember.001

# the GUI part of libreary proj
# in this codpage will do the gui part 
 
# ================== Start ===================

# This program has four features: the name of the book,
#  the name of the author,
#  the year of publication and its access code
# And it also has a list on the left side of the lower part,
#  and on the right side there are buttons to see all,
#  search, add, update, delete, and close the program.

# start 

from tkinter import *

window = Tk()

window.title("Library manager")

# ================== Lable ===================

lb1 = Label(window,text="Title")
lb1.grid(row=0,column=0)

lb2 = Label(window,text="Author")
lb2.grid(row=0,column=3)

lb3 = Label(window,text="Year")
lb3.grid(row=1,column=0)

lb4 = Label(window,text="ISBN")
lb4.grid(row=1,column=3)

# ================== Entrys ===================

titleText = StringVar()
ent1 = Entry(window,textvariable=titleText)
ent1.grid(row=0,column=1)

authorText = StringVar()
ent2 = Entry(window,textvariable=authorText)
ent2.grid(row=0,column=4)

yearText = StringVar()
ent3 = Entry(window,textvariable=yearText)
ent3.grid(row=1,column=1)

isbnText = StringVar()
ent4 = Entry(window,textvariable=isbnText)
ent4.grid(row=1,column=4)

# ================== ListBox & Scroll ===================

list1 = Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,columnspan=2,rowspan=6)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
 
# now we make a conection between lsistbox and scrollbar

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
# ================== Buttom ===================

b1 = Button(window,text="View All",width=12)
b1.grid(row=2,column=4)

b2 = Button(window,text="Search Entry",width=12)
b2.grid(row=3,column=4)

b3 = Button(window,text="Add Entry",width=12)
b3.grid(row=4,column=4)

b4 = Button(window,text="Update Selected",width=12)
b4.grid(row=5,column=4)

b5 = Button(window,text="Delete Selected",width=12)
b5.grid(row=6,column=4)

b6 = Button(window,text="Close",width=12)
b6.grid(row=7,column=4)


# ================== End ===================


window.mainloop()

# end