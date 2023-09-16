import matplotlib.pyplot as plt

# 创建一个图形和轴对象
fig, ax = plt.subplots()

# 定义起始点的坐标
start_x = 1
start_y = 1

# 定义向量的方向（朝向）和长度
dx = 2  # 在x轴上的分量
dy = 3  # 在y轴上的分量

# 使用plt.quiver()绘制向量
ax.quiver(start_x, start_y, dx, dy, angles='xy', scale_units='xy', scale=1, color='blue')

# 设置坐标轴范围
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)

# 显示图形
plt.grid()
plt.show()

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms
import numpy as np

# 创建一个图形和轴对象
fig, ax = plt.subplots(figsize=(8, 8))

# 矩形的中心点坐标
center_x = 250
center_y = 260

# 矩形的长和宽
length = 64
width = 64

# 旋转角度
angle_degrees = 30
angle_radians = np.deg2rad(angle_degrees)

# -----------------------
# 第一种方式：旋转中心不是矩形中心
# -----------------------

# 计算矩形的左下角坐标
left_x = center_x - length / 2
bottom_y = center_y - width / 2

# 创建矩形对象（旋转中心不是矩形中心）
rectangle0 = patches.Rectangle((left_x, bottom_y), length, width,
                               angle=0, fill=False, edgecolor='green', label='original')
rectangle1 = patches.Rectangle((left_x, bottom_y), length, width,
                               angle=angle_degrees, fill=False, edgecolor='blue', label='not center')

# -----------------------
# 第二种方式：旋转中心是矩形中心
# -----------------------

# 计算矩形的四个顶点坐标
# cos_theta = np.cos(angle_radians)
# sin_theta = np.sin(angle_radians)
# x1 = center_x - (length / 2) * cos_theta - (width / 2) * sin_theta
# y1 = center_y - (length / 2) * sin_theta + (width / 2) * cos_theta
# x2 = center_x + (length / 2) * cos_theta - (width / 2) * sin_theta
# y2 = center_y + (length / 2) * sin_theta + (width / 2) * cos_theta
# x3 = center_x + (length / 2) * cos_theta + (width / 2) * sin_theta
# y3 = center_y + (length / 2) * sin_theta - (width / 2) * cos_theta
# x4 = center_x - (length / 2) * cos_theta + (width / 2) * sin_theta
# y4 = center_y - (length / 2) * sin_theta - (width / 2) * cos_theta


def rotate_rectangle(center_x, center_y, height, width, angle_degrees):
    # 将角度转换为弧度
    angle_radians = np.deg2rad(angle_degrees)

    # 计算旋转后的四个顶点坐标
    cos_theta = np.cos(angle_radians)
    sin_theta = np.sin(angle_radians)
    x1 = center_x - (width / 2) * cos_theta - (height / 2) * sin_theta
    y1 = center_y - (width / 2) * sin_theta + (height / 2) * cos_theta
    x2 = center_x + (width / 2) * cos_theta - (height / 2) * sin_theta
    y2 = center_y + (width / 2) * sin_theta + (height / 2) * cos_theta
    x3 = center_x + (width / 2) * cos_theta + (height / 2) * sin_theta
    y3 = center_y + (width / 2) * sin_theta - (height / 2) * cos_theta
    x4 = center_x - (width / 2) * cos_theta + (height / 2) * sin_theta
    y4 = center_y - (width / 2) * sin_theta - (height / 2) * cos_theta

    return x1, y1, x2, y2, x3, y3, x4, y4


x1, y1, x2, y2, x3, y3, x4, y4 = rotate_rectangle(center_x, center_y, length, width, angle_degrees)


def rotate_rectangle2(center_x, center_y, height, width, angle_degrees):
    # 将角度转换为弧度
    angle_radians = np.deg2rad(angle_degrees)

    # 创建旋转矩阵
    rotation_matrix = np.array([
        [np.cos(angle_radians), -np.sin(angle_radians)],
        [np.sin(angle_radians), np.cos(angle_radians)]
    ])

    # 计算矩形的四个顶点相对于中心点的坐标
    vertices_relative = np.array([
        [-width / 2, height / 2],
        [width / 2, height / 2],
        [width / 2, -height / 2],
        [-width / 2, -height / 2]
    ])

    # 使用矩阵运算计算旋转后的顶点坐标
    rotated_vertices_relative = np.dot(rotation_matrix, vertices_relative.T).T

    # 将相对坐标转换为绝对坐标
    x = rotated_vertices_relative[:, 0] + center_x
    y = rotated_vertices_relative[:, 1] + center_y

    return x, y


x, y = rotate_rectangle2(center_x, center_y, length, width, angle_degrees)
print(f"x: {x}")
print(f"y: {y}")
print([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
# 创建矩形对象（旋转中心是矩形中心）
rectangle2 = patches.Polygon([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], closed=True, fill=False, edgecolor='red', label='center')
rectangle3 = patches.Polygon(list(zip(x, y)), closed=True, fill=False, edgecolor='black', label='center')

# 将矩形对象添加到轴中
ax.add_patch(rectangle0)
ax.add_patch(rectangle1)
ax.add_patch(rectangle2)
ax.add_patch(rectangle3)

# 设置坐标轴范围
ax.set_xlim(0, 512)
ax.set_ylim(0, 512)

# 显示图形
plt.grid()
plt.legend()
plt.show()


x, y = rotate_rectangle2(center_x, center_y, length, width, angle_degrees)

# 创建一个图形和轴对象
fig, ax = plt.subplots(figsize=(6, 6))

# 创建旋转矩形的多边形对象
polygon = plt.Polygon(list(zip(x, y)), closed=True, fill=False, edgecolor='blue')

# 将多边形对象添加到轴中
ax.add_patch(polygon)

# 设置坐标轴范围
ax.set_xlim(0, 512)
ax.set_ylim(0, 512)

# 显示图形
plt.grid()
plt.show()
