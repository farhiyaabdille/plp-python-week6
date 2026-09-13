# Patient 1
# FIXED: range(1, 10) stops before 10, so the upper bound must be 11.
for i in range(1, 11):
    print(i)

# Patient 2
# FIXED: n was never decreased, so the while loop could not reach its stopping condition.
n = 3
while n > 0:
    print(n)
    n -= 1

# Patient 3
# FIXED: total must be initialized before the loop so each number is accumulated.
total = 0
for i in range(1, 6):
    total = total + i
print(total)
