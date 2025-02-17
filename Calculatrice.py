from tkinter import *
from tkinter import ttk

######################################################################
#   DESIGN ###########################################################
######################################################################

#window=Tk()
window=Tk()
window.title('Calculator')
window.geometry("300x400+50+50")
window.iconbitmap("C:\\Users\\hp\\Downloads\\calculator_N7X_icon.ico")
window.resizable(0,0)
win_bg='#3D3E82'
window.config(bg=win_bg)

font_but=('Times New Roman',12,'bold')
width_but=4

######### Entry ####################################################
var=StringVar()
main_entry=Entry(window,width=17,font=('Times New Roman',20),state='readonly',textvariable=var,relief='flat')
main_entry.place(x=30,y=30)

######### Numbers BUTTONS ########
#RANGE 1_______________________________________
but_7=Button(window,width=width_but,font=font_but,text='7',command=lambda : Show(7))
but_7.place(x=30,y=140)

but_8=Button(window,width=width_but,font=font_but,text='8',command=lambda :Show(8))
but_8.place(x=90,y=140)

but_9=Button(window,width=width_but,font=font_but,text='9',command=lambda :Show(9))
but_9.place(x=150,y=140)
#RANGE 2______________________________________________
but_4=Button(window,width=width_but,font=font_but,text='4',command=lambda :Show(4))
but_4.place(x=30,y=190)

but_5=Button(window,width=width_but,font=font_but,text='5',command=lambda :Show(5))
but_5.place(x=90,y=190)

but_6=Button(window,width=width_but,font=font_but,text='6',command=lambda :Show(6))
but_6.place(x=150,y=190)

#RANGE 3 ________________________________________________
but_1=Button(window,width=width_but,font=font_but,text='1',command=lambda :Show(1))
but_1.place(x=30,y=240)

but_2=Button(window,width=width_but,font=font_but,text='2',command=lambda :Show(2))
but_2.place(x=90,y=240)

but_3=Button(window,width=width_but,font=font_but,text='3',command=lambda :Show(3))
but_3.place(x=150,y=240)

#RANGE 4_____________________________________
but_0=Button(window,width=11,font=font_but,text='0',command=lambda :Show(0))
but_0.place(x=30,y=290)

but_point=Button(window,width=4,font=font_but,text='.',command=lambda :Show('.'))
but_point.place(x=150,y=290)

list_but=[but_0,but_7,but_6,but_5,but_4,but_3,but_2,but_1,but_8,but_9,but_point]
for bt in list_but:
    bt.config(bg='#19314D',fg='white',bd=1,relief='flat')


#################### OPERATION BUTTONS #####################################
# Range 5 ````````````````````````````````````````````````````
but_equal=Button(window,width=17,font=font_but,text='=',command=lambda :Equal(),bg='orange',relief='flat')
but_equal.place(x=30,y=340)

#Range_Vertical #################################"
but_plus=Button(window,width=width_but,font=font_but,text='+',command=lambda :Show('+'))
but_plus.place(x=210,y=140)

but_moin=Button(window,width=width_but,font=font_but,text='-',command=lambda :Show('-'))
but_moin.place(x=210,y=190)

but_divis=Button(window,width=width_but,font=font_but,text='/',command=lambda :Show('/'))
but_divis.place(x=210,y=240)

but_multip=Button(window,width=width_but,font=font_but,text='*',command=lambda :Show('*'))
but_multip.place(x=210,y=290)

but_clear=Button(window,width=width_but,font=font_but,text='C',command=lambda :Clear())
but_clear.place(x=210,y=340)

list_op=[but_clear,but_divis,but_multip,but_moin,but_plus]
for bt in list_op :
    bt.config(bg='powder blue',relief='flat')
################################################################
# Program ######################################################
################################################################
expression=""
def Show(x):
    global expression
    expression=expression+str(x)
    var.set(expression)
def Equal():
    try :
        global expression
        final=eval(expression)
        var.set(final)
        expression=str(final)
    except Exception as exc:
        var.set(exc)
def Clear():
    global expression
    expression = ""
    var.set("")

window.mainloop()
