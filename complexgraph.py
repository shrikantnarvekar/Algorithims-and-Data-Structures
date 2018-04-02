from tkinter import *
mainloop=Tk()
c=Canvas(mainloop,width=400,height=400)
c.create_line(200,0,200,400,fill="red")
c.create_line(0,200,400,200,fill="red")
z=complex(2,3)
d=10
i=200
f=200
#first no
x=z.real
y=z.imag
a=(i+(x*d))
b=(f-(y*d))
c.create_oval(a-2,b-2,a+2,b+2,fill="blue")
#reflection
m=(-1)*(z)
x1=m.real
y1=m.imag
a1=(i+(x1*d))
b1=(f-(y1*d))
c.create_oval(a1-2,b1-2,a1+2,b1+2,fill="purple")
#scaling
m1=(0.5)*(z)
x2=m1.real
y2=m1.imag
a2=(i+(x2*d))
b2=(f-(y2*d))
c.create_oval(a2-2,b2-2,a2+2,b2+2,fill="black")
#rotate 90
m2=z*((-1)**(0.5))
x3=m2.real
y3=m2.imag
a3=(i+(x3*d))
b3=(f-(y3*d))
c.create_oval(a3-2,b3-2,a3+2,b3+2,fill="pink")
#rotate 180
m3=complex(-2,-3)
x4=m3.real
y4=m3.imag
a4=(i+(x4*d))
b4=(f-(y4*d))
c.create_oval(a4-2,b4-2,a4+2,b4+2,fill="brown")
#rotate 270
m4=complex(3,-2)
x5=m4.real
y5=m4.imag
a5=(i+(x5*d))
b5=(f-(y5*d))
c.create_oval(a5-2,b5-2,a5+2,b5+2,fill="red")


c.pack()
c.mainloop()
