#simple calculator app using Tkinter and by using classes
from tkinter import *
from tkinter import ttk
import math

#I am basically doing it to upload to my github


#initializing window
root=Tk()
root.geometry("600x600")
root.title("AMAL CALCULATOR")
root.resizable(0,0)



#creating frames for items
main_frame=Frame(root,height=600,width=600,bg='#c3c4c7')
main_frame.pack()
menu_frame=Frame(root,height=100,width=600,bg='#ed7d31')
menu_frame.place(x=0,y=550)


#loading pictures

#light mode
light_pressed=0
def onpress(e):
    global light_pressed
    if light_pressed==0:
        dark_bttn.config(image=dark_img2)
        light_pressed=1
        menu_frame.config(bg='#818181')
        main_frame.config(bg="black")
        b1.config(bg='#818181',fg="white")
        b2.config(bg='#818181',fg="white")
        b3.config(bg='#818181',fg="white")
        b4.config(bg='#818181',fg="white")
        b5.config(bg='#818181',fg="white")
        b6.config(bg='#818181',fg="white")
        b7.config(bg='#818181',fg="white")
        b8.config(bg='#818181',fg="white")
        b9.config(bg='#818181',fg="white")
        neg.config(bg='#818181',fg="white")
        deci.config(bg='#818181',fg="white")
        zer.config(bg='#818181',fg="white")
        
        bks.config(bg='#824308',fg="white")
        ac.config(bg='#824308',fg="white")
        br.config(bg='#824308',fg="white")
        per.config(bg='#824308',fg="white")
        add.config(bg='#824308',fg="white")
        sub.config(bg='#824308',fg="white")
        div.config(bg='#824308',fg="white")
        eql.config(bg='#824308',fg="white")
        logb.config(bg='#824308',fg="white")
        power.config(bg='#824308',fg="white")
        fact.config(bg='#824308',fg="white")
        sqrtb.config(bg='#824308',fg="white")
        recall.config(bg='#824308',fg="white")
        mul.config(bg='#824308',fg="white")
        expo.config(bg='#824308',fg="white")
        ln.config(bg='#824308',fg="white")
        pi.config(bg='#824308',fg="white")

    else:
        dark_bttn.config(image=dark_img)
        light_pressed=0
        menu_frame.config(bg='#ed7d31')
        main_frame.config(bg='#c3c4c7')
        b1.config(bg='white',fg='black')
        b2.config(bg='white',fg='black')
        b3.config(bg='white',fg='black')
        b4.config(bg='white',fg='black')
        b5.config(bg='white',fg='black')
        b6.config(bg='white',fg='black')
        b7.config(bg='white',fg='black')
        b8.config(bg='white',fg='black')
        b9.config(bg='white',fg='black')
        neg.config(bg='white',fg="black")
        deci.config(bg='white',fg="black")
        zer.config(bg='white',fg="black")

        bks.config(bg='#ed7d31')
        ac.config(bg='#ed7d31')
        br.config(bg='#ed7d31')
        per.config(bg='#ed7d31')
        add.config(bg='#ed7d31')
        sub.config(bg='#ed7d31')
        div.config(bg='#ed7d31')
        eql.config(bg='#ed7d31')
        logb.config(bg='#ed7d31')
        power.config(bg='#ed7d31')
        fact.config(bg='#ed7d31')
        sqrtb.config(bg='#ed7d31')
        recall.config(bg='#ed7d31')
        mul.config(bg='#ed7d31')
        pi.config(bg='#ed7d31')
        ln.config(bg='#ed7d31')
        expo.config(bg='#ed7d31')


def num_press(e):
    display.config(state="normal")
    display.insert(END,e)
    display.config(state="readonly")

def bttn_press(e):
    display.config(state="normal")
    curr=display.get()
    display.delete(0,END)
    display.insert(END,curr+str(e))
    display.config(state="readonly")

