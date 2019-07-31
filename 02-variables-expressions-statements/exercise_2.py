
# 1
r = 5
pi = 3.14

v = 4/3 * pi * r
print('#1:', 'volume =', v)


# 2
price = 24.95
discount = 40  # in %
cost1 = 3  # for 1st book
cost2 = 0.75  # for each additional book
n = 60  # amount

total = n * price * 40 / 100 + 1 * cost1 + (n-1) * cost2
print('#2:', 'total =', total)


# 3

start = 6 * 60 * 60 + 52 * 60  # 6:52 am
easy_pace = 8 * 60 + 15  # 8:15
tempo_pace = 3 * 7 * 60 + 12  # 3 miles * 7:12

time = easy_pace + tempo_pace + easy_pace
finish = start + time  # in seconds.
