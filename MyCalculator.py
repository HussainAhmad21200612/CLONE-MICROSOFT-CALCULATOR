from tkinter import *
cal=Tk()
cal.title("CALCULATOR")
cal.iconbitmap("cal.ico") #icon of the tkinter
cal.minsize(405,320)
cal.maxsize(520,320) #maximum size of the tkinter window
v1=StringVar()
v=StringVar()
v.set("")
v1.set("CALCULATOR.......")
#label for dispaly and calculatio n
Label(cal,font=('courier',15),textvariable=v1,width=43,height=2,anchor=NE,bg='black',fg='white').grid(row=0 ,column=0,columnspan=5)
Label(cal,font=('courier',15),textvariable=v,width=43,height=2,anchor=NE,bg='grey',fg='black').grid(row=1 ,column=0,columnspan=5)
l=['+','-','/','*','^','%','1/x']
#change of operators
def change(s):
    if(s=="^/%"):
        Button(cal,font=('courier',10),text='^',width=15,height=2,command=lambda:click('^')).grid(row=51,column=4)
        Button(cal,font=('courier',10),text='%',width=15,height=2,command=lambda:click('%')).grid(row=52,column=4)       
        Button(cal,font=('courier',10),text='1/x',width=15,height=2,command=lambda:click('1/x')).grid(row=53,column=4)       
        Button(cal,font=('courier',10),text='π',width=15,height=2,command=lambda:click('π')).grid(row=54,column=4)
        Button(cal,font=('courier',10),text='*/+',width=15,height=2,bg='cyan',fg='black',command=lambda:change('*/+')).grid(row=50,column=2)
    elif s=="*/+":
        Button(cal,font=('courier',10),text='^/%',width=15,height=2,bg='cyan',fg='black',command=lambda:change('^/%')).grid(row=50,column=2)       
        Button(cal,font=('courier',10),text='/',width=15,height=2,command=lambda:click('/')).grid(row=54,column=4)
        Button(cal,font=('courier',10),text='+',width=15,height=2,command=lambda:click('+')).grid(row=51,column=4)
        Button(cal,font=('courier',10),text='-',width=15,height=2,command=lambda:click('-')).grid(row=52,column=4)
        Button(cal,font=('courier',10),text='*',width=15,height=2,command=lambda:click('*')).grid(row=53,column=4)
#defining clicks of the button
def click(s):
    if s=='ce':
        v.set("")
        v1.set("")
    elif s=='π':
        
            v.set("3.14159")
            
    elif s=='C':
                v.set("")
    elif s=='9':
        if(v.get()!="" and v.get()!="hie" and len(v.get())<=25):
            v.set(v.get()+"9")
        elif(len(v.get())>25):
            pass
        else:
            v.set("9")
    elif s=='8':
        if(v.get()!="" and v.get()!="hie" and len(v.get())<=25):
            v.set(v.get()+"8")
        elif(len(v.get())>25):
            pass
        else:
            v.set("8")
    elif s=='7':
        if(v.get()!="" and v.get()!="hie" and len(v.get())<=25):
            v.set(v.get()+"7")
        elif(len(v.get())>25):
            pass
        else:
            v.set("7")
    elif s=='6':
        if(v.get()!="" and v.get()!="hie" and len(v.get())<=25):
            v.set(v.get()+"6")
        elif(len(v.get())>25):
            pass
        else:
            v.set("6")
    elif s=='5':
        if(v.get()!="" and v.get()!="hie" and len(v.get())<=25):
            v.set(v.get()+"5")
        elif(len(v.get())>25):
            pass
        else:
            v.set("5")
    elif s=='4':
        if(v.get()!="" and v.get()!="hie" and len(v.get())<=25):
            v.set(v.get()+"4")
        elif(len(v.get())>25):
            pass
        else:
            v.set("4")
    elif s=='3':
        if(v.get()!="" and v.get()!="hie" and len(v.get())<=25):
            v.set(v.get()+"3")
        elif(len(v.get())>25):
            pass
        else:
            v.set("3")
    elif s=='2':
        if(v.get()!="" and v.get()!="hie" and len(v.get())<=25):
            v.set(v.get()+"2")
        elif(len(v.get())>25):
            pass
        else:
            v.set("2")
    elif s=='1':
        if(v.get()!="" and v.get()!="hie" and len(v.get())<=25):
            v.set(v.get()+"1")
        elif(len(v.get())>25):
            pass
        else:
            v.set("1")
    elif s=='0':
        if(v.get()!="" and v.get()!="hie" and len(v.get())<=25):
            v.set(v.get()+"0")
        elif(len(v.get())>25):
            pass
        else:
            v.set("0")
    elif s=='+/-':
        if v.get()=="":
            pass
        else:
            if "." in v.get():
                if float(v.get())>0:
                    v.set("-"+v.get())
                elif float(v.get())<0:
                    v.set(v.get()[1:])
            else:
                 if int(v.get())>0:
                     v.set("-"+v.get())
                 elif int(v.get())<0:
                     v.set(v.get()[1:])
                          
    elif s=='+':
        if (v1.get()[len(v1.get())-1] not in l):
                        if v.get()=="":
                            pass
                        else:
                            v1.set(v.get()+"+")
                            v.set("")
        else:
            s1=v1.get()
            res=op(s1[len(s1)-1],s1[0:len(s1)-1],v.get())
            v1.set(res+"+")
            v.set("")
    elif s=='-':
        if (v1.get()[len(v1.get())-1] not in l):
                        if v.get()=="":
                            pass
                        else:
                            v1.set(v.get()+"-")
                            v.set("")
        else:
            s1=v1.get()
            res=op(s1[len(s1)-1],s1[0:len(s1)-1],v.get())
            v1.set(res+"-")
            v.set("")
    elif s=='*':
        if (v1.get()[len(v1.get())-1] not in l):
                        if v.get()=="":
                            pass
                        else:
                            v1.set(v.get()+"*")
                            v.set("")
        else:
            s1=v1.get()
            res=op(s1[len(s1)-1],s1[0:len(s1)-1],v.get())
            v1.set(res+"*")
            v.set("")
            
    elif s=='^':
        if (v1.get()[len(v1.get())-1] not in l):
                       if v.get()=="":
                           pass
                       else:
                           v1.set(v.get()+"^")
                           v.set("")
        else:
            s1=v1.get()
            res=op(s1[len(s1)-1],s1[0:len(s1)-1],v.get())
            v1.set(res+"^")
            v.set("")
            
    elif s=='/':
        if (v1.get()[len(v1.get())-1] not in l):
                        if v.get()=="":
                            pass
                        else:
                            v1.set(v.get()+"/")
                            v.set("")
        else:
            s1=v1.get()
            res=op(s1[len(s1)-1],s1[0:len(s1)-1],v.get())
            v1.set(res+"/")
            v.set("")
    elif s=='%':
        if (v1.get()[len(v1.get())-1] not in l):
                        if v.get()=="":
                            pass
                        else:
                            v1.set(v.get()+"%")
                            v.set("")
        else:
            s1=v1.get()
            res=op(s1[len(s1)-1],s1[0:len(s1)-1],v.get())
            v1.set(res+"%")
            v.set("")
    elif s=='1/x':
       if v.get()=="":
           pass
       else:
           if '.' in v.get():
               v.set(1/float(v.get()))
           else:
               v.set(1/int(v.get()))
    elif s=='.' :
        if (v1.get()[len(v1.get())-1] not in l):
            if v.get()=='':
                v.set("0.")
            elif '.' in v.get():
                pass
            else:
                        v.set(v.get()+".")
        else:
            if '.' in v.get():
                pass
            else:
                v.set(v.get()+".")
    elif s=='=':
        if (v1.get()=="welcome" or v1.get()==""):
            v.set(v.get())
        else:
            if v.get()!="":
                s1=v1.get()
                res=op(s1[len(s1)-1],s1[0:len(s1)-1],v.get())
                v1.set(s1+v.get()+"=")
                v.set(res)
