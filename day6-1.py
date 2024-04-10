print('cd'.partition('cd'))

# output: ('', 'cd', '')

# *******************************************************

# Solutions - 

# Define the input string
# input_string = 'cd'
# Use the partition method to split the string
# result = input_string.partition('cd')
# The 'result' variable now contains a tuple with three elements
# Element 0: The part of the string before the partitioned substring
# Element 1: The partitioned substring itself
# Element 2: The part of the string after the partitioned substring
# Print the result

# print(result)

# In this case, the input string is 'cd', and the partition method is used to split it into three parts. 
# The print statement will display the following result: ('', 'cd', '')

# Here's a breakdown of the result:
# Element 0 is an empty string '' because there is nothing before the partitioned substring 'cd' in the input string.
# Element 1 is the partitioned substring itself, which is 'cd'.
# Element 2 is an empty string '' because there is nothing after the partitioned substring 'cd' in the input string.
# This is the expected output when using the partition method with 'cd' as both the input string and the partitioned substring.