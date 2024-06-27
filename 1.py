def differenceofSum(n,m):

    divisible =0
    not_divisible =0
        
    for i in range(1,n +1):
        if i % m == 0:
            divisible +=i
        else:
            not_divisible +=i
    return not_divisible - divisible

m = int(input("m :"))
n = int(input("n :"))

result= differenceofSum(n,m)
print(f"result : {result}")