#Creating buttons
Button(cal,font=('courier',10),text='=',width=15,height=2,bg='brown',fg='black',command=lambda:click('=')).grid(row=50,column=0)   
Button(cal,font=('courier',10),text='^/%',width=15,height=2,bg='cyan',fg='black',command=lambda:change('^/%')).grid(row=50,column=2)       
Button(cal,font=('courier',10),text='ce',width=15,height=2,bg='cyan',fg='black',command=lambda:click('ce')).grid(row=50,column=3)
Button(cal,font=('courier',10),text='C',width=15,height=2,bg='brown',fg='black',command=lambda:click('C')).grid(row=50,column=4)
Button(cal,font=('courier',10),text='7',width=15,height=2,command=lambda:click('7')).grid(row=51,column=0)
Button(cal,font=('courier',10),text='8',width=15,height=2,command=lambda:click('8')).grid(row=51,column=2)
Button(cal,font=('courier',10),text='9',width=15,height=2,command=lambda:click('9')).grid(row=51,column=3)
Button(cal,font=('courier',10),text='+',width=15,height=2,command=lambda:click('+')).grid(row=51,column=4)
Button(cal,font=('courier',10),text='4',width=15,height=2,command=lambda:click('4')).grid(row=52,column=0)
Button(cal,font=('courier',10),text='5',width=15,height=2,command=lambda:click('5')).grid(row=52,column=2)
Button(cal,font=('courier',10),text='6',width=15,height=2,command=lambda:click('6')).grid(row=52,column=3)
Button(cal,font=('courier',10),text='-',width=15,height=2,command=lambda:click('-')).grid(row=52,column=4)
Button(cal,font=('courier',10),text='1',width=15,height=2,command=lambda:click('1')).grid(row=53,column=0)
Button(cal,font=('courier',10),text='2',width=15,height=2,command=lambda:click('2')).grid(row=53,column=2)
Button(cal,font=('courier',10),text='3',width=15,height=2,command=lambda:click('3')).grid(row=53,column=3)
Button(cal,font=('courier',10),text='*',width=15,height=2,command=lambda:click('*')).grid(row=53,column=4)
Button(cal,font=('courier',10),text='0',width=15,height=2,command=lambda:click('0')).grid(row=54,column=0)
Button(cal,font=('courier',10),text='+/-',width=15,height=2,command=lambda:click('+/-')).grid(row=54,column=2)
Button(cal,font=('courier',10),text='.',width=15,height=2,command=lambda:click('.')).grid(row=54,column=3)
Button(cal,font=('courier',10),text='/',width=15,height=2,command=lambda:click('/')).grid(row=54,column=4)
cal.mainloop()