# %% [markdown]
# # Subplots

# %%
# import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
plt.plot([1,2,3,4], [2,6,8,10], 'ro--')

# %%
fig = plt.figure()
fig.add_axes

# %%
fig, ax = plt.subplots()
ax.plot([1,2,3,4], [2,6,8,10], 'ro--')

# %%
fig, axes = plt.subplots(2,1, figsize=(8, 8))

ax1, ax2= axes

data = np.linspace(0, 50, 100)

ax1.set_title("Linear Graph")
ax1.plot(data, data, label="linear")

ax2.set_title("Quadratic Graph")
ax2.plot(data, data**2, label="linear")

# %%
fig, ax = plt.subplots(figsize=(8, 5))

data = np.linspace(0, 2, 100)

ax.plot(data, data, label="linear")
ax.plot(data, data**2, label="quadratic")

# can be comined in a single function:
# ax.plot(data, data, 'r--', data, data**2, 'b-')

ax.legend()

plt.show()

# %%


# %% [markdown]
# # Bar Graphs

# %%
companies = ["Apple", "Microsoft", "Googole", "Amazon", "Facebook", "Twitter"]
revenue = np.asarray([98, 212, 39, 432, 123, 876])
expenses = np.asarray([21, 144, 20, 232, 56, 453])
profit = revenue - expenses
x = np.arange(0, 6)

plt.ylabel("Revenue (millions)")
plt.bar(x-0.2, revenue, width=0.4, label="Revenue")
plt.bar(x+0.2, expenses, width=0.4, label="Expenses")
plt.legend()



# %%
companies = ["Apple", "Microsoft", "Googole", "Amazon", "Facebook", "Twitter"]
revenue = np.asarray([98, 212, 39, 432, 123, 876])
expenses = np.asarray([21, 144, 20, 232, 56, 453])
profit = revenue - expenses
x = np.arange(0, 6)

plt.ylabel("Revenue (millions)")
plt.bar(x-0.3, revenue, width=0.3, label="Revenue")
plt.bar(x, expenses, width=0.3, label="Expenses")
plt.bar(x+0.3, profit, width=0.3, label="Profit")
plt.legend()


# %%
companies = ["Apple", "Microsoft", "Googole", "Amazon", "Facebook", "Twitter"]
revenue = np.asarray([98, 212, 39, 432, 123, 876])
expenses = np.asarray([21, 144, 20, 232, 56, 453])
profit = revenue - expenses
x = np.arange(0, 6)

plt.ylabel("Revenue (millions)")
plt.barh(x-0.3, revenue, height=0.3, label="Revenue")
plt.barh(x, expenses, height=0.3, label="Expenses")
plt.barh(x+0.3, profit, height=0.3, label="Profit")
plt.legend()


# %% [markdown]
# # Reading CSV

# %%
data = pd.read_csv("companies-revenue.csv")

companies = data["Name"]
revenues = data["Revenues"]
expenses = data["Expenses"]
profit = data["Profits"]
x = np.arange(len(companies))

plt.ylabel("Revenues (millions)")
plt.bar(x-0.3, revenues, width=0.3, label="Revenue")
plt.bar(x, expenses, width=0.3, label="Expenses")
plt.bar(x+0.3, profit, width=0.3, label="Profit")
plt.legend()

# %% [markdown]
# # Histogram

# %%
student_age_info = [23,21, 43, 32, 56, 61, 48, 39, 31, 41, 36, 19, 18, 20, 25, 28, 27, 32 ]

plt.hist(student_age_info, rwidth=0.8)

# %%
student_age_info = [23,21, 43, 32, 56, 61, 48, 39, 31, 41, 36, 19, 18, 20, 25, 28, 27, 32 ]

plt.hist(student_age_info, rwidth=0.8, bins=5)

# %%
student_age_info = [23,21, 43, 32, 56, 61, 48, 39, 31, 41, 36, 19, 18, 20, 25, 28, 27, 32 ]

plt.hist(student_age_info, rwidth=0.8, bins=[20, 30, 50, 100])

# %%
student_age_info = [23,21, 43, 32, 56, 61, 48, 39, 31, 41, 36, 19, 18, 20, 25, 28, 27, 32 ]

plt.hist(student_age_info, rwidth=0.8, bins=[20, 30, 50, 100], color="g", histtype="step")

# %%
student_age_info = [23,21, 43, 32, 56, 61, 48, 39, 31, 41, 36, 19, 18, 20, 25, 28, 27, 32 ]

plt.hist(student_age_info, rwidth=0.8, bins=[20, 30, 50, 100], color="g", orientation="horizontal")

# %%
male_age_info = [23, 21, 43, 32, 56, 61, 48, 39, 31, 41, 36, 19, 18, 20, 25, 28, 27, 32]
female_age_info = [
    32,
    18,
    19,
    20,
    21,
    26,
    54,
    43,
    26,
    29,
    25,
    47,
    46,
    42,
    33,
    44,
    31,
    28,
]

plt.hist(
    [male_age_info, female_age_info],
    rwidth=0.9,
    bins=[20, 30, 50, 100],
    color=["g", "orange"],
    label=["male", "female"],
)
plt.legend()


# %% [markdown]
# # Piechart
# 
# Show percentage

# %%
monthly_exp = [1500, 600, 250, 150, 200]
exp_label = ["Rent", "Food", "Utilities", "Car Insurance", "Shopping"]

plt.pie(monthly_exp, labels=exp_label)

