import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

l0=0.7

dt=0.01
m1=0.9
m2=0.5
B=0.2
K=0.7
x1dot=0
y1dot=0
x2dot=0
y2dot=0
x1=0.1
y1=0.2
x2=0.7
y2=0.9
xx1=[]
xx2=[]
yy1=[]
yy2=[]
tt=[]
t=0

while(t<10):
    l=np.sqrt((x1-x2)**2+(y1-y2)**2)
    dl=l-l0
    theta=np.atan((y2-y1)/(x2-x1))
    dx=dl*np.cos(theta)
    dy=dl*np.sin(theta)
    g=9.81
    mu1=0.5
    mu2=0.4
    bx=B*np.cos(theta)
    by=B*np.sin(theta)
    kx=K*np.cos(theta)
    ky=K*np.sin(theta)

    x1dotdot=(kx*dx-bx*np.abs(x1dot))/m1
    y1dotdot=(ky*dy-by*np.abs(y1dot))/m1
    x2dotdot=(-kx*dx+bx*np.abs(x2dot))/m2
    y2dotdot=(-ky*dy+by*np.abs(y2dot))/m2
    x1dot+=x1dotdot*dt
    y1dot+=y1dotdot*dt
    x2dot+=x2dotdot*dt
    y2dot+=y2dotdot*dt
    xx1.append(x1)
    xx2.append(x2)
    yy1.append(y1)
    yy2.append(y2)
    tt.append(t)
    x1+=x1dot*dt
    y1+=y1dot*dt
    x2+=x2dot*dt
    y2+=y2dot*dt
    t+=dt

# 3. Plot each line individually and assign a 'label' for the legend
#plt.plot(tt, xx1, color='blue', label='particle 1x')
#plt.plot(t11, xx1, color='red',   label='y11')
#plt.plot(tt, yy1, color='black', label='particle 1y')
#plt.plot(tt, xx2, color='red', label='particle 2x')
#plt.plot(t11, xx1, color='red',   label='y11')
#plt.plot(tt, yy2, color='green', label='particle 2y')

# 4. Add titles, labels, and turn on the grid
#plt.title("Plotting Multiple Lines")
#plt.xlabel("X Axis")
#plt.ylabel("Y Axis")
#plt.grid(True)

# 5. Display the legend (uses the 'label' tags from step 3)
#plt.legend()

# 6. Show the final graph
#plt.show()




# 1. Define your X and Y arrays (Example: a spiral path)
# Replace these with your own numpy arrays or lists
theta = tt
x_data = xx2
y_data = yy2
num_frames = len(x_data)  # Total number of frames in the animation

trajectories = [
    {"name": "particle A", "color": "teal",     "x": xx1,     "y": yy1},
    {"name": "particle B", "color": "crimson",  "x": xx2, "y": yy2},
    
]

# 2. Setup the plot canvas
fig, ax = plt.subplots(figsize=(8, 8))
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_title("Multi-Trajectory Tracker", fontsize=12, fontweight='bold')

# Find global min/max bounds across all trajectories to set static plot limits
all_x = np.concatenate([t["x"] for t in trajectories])
all_y = np.concatenate([t["y"] for t in trajectories])
ax.set_xlim(np.min(all_x) - 1, np.max(all_x) + 1)
ax.set_ylim(np.min(all_y) - 1, np.max(all_y) + 1)

# 3. Create plot objects dynamically and store them in lists
lines = []
dots = []

for t in trajectories:
    # Build trail line
    line, = ax.plot([], [], color=t["color"], alpha=0.5, linewidth=2, label=f"{t['name']} Trail")
    lines.append(line)
    # Build leading dot particle
    dot, = ax.plot([], [], marker='o', color=t["color"], markersize=8, label=t["name"])
    dots.append(dot)

ax.legend(loc='lower right')

# Create a telemetry text container anchored to the top-left corner
telemetry_text = ax.text(
    0.05, 0.95, '', 
    transform=ax.transAxes, 
    fontsize=9, 
    fontfamily='monospace',
    verticalalignment='top', 
    bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8, edgecolor='gray')
)

# 4. Initialization function
def init():
    for line, dot in zip(lines, dots):
        line.set_data([], [])
        dot.set_data([], [])
    telemetry_text.set_text('')
    # Return all graphical elements that change
    return lines + dots + [telemetry_text]

# 5. Animation update loop (runs for every frame index 'i')
def update(i):
    text_output = f"Frame: {i:03d} / {num_frames}\n"
    text_output += "=" * 25 + "\n"
    
    # Iterate through each trajectory index and update its respective line/dot
    for idx, t in enumerate(trajectories):
        # Update trailing path line segment
        lines[idx].set_data(t["x"][:i+1], t["y"][:i+1])
        
        # Update current step head dot position
        current_x = t["x"][i]
        current_y = t["y"][i]
        dots[idx].set_data([current_x], [current_y])
        
        # Append telemetry data for this specific point to the screen readout
        text_output += f"{t['name']}: X={current_x:5.2f} | Y={current_y:5.2f}\n"
        
    telemetry_text.set_text(text_output.strip())
    
    # Return flat list of updated artists
    return lines + dots + [telemetry_text]

# 6. Instantiate and run animation
ani = FuncAnimation(
    fig, 
    update, 
    frames=len(xx1), 
    init_func=init, 
    interval=40, 
    blit=True
)

# Uncomment to render video file output:
# ani.save('multi_trajectory.mp4', writer='ffmpeg', fps=25)

plt.show()


