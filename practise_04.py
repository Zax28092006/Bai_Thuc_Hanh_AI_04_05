import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi,200)
y = np.sin(x)

#Cách 1: thiết lập biểu đồ bằng pyplot
plt.figure(figsize=(6,3))
plt.plot(x, y)
plt.title("Vẽ đồ thị bằng Pyplot")
plt.show()

# Cách 2: Vẽ biểu đồ thông qua hướng đối tượng
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(6,3))
ax.plot(x, y)
ax.set_title("Vẽ đồ thị bằng hướng đối tượng")
ax.set_xlabel("gốc(rad)")
ax.set_ylabel("sin(x)")
plt.show()

#5 basic chart
x = np.linspace(0, 2 * np.pi,200)
fig, axes = plt.subplots(2,3,figsize = (15,8))

#Biểu đồ đường (line)
axes[0,0].plot(x,np.sin(x), label = "sin")
axes[0,0].plot(x,np.cos(x), label = "cos")
axes[0,0].plot(x,np.tan(x), label = "tan")
axes[0,0].plot(x,np.tan(1/x), label = "cot")
axes[0,0].set_title("Line Chart")

#Scatter chart
rng = np.random.default_rng(42)
xs, ys = rng.random(80), rng.random(80)
sc = axes[0,1].scatter(xs, ys, c = xs + ys, s = ys*200, cmap = "viridis", alpha = 0.7)
axes[0,1].set_title("Scatter")
fig.colorbar(sc, ax=axes[0,1])

#Bar chart
prod = ['A','B','C','D']
axes[0,2].bar(prod,[23,45,31,38], color = "red")
axes[0,2].set_title("Bar")

#Histogram chart
axes[1,0].hist(rng.normal(70,15,120000000), bins = 10, edgecolor = "green", color = "white")
axes[1,0].set_title("Histogram")
#rng.normal(70,15,1000)
#70: trung bình(mean) -> dự liệu tập trung quanh giá trị 70
#15: độ lệch chuẩn -> mức độ phân tán, mức phân tán càng lớn thì dữ liệu càng trải rộng ra
#1000: số lượng mẫu cần sinh ra
#bins = 30 -> chia thành 30 khoảng

fig.suptitle("5 basic chart", fontsize = 15)
fig.tight_layout()
plt.show()

#Bai A1
x = np.linspace(-5,5, 200)
y1 = x**2
y2 = x**3

fig, ax = plt.subplots(figsize=(6,3))
ax.plot(x,y1, label = "y = x**2")
ax.plot(x,y2, label = "y = x**3")
ax.set_xlabel("Trục x")
ax.set_ylabel("Trục y")
ax.set_title("Line Chart")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

#Bài A2
fig, ax = plt.subplots(figsize = (6,3))
rng = np.random
xs, ys = rng.uniform(-1,1,150),rng.uniform(-1,1,150)

q1 = (xs >= 0) & (ys >= 0)
q2 = (xs < 0) & (ys >= 0)
q3 = (xs < 0) & (ys < 0)
q4 = (xs >= 0) & (ys < 0)

ax.scatter(xs[q1],ys[q1], color = "blue", label = "Góc phần tư I")
ax.scatter(xs[q2],ys[q2], color = "green", label = "Góc phần tư II")
ax.scatter(xs[q3],ys[q3], color = "orange", label = "Góc phần tư III")
ax.scatter(xs[q4], ys[q4], color = "black", label = "Góc phần tư IV")

plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=0, color='black', linestyle='--')
ax.legend()
ax.set_title("Scatter")

#Bài A3
fig, ax = plt.subplots(figsize = (8,6))
prod = ['A','B','C','D','E']
value = [23,45,31,38,50]
bars = ax.bar(prod,value, color = "lightgray")
plt.bar_label(bars,value)
max_value = max(value)
max_index = value.index(max_value)
bars[max_index].set_color("orange")
ax.set_title("Bar")

fig, axes = plt.subplots(2,2,figsize = (18,16))
x = np.linspace(-5,5, 200)
y1 = x**2
y2 = x**3

