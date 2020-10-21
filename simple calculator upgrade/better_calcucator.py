from tkinter import *
#simple calculator


# Top level widget which is the main window of an application.
root = Tk()
# adds title of the application
root.title('Simple calculator')

#widget used to enter or display single line of text
e = Entry(root,width =35,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

e.insert(0,"")
memory =[]

def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0,f_num+int(second_number))
    if math == 'subtraction':
        e.insert(0,f_num-int(second_number))
    if math == 'multiplication':
        e.insert(0,f_num*int(second_number))
    if math == 'division':
        e.insert(0,f_num/int(second_number))

def add_to_mem():
    memory.append(e.get())

def mem_view():
    e.insert(0,memory[0])

def button_add():
    first_number = e.get()
    global f_num,math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0,END)

def button_sub():
    first_number = e.get()
    global f_num,math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0,END)

def button_mul():
    first_number = e.get()
    global f_num,math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0,END)

def button_div():
    first_number = e.get()
    global f_num,math
    math = 'division'
    f_num = int(first_number)
    e.delete(0,END)

#defining buttons with digits
Button_1 = Button(root,text='1',padx=31,pady=15,command=lambda:button_click(1))
Button_2 = Button(root,text='2',padx=32,pady=15,command=lambda:button_click(2))
Button_3 = Button(root,text='3',padx=31,pady=15,command=lambda:button_click(3))

Button_4 = Button(root,text='4',padx=31,pady=15,command=lambda:button_click(4))
Button_5 = Button(root,text='5',padx=32,pady=15,command=lambda:button_click(5))
Button_6 = Button(root,text='6',padx=31,pady=15,command=lambda:button_click(6))

Button_7 = Button(root,text='7',padx=31,pady=15,command=lambda:button_click(7))
Button_8 = Button(root,text='8',padx=32,pady=15,command=lambda:button_click(8))
Button_9 = Button(root,text='9',padx=31,pady=15,command=lambda:button_click(9))

Button_0 = Button(root,text='0',padx=31,pady=15,command=lambda:button_click(0))
Button_Add = Button(root,text='+',padx=28,pady=15,command=button_add)
Button_Sub = Button(root,text='-',padx=30,pady=15,command=button_sub)
Button_Div = Button(root,text='/',padx=30,pady=15,command=button_div)
Button_Mul = Button(root,text='*',padx=30,pady=15,command=button_mul)

Button_Eq = Button(root,text='=',padx=70,pady=15,command=button_equal)
Button_Cl = Button(root,text='C',padx=70,pady=15,command=button_clear)

Button_MAdd = Button(root,text='M+',padx=24,pady=15,command=add_to_mem)
Button_MView = Button(root,text='MV',padx=24,pady=15,command=mem_view)

#put the buttons on the screen
Button_1.grid(row=3,column=0)
Button_2.grid(row=3,column=1)
Button_3.grid(row=3,column=2)

Button_4.grid(row=2,column=0)
Button_5.grid(row=2,column=1)
Button_6.grid(row=2,column=2)

Button_7.grid(row=1,column=0)
Button_8.grid(row=1,column=1)
Button_9.grid(row=1,column=2)

Button_0.grid(row=4,column=0)

Button_Add.grid(row=1,column=3)
Button_Sub.grid(row=2,column=3)
Button_Div.grid(row=3,column=3)
Button_Mul.grid(row=4,column=3)

Button_Eq.grid(row=4,column=1,columnspan=2)
Button_Cl.grid(row=5,column=0,columnspan=2)
Button_MAdd.grid(row=5,column=2)
Button_MView.grid(row=5,column=3)






#infinite loop used to run application, wait for an event to occur and process the event as long as the window is not closed
root.mainloop()
