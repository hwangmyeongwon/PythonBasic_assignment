# -*- coding: utf-8 -*-



import tkinter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import animation
Ydat = []
Xdat = []
Ndat=[]
n_max=6000
#=== System Parameter of R-C Circuit =================
R=100000 #Resistance
C=0.000001 #Capacitance
dt=0.00001 #Sampling period
#=== Initial Output ===================================
#Xtemp=0
Ytemp=0
Xdat.append(Ytemp)
Ydat.append(Ytemp)
num=dt/R/C
for n in range (0,n_max):
    Xtemp=1 #Input 
    Ytemp1=Ytemp #Current Output
    Ytemp=(1-num)*Ytemp1+num*Xtemp #System Output Equation : Next Output
    Xdat.append(n*dt)
    Ydat.append(Ytemp)
    Ndat.append(n)
print(Ydat)
plt.figure(1)

plt.plot(Xdat,Ydat)
plt.xlabel('Time(sec)')
plt.ylabel('Vc', fontsize=20)
plt.title("Step Response")
plt.grid(True)
#Frequency Responso
mag=[]
phase=[]
for w in range(300) :
   m=1/np.sqrt((R*C*w)**2+1)
   p=-np.arctan(R*C*w)*180/np.pi
   mag.append(m)
   phase.append(p)
plt.figure(2)

plt.subplot(211)
plt.plot(mag)
plt.xlabel('w(rad/sec)')
plt.ylabel('magnitude', fontsize=12)
plt.title("Frequency Response")
plt.grid(True)
plt.subplot(212)
plt.plot(phase)
plt.xlabel('w(rad/sec)')
plt.ylabel('phase(rad)*180/pi', fontsize=12)

plt.grid(True)


XXdat=np.array(0)
YYdat=np.array(0)
NNdat=np.array(0)
num1=dt/R/C/2

YYtemp=0
for n in range (0,n_max):
    XXtemp=1 #Input 
    YYtemp1=YYtemp #Current Output
    YYtemp=(1-num1)*YYtemp1+num1*XXtemp #System Output Equation : Next Output
    XXdat=np.append(XXdat,n*dt)
    YYdat=np.append(YYdat,YYtemp)
    NNdat=np.append(NNdat,n)
    

plt.figure(3)


plt.plot(Xdat,Ydat,label="System1")
plt.plot(XXdat,YYdat,label="System2")
plt.xlabel('Time(sec)')
plt.ylabel('Vc', fontsize=20)
plt.axis([0,0.1,0,2])
plt.legend(loc=0)
plt.title("Step Response")
plt.grid(True)
#Frequency Responso




class MyInformaion:
    def info(self):
        self.name=""
        self.age=0
        self.schoolnum=0
        self.major=""
        self.email=""
class grade:
    def grad(self):
        self.first=""
        self.second=""
        self.third=""
        self.forth=""

def calc(event):
    label.config(text="결과="+str(eval(entry.get())))
def name(event):
      label.config(text="이름="+(entry.get()))
      MyInformaion.name=entry.get()
def age(event):
    label.config(text="나이=" + (entry.get()))
    MyInformaion.age = entry.get()
def schoolnum(event):
    label.config(text="학번=" + (entry.get()))
    MyInformaion.schoolnum = entry.get()
def major(event):
    label.config(text="전공=" + (entry.get()))
    MyInformaion.major = entry.get()
def email(event):
    label.config(text="email=" + (entry.get()))
    MyInformaion.email = entry.get()
def first(event):
    label.config(text="1학년 학점=" + (entry.get()))
    grade.first = entry.get()
def second(event):
    label.config(text="2학년 학점=" + (entry.get()))
    grade.second = entry.get()
def third(event):
    label.config(text="3학년 학점=" + (entry.get()))
    grade.third = entry.get()
def fourth(event):
    label.config(text="4학년 학점=" + (entry.get()))
    grade.fourth = entry.get()

window=tkinter.Tk()
window.title("MyInformation 이름")
window.geometry("400x400+100+100")
window.resizable(False, False)
entry=tkinter.Entry(window)
entry.bind("<Return>", name)
entry.pack()
label=tkinter.Label(window)
label.pack()
window.mainloop()

window1=tkinter.Tk()
window1.title("MyInformation 나이 ")
window1.geometry("400x400+100+100")
window1.resizable(False, False)
entry=tkinter.Entry(window1)
entry.bind("<Return>", age)
entry.pack()
label=tkinter.Label(window1)
label.pack()
window1.mainloop()

window2=tkinter.Tk()
window2.title("MyInformation 학번 ")
window2.geometry("400x400+100+100")
window2.resizable(False, False)
entry=tkinter.Entry(window2)
entry.bind("<Return>", schoolnum)
entry.pack()
label=tkinter.Label(window2)
label.pack()
window2.mainloop()

window3=tkinter.Tk()
window3.title("MyInformation 전공 ")
window3.geometry("400x400+100+100")
window3.resizable(False, False)
entry=tkinter.Entry(window3)
entry.bind("<Return>", major)
entry.pack()
label=tkinter.Label(window3)
label.pack()
window3.mainloop()

window4=tkinter.Tk()
window4.title("MyInformation 이메일 ")
window4.geometry("400x400+100+100")
window4.resizable(False, False)
entry=tkinter.Entry(window4)
entry.bind("<Return>", email)
entry.pack()
label=tkinter.Label(window4)
label.pack()
window4.mainloop()

window5=tkinter.Tk()
window5.title("Grade 1학년 학점 ")
window5.geometry("400x400+100+100")
window5.resizable(False, False)
entry=tkinter.Entry(window5)
entry.bind("<Return>", first)
entry.pack()
label=tkinter.Label(window5)
label.pack()
window5.mainloop()

window6=tkinter.Tk()
window6.title("Grade 2학년 학점 ")
window6.geometry("400x400+100+100")
window6.resizable(False, False)
entry=tkinter.Entry(window6)
entry.bind("<Return>", second)
entry.pack()
label=tkinter.Label(window6)
label.pack()
window6.mainloop()

window7=tkinter.Tk()
window7.title("Grade 3학년 학점 ")
window7.geometry("400x400+100+100")
window7.resizable(False, False)
entry=tkinter.Entry(window7)
entry.bind("<Return>", third)
entry.pack()
label=tkinter.Label(window7)
label.pack()
window7.mainloop()

window8=tkinter.Tk()
window8.title("Grade 4학년 학점 ")
window8.geometry("400x400+100+100")
window8.resizable(False, False)
entry=tkinter.Entry(window8)
entry.bind("<Return>", fourth)
entry.pack()
label=tkinter.Label(window8)
label.pack()
window8.mainloop()

main=tkinter.Tk()
main.title("Term Project ")
main.geometry("600x600+100+100")
main.resizable(False, False)

text=tkinter.Text(main)
text.insert(tkinter.CURRENT,"개인정보\n")
text.insert("current", "성명 "+MyInformaion.name)
text.insert("current", "\n나이 "+MyInformaion.age)
text.insert("current", "\n학년 "+MyInformaion.schoolnum)
text.insert("current", "\n전공 "+MyInformaion.major)
text.insert("current", "\n학점 ")
text.insert("current", "\n1학년 "+grade.first)
text.insert("current", "\n2학년 "+grade.second)
text.insert("current", "\n3학년 "+grade.third)
text.insert("current", "\n4학년 "+grade.fourth)

text.pack()







fig=plt.figure(3)
canvas = FigureCanvasTkAgg(fig,main)
canvas.get_tk_widget().pack()
main.mainloop()


