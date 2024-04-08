y = 8
z = lambda x: x*y
print(z(6))

# Output: 48

# In the above code a lambda function z that takes an argument x and multiplies it by the value of y,
# which is set to 8. Then, 
# you call this lambda function with the argument 6 and print the result.

# Here's a step-by-step breakdown of what happens:

# y = 8: You define a variable y and assign it the value 8.

# z = lambda x: x * y: You define a lambda function z that takes an argument x and multiplies it by the value of y. 
# Essentially, it's equivalent to the following regular function definition:

# def z(x):

#     return x * y

# print(z(6)): You call the lambda function z with the argument 6, and 
# it performs the multiplication: 6 * 8, resulting in 48. Then, you print the result, so the output will be: 48