import numpy as np
import matplotlib.pyplot as plt




x1dot=0
x2dot=0
k=0.9
B=0.1
x0=2.7
x=3.4
x1=x/2
x2=x1
m1=0.4
m2=0.8
dt=0.01
t=0
tt=[]
xx1=[]
xx2=[]
while(t<10):
    dx=x-x0
    x1dotdot=(-k*dx+B*x1dot)/m1
    x2dotdot=(-k*dx+B*x2dot)/m2
    x1dot=x1dot+x1dotdot*dt
    x2dot=x2dot+x2dotdot*dt
    x1=x1+x1dot*dt
    x2=x2+x2dot*dt
    xx1.append(x1)
    xx2.append(x2)
    x=x1+x2
    tt.append(t)
    t+=dt
# 3. Plot each line individually and assign a 'label' for the legend
plt.plot(tt, xx1, color='blue', label='particle 1')
#plt.plot(t11, xx1, color='red',   label='y11')
plt.plot(tt, xx2, color='green', label='particle 2')

# 4. Add titles, labels, and turn on the grid
plt.title("Plotting Multiple Lines")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)

# 5. Display the legend (uses the 'label' tags from step 3)
plt.legend()

# 6. Show the final graph
plt.show()
