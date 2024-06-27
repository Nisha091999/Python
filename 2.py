# arr= input("arr :").split()

# even = []
# odd =[]

# # for i in range(len(arr)):
# #     if i % 2==0:

# for i in range(len(arr)): 
#     # print(i, arr[i])
#     if i % 2==0:
#         even.append(int(arr[i]))
#         # print(even)
#     else:
#         odd.append(int(arr[i]))
#         # print(odd)

# even.sort()
# odd.sort()

# output = even[1] + odd[1]
# print(f"Output is {output}")

def LargeSmallSum(arr):
    if len(arr) == 0 or len(arr) <= 3:
        return 0
    
    odd_elements = []
    even_elements = []
    
    # Separate the elements based on their indices
    for i in range(len(arr)):
        if i % 2 == 0:
            even_elements.append(arr[i])
        else:
            odd_elements.append(arr[i])
    
    # Ensure there are at least 2 elements in each list
    if len(odd_elements) < 2 or len(even_elements) < 2:
        return 0
    
    # Find the second smallest in odd_elements and second largest in even_elements
    odd_elements.sort()
    even_elements.sort(reverse=True)
    
    second_smallest_odd = odd_elements[1]
    second_largest_even = even_elements[1]
    
    return second_smallest_odd + second_largest_even


input_str = input("Enter the elements of the array separated by spaces: ").split()


# Convert input list elements to integers manually
arr = []
for elem in input_str:
    arr.append(int(elem))

# Calculate and print the result
result = LargeSmallSum(arr)
print(f"The result is: {result}")