# %%
monthly_exp = [1500, 600, 250, 150, 200]
exp_label = ["Rent", "Food", "Utilities", "Car Insurance", "Shopping"]

plt.pie(monthly_exp, labels=exp_label, autopct="%.2f%%", radius=1.5)
plt.show()

# %%
monthly_exp = [1500, 600, 250, 150, 200]
exp_label = ["Rent", "Food", "Utilities", "Car Insurance", "Shopping"]

plt.pie(
    monthly_exp,
    labels=exp_label,
    autopct="%.2f%%",
    radius=1.5,
    explode=[0, 0, 0, 0.1, 0.5],
    counterclock=False,
)
plt.show()


# %%
monthly_exp = [1500, 600, 250, 150, 200]
exp_label = ["Rent", "Food", "Utilities", "Car Insurance", "Shopping"]

plt.pie(
    monthly_exp,
    labels=exp_label,
    autopct="%.2f%%",
    radius=1.5,
    counterclock=True,
    startangle=45
)
plt.show()

# %%
monthly_exp = [1500, 600, 250, 150, 200]
exp_label = ["Rent", "Food", "Utilities", "Car Insurance", "Shopping"]

plt.pie(
    monthly_exp,
    labels=exp_label,
    autopct="%.2f%%",
    radius=1.5,
    counterclock=True,
    startangle=45,
    wedgeprops={"edgecolor":"black"}
)
plt.show()

# %% [markdown]
# ## Save Figure

# %%
monthly_exp = [1500, 600, 250, 150, 200]
exp_label = ["Rent", "Food", "Utilities", "Car Insurance", "Shopping"]

plt.title("My Montly Expenses")
plt.pie(
    monthly_exp,
    labels=exp_label,
    autopct="%.2f%%",
    radius=1,
    counterclock=True,
    startangle=45,
    wedgeprops={"edgecolor":"black"}
)

plt.savefig("expense-chart.png", bbox_inches="tight", pad_inches=1, transparent=True)

plt.show()

# %% [markdown]
# # Stack Plot
# 
# Plot data over range of time

# %%
minutes = [i for i in range(10, 100, 10)]

p1 = [2, 4, 4, 5, 1, 0, 3, 2, 1]
p2 = [5, 2, 1, 0, 2, 2, 1, 2, 3]
p3 = [3, 3, 3, 2, 1, 1, 0, 1, 2]

plt.stackplot(
    minutes, p1, p2, p3, labels=["P1", "P2", "P3"], colors=["blue", "red", "orange"]
)
plt.title("Players - Scores")
plt.legend()


# %%
"""
Takeover
1 team member is quitting, and transfer the code to the other two team members
"""

days = [i for i in range(1, 10)]
dev1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
dev2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
dev3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

plt.stackplot(
    days,
    dev1,
    dev2,
    dev3,
    labels=["Dev1", "Dev2", "Dev3"],
    colors=["blue", "red", "orange"],
)
plt.legend()
plt.title("Project Takeover Time")


# %% [markdown]
# # Scatterplot
# 
# Relationship between two set of data or variable and to see if they are correlated

# %%
videos = [i for i in range(1, 11)]
views = [10000, 20000, 1500, 7000, 1700, 25000, 11000, 2500, 2400, 9000]
likes = [100, 3000, 2000, 20, 4000, 50, 125, 430, 750, 1000]
dislikes = [2000, 150, 120, 540, 870, 920, 810, 490, 40, 500]

plt.scatter(videos, views)

# %%
videos = [i for i in range(1, 11)]
views = [10000, 20000, 1500, 7000, 1700, 25000, 11000, 2500, 2400, 9000]
likes = [100, 3000, 2000, 20, 4000, 500, 1205, 4300, 7500, 1000]
dislikes = [2000, 150, 120, 540, 870, 920, 810, 490, 40, 500]

# additional info representated via color, size
plt.scatter(videos, views, c=likes, cmap="summer")
plt.colorbar()

# %%
videos = [i for i in range(1, 11)]
views = [10000, 20000, 1500, 7000, 1700, 25000, 11000, 2500, 2400, 9000]
likes = [100, 3000, 2000, 20, 4000, 500, 1205, 4300, 7500, 1000]
dislikes = [2000, 150, 120, 540, 870, 920, 810, 490, 40, 500]

# additional info representated via color, size
plt.scatter(videos, views, s=dislikes, c=likes, cmap="summer")
plt.colorbar()

# %% [markdown]
# # Fill Between Graph
# 
# Fill the gap between two graphs
# 

# %%
x = np.linspace(0, 3, 200)

y1 = x**2 + 3
y2 = np.exp(x) + 2
y3 = np.cos(x)

plt.plot(x, y1, label="line1")
plt.plot(x, y2, label="line2")
plt.plot(x, y2, label="line3")

plt.fill_between(x, y1, y2, color="gray", alpha=0.5)
plt.fill_between(x, y1, y3, color="green", alpha=0.5)

# %%
fig, ax = plt.subplots(figsize=(10, 5))

x = np.linspace(0, 2, 100)

y1 = x
y2 = x**2
y3 = x**3

ax.plot(x, y1, label="linear")
ax.plot(x, y2, label="quadratic")
ax.plot(x, y3, label="cubic")

plt.fill_between(x, y1, y2, color="gray", alpha=0.5)
plt.fill_between(x, y1, y3, color="green", alpha=0.5)

ax.legend()

plt.show()


