"""
==================
Animated line plot
==================

"""
#import os as os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#plt.rcParams['animation.ffmpeg_path']='‪C:\FFmpeg\bin\ffmpeg.exe'

#print(os.path.exists('animation.ffmpeg_path'))

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
writer = animation.FFMpegWriter(
     fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani.save("movie.mp4", writer=writer)

#plt.show()