def special_press(e):
    if e=='C':
        display.config(state="normal")
        display.delete(0,END)
        display.config(state="readonly")
    if e=='neg':
        curr=display.get()
        new='-('+curr+')'
        display.config(state="normal")
        display.delete(0,END)
        display.insert(END,new)
        display.config(state="readonly")
    if e=='bracket':
        curr=display.get()
        display.config(state="normal")
        if curr=='' or ((curr[-1]) not in ['0','1','2','3','4','5','6','7','8','9']):
            display.insert(END,"(")
        else:
            display.insert(END,")")
        display.config(state="readonly")
    if e=='bks':
        curr=display.get()
        display.config(state="normal")
        if "SYNTAX ERROR" in curr:
            display.delete(0,END)
        else:
            display.delete(0,END)
            new=curr[0:len(curr)-1]
            display.insert(END,new)
        display.config(state="readonly")
    if e=='find':
        curr=display.get()
        display.config(state="normal")
        display.delete(0,END)
        try:
            new=eval(curr)
            display.insert(END,new)
        except:
            display.insert(END,"SYNTAX ERROR")
        
        display.config(state="readonly")

def math_press(e):
    if e=="sqrt":
        display.config(state="normal")
        try:
            curr=display.get()
            new=math.sqrt(int(curr))
            display.delete(0,END)
            display.insert(END,new)
        except:
            display.insert(END,"SYNTAX ERROR")
        display.config(state="readonly")
    if e=='expo':
        display.config(state="normal")
        display.insert(END,math.e)
        display.config(state="readonly")
    if e=='pi':
        display.config(state="normal")
        display.insert(END,math.pi)
        display.config(state="readonly")
    if e=='log':
        display.config(state="normal")
        try:
            curr=display.get()
            new=math.log10(int(curr))
            display.delete(0,END)
            display.insert(END,new)
        except:
            display.insert(END,"SYNTAX ERROR")
        display.config(state="readonly")
    if e=='ln':
        display.config(state="normal")
        try:
            curr=display.get()
            new=math.log(int(curr))
            display.delete(0,END)
            display.insert(END,new)
        except:
            display.insert(END,"SYNTAX ERROR")
        display.config(state="readonly")
    if e=='fact':
        display.config(state="normal")
        try:
            curr=display.get()
            new=math.factorial(int(curr))
            display.delete(0,END)
            display.insert(END,new)
        except:
            display.insert(END,"SYNTAX ERROR")
        display.config(state="readonly")



        

dark_img=PhotoImage(file="assets/buttons/light/dark.png")
dark_img2=PhotoImage(file="assets/buttons/dark/light.png")




#loading images into menu_frame
dark_bttn=Label(menu_frame,image=dark_img,borderwidth=0,height=45)
dark_bttn.bind("<Button-1>",onpress)
dark_bttn.place(x=300,y=0)


#loading items on main frame
display=Entry(main_frame,width=28,borderwidth=2,font=("Helvatica 26"),state="readonly")
display.place(x=30,y=10,height=100)

ac=Button(main_frame,height=3,width=9,fg='white',text="CLEAR",bg='#ed7d31',command=lambda:special_press("C"))
ac.place(x=20,y=150)
br=Button(main_frame,height=3,width=9,text="( )",font="Helvatica 9",bg='#ed7d31',fg='white',command=lambda:special_press("bracket"))
br.place(x=120,y=150)
per=Button(main_frame,height=3,width=9,text="%",font="Helvatica 9",bg='#ed7d31',fg='white')
per.place(x=220,y=150)
mul=Button(main_frame,height=3,width=9,text="x",font="Helvatica 9",bg='#ed7d31',fg='white',command=lambda: bttn_press("*"))
mul.place(x=320,y=150)

bks=Button(main_frame,height=3,width=9,text="DELETE",font="Helvatica 9",bg='#ed7d31',fg='white',command=lambda:special_press('bks'))
bks.place(x=520,y=150)

expo=Button(main_frame,height=3,width=9,text="e",font="Helvatica 9",bg='#ed7d31',fg='white',command=lambda:math_press("expo"))
expo.place(x=520,y=220)

