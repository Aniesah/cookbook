import math

xc = 20
yc = 20
r = 10
circle = plt.Circle(
    (xc, yc), radius=r,
    fc='#ccf',
    lw=2, ls='dashed', color='k'
)
plt.gca().add_patch(circle)

x = 80
y = 80
w = 20
h = 20
rectangle = plt.Rectangle(
    (x, y), w, h,
    fc='b',
    color='r', ls='solid', lw=4
)
plt.gca().add_patch(rectangle)

x1 = 20 + r * math.cos(45/180 * math.pi)
y1 = 20 + r * math.sin(45/180 * math.pi)
x2 = 80
y2 = 80
line = plt.Line2D((x1, x2), (y1, y2), color='#4c4', lw=2, ls='solid')
plt.gca().add_line(line)

plt.axis('scaled')
plt.show()