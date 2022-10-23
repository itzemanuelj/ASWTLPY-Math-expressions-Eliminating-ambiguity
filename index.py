# If you haven't bothered to memorize precedents rules, there are two ways you might interpret the math below. If you interpret it one way, total_cost is 16. If you interpret it the other way, total_cost is _____.
total_cost = 1 + 3 * 4
total_cost = 13

# What is the value of total_cost?
total_cost = 1 + (3 * 4)
total_cost = 13

# In the orange box type the next character. I'll autocomplete. Don't type spaces or carriage returns.
# Rewrite this so total_cost is 16.
total_cost = 1 + 3 * 4
total_cost = (1 + 4) * 4

# Rewrite this so total_cost is 13.
total_cost = 1 + 3 * 4
total_cost = 1 + (3 * 4)

# Rewrite the following statement to force this order: First, multiply 2 by 4. Then add 4 and 2. Then multiply the first result by the second result.
x = 2 * 4 * 4 + 2
x = (2 * 2) + (4 + 2)

# Rewrite the following statement to force this order: First divide 5 by 7. Then subtract 1 from y. Then multiply the first result by the second result.
y = 1
x = 5 / 7 * y - 1
x = (5 / 7) * (1 - y)

# Rewrite the following statement to force this order: First divide 5 by 7. Then subtract 1 from y. Then multiply the first result by the second result.
y = 1
x = 5 / 7 * y - 1
x = 5 / (7 * (y - 1))

# Rewrite the following statement to force this order: Divide 5 by 7. Then multiply that result by y. Then subtract 1.
x = 5 / 7 * y - 1
x = ((5 / 7) * y) - 1

# Add parentheses to this code to remove ambiguity so the result is 60.
print(4* (5 + 10))