ln=Button(main_frame,height=3,width=9,text="Ln",font="Helvatica 9",bg='#ed7d31',fg='white',command=lambda:math_press('ln'))
ln.place(x=520,y=290)

pi=Button(main_frame,height=3,width=9,text="π",font="Helvatica 9",bg='#ed7d31',fg='white',command=lambda:math_press('pi'))
pi.place(x=520,y=360)


b7=Button(main_frame,height=3,width=9,text="7",font="Helvatica 9",command=lambda: num_press(7))
b7.place(x=20,y=220)
b8=Button(main_frame,height=3,width=9,text="8",font="Helvatica 9",command=lambda: num_press(8))
b8.place(x=120,y=220)
b9=Button(main_frame,height=3,width=9,text="9",font="Helvatica 9",command=lambda: num_press(9))
b9.place(x=220,y=220)
add=Button(main_frame,height=3,width=9,text="+",font="Helvatica 9",bg='#ed7d31',fg='white',command=lambda: bttn_press("+"))
add.place(x=320,y=220)



b4=Button(main_frame,height=3,width=9,text="4",font="Helvatica 9",command=lambda: num_press(4))
b4.place(x=20,y=290)
b5=Button(main_frame,height=3,width=9,text="5",font="Helvatica 9",command=lambda: num_press(5))
b5.place(x=120,y=290)
b6=Button(main_frame,height=3,width=9,text="6",font="Helvatica 9",command=lambda: num_press(6))
b6.place(x=220,y=290)
sub=Button(main_frame,height=3,width=9,text="-",font="Helvatica 9",bg='#ed7d31',fg='white',command=lambda: bttn_press("-"))
sub.place(x=320,y=290)

b1=Button(main_frame,height=3,width=9,text="1",font="Helvatica 9",command=lambda: num_press(1))
b1.place(x=20,y=360)
b2=Button(main_frame,height=3,width=9,text="2",font="Helvatica 9",command=lambda: num_press(2))
b2.place(x=120,y=360)
b3=Button(main_frame,height=3,width=9,text="3",font="Helvatica 9",command=lambda: num_press(3))
b3.place(x=220,y=360)
div=Button(main_frame,height=3,width=9,text="/",font="Helvatica 9",bg='#ed7d31',fg='white',command=lambda: bttn_press("/"))
div.place(x=320,y=360)

neg=Button(main_frame,height=3,width=9,text="+/-",font="Helvatica 9",command=lambda:special_press("neg"))
neg.place(x=20,y=430)
zer=Button(main_frame,height=3,width=9,text="0",font="Helvatica 9",command=lambda: num_press(0))
zer.place(x=120,y=430)
deci=Button(main_frame,height=3,width=9,text=".",font="Helvatica 9",command=lambda: bttn_press("."))
deci.place(x=220,y=430)
eql=Button(main_frame,height=3,width=9,text="=",font="Helvatica 9",bg='#ed7d31',fg='white',command=lambda:special_press("find"))
eql.place(x=320,y=430)

logb=Button(main_frame,height=3,width=9,text="log",font="Helvatica 9",bg='#ed7d31',fg='white',command=lambda:math_press('log'))
logb.place(x=420,y=150)
power=Button(main_frame,height=3,width=9,text="x^y",font="Helvatica 9",bg='#ed7d31',fg='white')
power.place(x=420,y=220)
fact=Button(main_frame,height=3,width=9,text="Fact",font="Helvatica 9",bg='#ed7d31',fg='white',command=lambda:math_press("fact"))
fact.place(x=420,y=290)
sqrtb=Button(main_frame,height=3,width=9,text="√",font="Helvatica 9",bg='#ed7d31',fg='white',command=lambda:math_press("sqrt"))
sqrtb.place(x=420,y=360)
recall=Button(main_frame,height=3,width=9,text="Recall",font="Helvatica 9",bg='#ed7d31',fg='white')
recall.place(x=420,y=430)
















root.mainloop()