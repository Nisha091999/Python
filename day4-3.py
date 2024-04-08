i = 0
while i< 3:
    print(i)
    i+=1
    print(1 + i)
    
# **********************************************
    
# output:
# 0
# 2
# 1
# 3
# 2
# 4

# **********************************************

# i = 0  # Initialize the variable i to 0

# while i < 3:  # Start a while loop that continues as long as i is less than 3

#     print(i)  # Print the current value of i

#     i += 1  # Increment the value of i by 1

#     print(i + 1)  # Print the value of i + 1 after the increment

# Let's break it down step by step:

# i = 0: We initialize a variable i and set its initial value to 0.
# # while i < 3:: This line starts a while loop. The loop will continue executing as long as the value of i is less than 3. In other words, the loop will run when i is 0, 1, or 2, and it will exit when i becomes 3 or greater.
# print(i): Inside the loop, we print the current value of i. The first time through the loop, this will print 0.
# i += 1: After printing the value of i, we increment its value by 1. So, i changes from 0 to 1.
# print(i + 1): We then print the value of i + 1. Since i is now 1, this line will print 2.
# The loop returns to the top, and the process repeats if i is still less than 3. In this case, i is still less than 3 (i.e., 1 is less than 3), so the loop continues.
# The second iteration of the loop starts with i equal to 1.
# print(i): We print the current value of i, which is 1.
# i += 1: We increment i by 1, making it equal to 2.
# print(i + 1): We print i + 1, which is now 3.
# The loop continues for one more iteration with i equal to 2.
# print(i): We print 2.
# i += 1: We increment i to 3.
# print(i + 1): We print i + 1, which is 4.
# The loop condition i < 3 is no longer satisfied because i is now equal to 3. Therefore, the loop exits.
# So, the output of this code will be as follows: 0 2 1 3 2 4