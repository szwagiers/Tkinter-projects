from tkinter import *
import math
from tkinter import messagebox

#simple calculator


# Top level widget which is the main window of an application.
root = Tk()
# adds title of the application and icon
root.title('Better calculator')
root.iconbitmap('D:/ikony/calc.ico')

#widget used to enter or display single line of text
e = Entry(root,width =35,borderwidth=5)
e.grid(row=0,column=0,columnspan=6,padx=10,pady=10)

e.insert(0,"")


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
    if math == 'addition' and isinstance(f_num, float):
        e.insert(0,f_num+float(second_number))
    else:
        e.insert(0,f_num+int(second_number))
    if math == 'subtraction':
        e.insert(0,f_num-int(second_number))
    if math == 'multiplication':
        e.insert(0,f_num*int(second_number))
    if math == 'division':
        e.insert(0,f_num/int(second_number))

index = 0
#adding values or result to memory
def add_to_mem():
    global index
    index += 1
    if index <= 4:
        memory.append(e.get())
        #important note : insert widget accepts only strings
        # insert saved result in the textbox with index number
        list.insert(INSERT,str(index)+')'+ e.get() + '\n')
        e.delete(0,END)
    #if there are 4 positions in memory popup warning message
    else:
        messagebox.showinfo("WARNING", "Out of memory")

#put result from memory in your calculator window by chosing index number and clicking MV button
def mem_view():
    position = int(e.get())
    e.delete(0,END)
    if position == 1:
        if isinstance(memory[position-1],float):
            e.insert(0,float(memory[position-1]))
        else:
            e.insert(0,memory[position-1])
    if position == 2:
        if isinstance(memory[position-1],float):
            e.insert(0,float(memory[position-1]))
        else:
            e.insert(0,memory[position-1])
    if position == 3:
        if isinstance(memory[position-1],float):
            e.insert(0,float(memory[position-1]))
        else:
            e.insert(0,memory[position-1])
    if position == 4:
        if isinstance(memory[position-1],float):
            e.insert(0,float(memory[position-1]))
        else:
            e.insert(0,memory[position-1])

def int_or_flo(number):
    if '.' in number:
        num = float(number)
    else:
        num = int(number)
    return num

def button_add():
    first_number = e.get()
    global f_num,math
    math = 'addition'
    f_num = int_or_flo(first_number)
    e.delete(0,END)

def button_sub():
    first_number = e.get()
    global f_num,math
    math = 'subtraction'
    f_num = int_or_flo(first_number)
    e.delete(0,END)

def button_mul():
    first_number = e.get()
    global f_num,math
    math = 'multiplication'
    f_num = int_or_flo(first_number)
    e.delete(0,END)

def button_div():
    first_number = e.get()
    global f_num,math
    math = 'division'
    f_num = int_or_flo(first_number)
    e.delete(0,END)

#squareroot of number
def button_sqrt():
    first_number = e.get()
    f_num = int_or_flo(first_number)
    #important to clear Entry. Without it, calculator will return sqrt(4) = 2,04.
    e.delete(0,END)
    e.insert(0,math.sqrt(f_num))


#defining buttons with digits

Button_1 = Button(root,text='1',padx=31,pady=16,command=lambda:button_click(1))
Button_2 = Button(root,text='2',padx=32,pady=16,command=lambda:button_click(2))
Button_3 = Button(root,text='3',padx=31,pady=16,command=lambda:button_click(3))

Button_4 = Button(root,text='4',padx=31,pady=16,command=lambda:button_click(4))
Button_5 = Button(root,text='5',padx=32,pady=16,command=lambda:button_click(5))
Button_6 = Button(root,text='6',padx=31,pady=16,command=lambda:button_click(6))

Button_7 = Button(root,text='7',padx=31,pady=16,command=lambda:button_click(7))
Button_8 = Button(root,text='8',padx=32,pady=16,command=lambda:button_click(8))
Button_9 = Button(root,text='9',padx=31,pady=16,command=lambda:button_click(9))

Button_0 = Button(root,text='0',padx=31,pady=16,command=lambda:button_click(0))
Button_Add = Button(root,text='+',padx=28,pady=16,command=button_add)
Button_Sub = Button(root,text='-',padx=30,pady=16,command=button_sub)
Button_Div = Button(root,text='/',padx=30,pady=16,command=button_div)
Button_Mul = Button(root,text='*',padx=30,pady=16,command=button_mul)
Button_Sqrt = Button(root, text='\u221A',padx=29,pady=15,command=button_sqrt)

Button_Eq = Button(root,text='=',padx=69,pady=16,command=button_equal)
Button_Cl = Button(root,text='C',padx=30,pady=15,command=button_clear)

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

Button_Div.grid(row=1,column=3)
Button_Mul.grid(row=2,column=3)
Button_Sub.grid(row=3,column=3)
Button_Add.grid(row=4,column=3)

#mathematical operations
Button_Eq.grid(row=4,column=1,columnspan=2)
Button_Cl.grid(row=5,column=0)
Button_Sqrt.grid(row=5,column=3)
Button_MAdd.grid(row=5,column=2)
Button_MView.grid(row=5,column=1)

#frame where memory content will be shown
memory_frame = LabelFrame(root, text ='Memory', padx =10 , pady=12)
memory_frame.grid(row=1,column=5,rowspan=2)

# list where results are stored
memory =[]
list = Text(memory_frame,height=4,width=20)
list.grid(row=2,column=5)



#infinite loop used to run application, wait for an event to occur and process the event as long as the window is not closed
root.mainloop()
