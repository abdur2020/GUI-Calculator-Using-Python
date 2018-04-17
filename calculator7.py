from tkinter import *
import math
root=Tk()
root.geometry("450x575")
root.title("A Simple Gui Calculator Using Python")


def button_click(num):
    global operator
    operator=operator+str(num)
    var1.set(operator)
    return

def button_equal():
    global operator
    try:
        temp=str(eval(operator))
    except:
        for i in range(len(operator)):
            if operator[i]=='/' and operator[i+1]=='0':
                temp="ZeroDivisionError"
                var1.set(temp)
                operator=" "
                return
        temp="Syntax Error"
    var1.set(temp)
    operator=" "
    return

def button_backspace():
    global operator
    operator=operator[:-1]
    var1.set(operator)
    return

def button_fact():
    global operator
    p=int(eval(operator))
    f=math.factorial(p)
    operator=str(f)
    var1.set(operator)


def sin_function():
    global operator
    global sin
    sin=lambda x:round(math.sin(math.radians(x%360)),4)
    operator=operator+"sin("
    var1.set(operator)
    return


def cos_function():
    global operator
    global cos
    cos=lambda x:round(math.cos(math.radians(x%360)),4)
    operator=operator+"cos("
    var1.set(operator)
    return


def tan_function():
    global operator
    global tan
    tan=lambda x:round(math.tan(math.radians(x%360)),4)
    operator=operator+"tan("
    var1.set(operator)
    return


def log_function():
    global operator
    global log
    log=lambda x:round(math.log10(x),4)
    operator=operator+"log("
    var1.set(operator)
    return

def sqrt_function():
    global operator
    global sqrt
    sqrt=lambda x:round(math.sqrt(x),4)
    operator=operator+"sqrt("
    var1.set(operator)

def e_pow_x_function():
    global operator
    global e
    e=lambda x:round(math.exp(x),4)
    operator=operator+"e("
    var1.set(operator)
    
    
def button_clear():
    global operator
    operator=" "
    var1.set(operator)
    return 


top_frame=Frame(root,width=450,height=40,bd=4,relief='raise')
top_frame.pack(side=TOP)

below_frame=Frame(root,width=455,height=530,bd=4,relief='raise')
below_frame.pack(side=BOTTOM)


var1=StringVar()
operator=" "


display=Entry(top_frame,width=21,bd=4,font=('arial',27,'bold'),justify='right',textvariable=var1)
display.grid(row=0,column=0)



btn_sin=Button(below_frame,width=2,height=2,padx=16,pady=1,text="sin",fg="red",bd=4,font=('arial',18,'bold'),command=sin_function).grid(row=0,column=0)
btn_cos=Button(below_frame,width=2,height=2,padx=16,pady=1,text="cos",fg="red",bd=4,font=('arial',18,'bold'),command=cos_function).grid(row=0,column=1)
btn_tan=Button(below_frame,width=2,height=2,padx=16,pady=1,text="tan",fg="red",bd=4,font=('arial',18,'bold'),command=tan_function).grid(row=0,column=2)
btn_log10=Button(below_frame,width=2,height=2,padx=16,pady=1,text="log",fg="red",bd=4,font=('arial',18,'bold'),command=log_function).grid(row=0,column=3)
btn_sqrt=Button(below_frame,width=2,height=2,padx=16,pady=1,text="sqrt",fg="red",bd=4,font=('arial',18,'bold'),command=sqrt_function).grid(row=0,column=4)
btn_e_pow_x=Button(below_frame,width=2,height=2,padx=16,pady=1,text="e^x",fg="red",bd=4,font=('arial',18,'bold'),command=e_pow_x_function).grid(row=0,column=5)



bnt7=Button(below_frame,width=2,height=2,padx=16,pady=1,text="7",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click(7)).grid(row=1,column=0)
bnt8=Button(below_frame,width=2,height=2,padx=16,pady=1,text="8",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click(8)).grid(row=1,column=1)
bnt9=Button(below_frame,width=2,height=2,padx=16,pady=1,text="9",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click(9)).grid(row=1,column=2)
bnt_2_zero=Button(below_frame,width=2,height=2,padx=16,pady=1,text="00",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click("00")).grid(row=1,column=3)
bnt_add=Button(below_frame,width=2,height=2,padx=16,pady=1,text="+",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click("+")).grid(row=1,column=4)
bnt_back=Button(below_frame,width=2,height=2,padx=16,pady=1,text="<--",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_backspace()).grid(row=1,column=5)



bnt4=Button(below_frame,width=2,height=2,padx=16,pady=1,text="4",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click(4)).grid(row=2,column=0)
bnt5=Button(below_frame,width=2,height=2,padx=16,pady=1,text="5",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click(5)).grid(row=2,column=1)
bnt6=Button(below_frame,width=2,height=2,padx=16,pady=1,text="6",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click(6)).grid(row=2,column=2)
bnt_mod=Button(below_frame,width=2,height=2,padx=16,pady=1,text="%",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click("%")).grid(row=2,column=3)
bnt_sub=Button(below_frame,width=2,height=2,padx=16,pady=1,text="-",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click("-")).grid(row=2,column=4)
btn_fact=Button(below_frame,width=2,height=2,padx=16,pady=1,text="x!",fg="red",bd=4,font=('arial',18,'bold'),command=lambda :button_fact()).grid(row=2,column=5)



bnt1=Button(below_frame,width=2,height=2,padx=16,pady=1,text="1",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click(1)).grid(row=3,column=0)
bnt2=Button(below_frame,width=2,height=2,padx=16,pady=1,text="2",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click(2)).grid(row=3,column=1)
bnt3=Button(below_frame,width=2,height=2,padx=16,pady=1,text="3",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click(3)).grid(row=3,column=2)
bnt_exp=Button(below_frame,width=2,height=2,padx=16,pady=1,text="exp",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click("**")).grid(row=3,column=3)
bnt_mult=Button(below_frame,width=2,height=2,padx=16,pady=1,text="*",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click("*")).grid(row=3,column=4)
bnt_square=Button(below_frame,width=2,height=2,padx=16,pady=1,text="^2",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click("**2")).grid(row=3,column=5)


bnt0=Button(below_frame,width=2,height=2,padx=16,pady=1,text="0",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click(0)).grid(row=4,column=0)
bnt_point=Button(below_frame,width=2,height=2,padx=16,pady=1,text=".",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click(".")).grid(row=4,column=1)
bnt_equal=Button(below_frame,width=2,height=2,padx=16,pady=1,text="=",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_equal()).grid(row=4,column=2)
bnt_clear=Button(below_frame,width=2,height=2,padx=16,pady=1,text="AC",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_clear()).grid(row=4,column=3)
bnt_div=Button(below_frame,width=2,height=2,padx=16,pady=1,text="/",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click("/")).grid(row=4,column=4)
bnt_pi=Button(below_frame,width=2,height=2,padx=16,pady=1,text="pi",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click(3.14)).grid(row=4,column=5)


bnt_left_p=Button(below_frame,width=2,height=2,padx=16,pady=1,text="(",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click("(")).grid(row=5,column=0)
bnt_right_p=Button(below_frame,width=2,height=2,padx=16,pady=1,text=")",fg='red',bd=4,font=('arial',18,'bold'),command=lambda :button_click(")")).grid(row=5,column=1)

root.mainloop()