#Bài A4
#first chart
axes[0,0].plot(x,y1, label = "y = x**2")
axes[0,0].plot(x,y2, label = "y = x**3")
axes[0,0].set_xlabel("Trục x")
axes[0,0].set_ylabel("Trục y")
axes[0,0].set_title("Line Chart")
axes[0,0].grid(True, linestyle="--", alpha=0.7)
axes[0,0].legend()

#second chart
rng = np.random
xs, ys = rng.uniform(-1,1,150),rng.uniform(-1,1,150)

q1 = (xs >= 0) & (ys >= 0)
q2 = (xs < 0) & (ys >= 0)
q3 = (xs < 0) & (ys < 0)
q4 = (xs >= 0) & (ys < 0)

axes[0,1].scatter(xs[q1],ys[q1], color = "blue", label = "Góc phần tư I")
axes[0,1].scatter(xs[q2],ys[q2], color = "green", label = "Góc phần tư II")
axes[0,1].scatter(xs[q3],ys[q3], color = "orange", label = "Góc phần tư III")
axes[0,1].scatter(xs[q4], ys[q4], color = "black", label = "Góc phần tư IV")

axes[0,1].axhline(y=0, color='black', linestyle='--')
axes[0,1].axvline(x=0, color='black', linestyle='--')
axes[0,1].legend()
axes[0,1].set_title("Scatter")

#third chart
prod = ['A','B','C','D','E']
value = [23,45,31,38,50]
bars = axes[1,0].bar(prod,value, color = "lightgray")
axes[1,0].bar_label(bars,value)
max_value = max(value)
max_index = value.index(max_value)
bars[max_index].set_color("orange")
axes[1,0].set_title("Bar")

#forth chart
axes[1,1].hist(rng.normal(70,15,120000000), bins = 10, edgecolor = "green", color = "white")
axes[1,1].set_title("Histogram")
fig.suptitle("5 basic chart", fontsize = 15)
fig.tight_layout()
plt.savefig("bieudo.png", dpi=300, bbox_inches="tight")
plt.savefig('bieudo.pdf', format='pdf', bbox_inches='tight')
plt.show()

#Bài A6
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(10, 6))
#gridspec
gs = gridspec.GridSpec(nrows=4, ncols=4)
ax1 = fig.add_subplot(gs[0:2, 0:2]) 
x = np.linspace(-5,5, 200)
y1 = x**2
y2 = x**3
ax1.plot(x,y1, label = "y = x**2")
ax1.plot(x,y2, label = "y = x**3")
ax1.set_xlabel("Trục x")
ax1.set_ylabel("Trục y")
ax1.set_title("Line Chart") 
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()   # Spans all columns in the top row
ax2 = fig.add_subplot(gs[0:1,3:4])# Spans first two columns of the middle row
rng = np.random
xs, ys = rng.uniform(-1,1,150),rng.uniform(-1,1,150)

q1 = (xs >= 0) & (ys >= 0)
q2 = (xs < 0) & (ys >= 0)
q3 = (xs < 0) & (ys < 0)
q4 = (xs >= 0) & (ys < 0)

ax2.scatter(xs[q1],ys[q1], color = "blue", label = "Góc phần tư I")
ax2.scatter(xs[q2],ys[q2], color = "green", label = "Góc phần tư II")
ax2.scatter(xs[q3],ys[q3], color = "orange", label = "Góc phần tư III")
ax2.scatter(xs[q4], ys[q4], color = "black", label = "Góc phần tư IV")

plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=0, color='black', linestyle='--')
ax2.legend()
ax2.set_title("Scatter")
ax3 = fig.add_subplot(gs[3:4, 0:1])
prod = ['A','B','C','D','E']
value = [23,45,31,38,50]
bars = ax3.bar(prod,value, color = "lightgray")
plt.bar_label(bars,value)
max_value = max(value)
max_index = value.index(max_value)
bars[max_index].set_color("orange")
ax3.set_title("Bar")